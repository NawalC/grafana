import http.server
import socketserver
import requests
import socket
import psutil
from psutil import AccessDenied
import yaml
import subprocess
import time

PORT = 8000
GRAFANA_URL = "http://localhost:8085/api/datasources"  # Updated port to 8085

def port_forward_grafana():
    process = subprocess.Popen(
        ["kubectl", "port-forward", "svc/grafana", "8085:3000", "--namespace", "default"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(5)  # Wait for port forwarding to be established
    return process

def get_grafana_admin_password():
    result = subprocess.run(
        ["kubectl", "get", "secret", "grafana-admin", "--namespace", "default", "-o", "jsonpath={.data.GF_SECURITY_ADMIN_PASSWORD}"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return subprocess.run(["base64", "-d"], input=result.stdout, capture_output=True, text=True).stdout.strip()
    else:
        raise Exception("Failed to retrieve Grafana admin password")

def get_grafana_service_account_id(service_account_name):
    grafana_url = "http://localhost:8085"
    grafana_admin_user = "admin"
    grafana_admin_password = get_grafana_admin_password()

    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(f"{grafana_url}/api/serviceaccounts", headers=headers, auth=(grafana_admin_user, grafana_admin_password))
    if response.status_code == 200:
        service_accounts = response.json()
        for account in service_accounts:
            if account['name'] == service_account_name:
                return account['id']
    elif response.status_code == 404:
        print("Service accounts endpoint not found. Ensure Grafana version supports this endpoint.")
        return None  # Add this line to handle the 404 case
    else:
        print(f"Failed to retrieve service accounts: {response.status_code} - {response.text}")
    return None

def create_grafana_service_account():
    service_account_name = "my_service_account"
    service_account_id = get_grafana_service_account_id(service_account_name)
    if service_account_id:
        print("Service account already exists")
        return service_account_id

    grafana_url = "http://localhost:8085"
    grafana_admin_user = "admin"
    grafana_admin_password = get_grafana_admin_password()

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "name": service_account_name,
        "role": "Admin"
    }
    response = requests.post(f"{grafana_url}/api/serviceaccounts", headers=headers, json=data, auth=(grafana_admin_user, grafana_admin_password))
    if response.status_code == 201:
        service_account_id = response.json()['id']
        print("Service account created successfully")
        return service_account_id
    elif response.status_code == 400 and "service account already exists" in response.text:
        print("Service account already exists")
        return get_grafana_service_account_id(service_account_name)
    elif response.status_code == 404:
        print("Service accounts endpoint not found. Ensure Grafana version supports this endpoint.")
        return None  # Add this line to handle the 404 case
    else:
        print(f"Failed to create service account: {response.status_code} - {response.text}")
        return None

def create_grafana_service_account_token(service_account_id):
    grafana_url = "http://localhost:8085"
    grafana_admin_user = "admin"
    grafana_admin_password = get_grafana_admin_password()
    token_name = "my_service_account_token"

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "name": token_name
    }
    response = requests.post(f"{grafana_url}/api/serviceaccounts/{service_account_id}/tokens", headers=headers, json=data, auth=(grafana_admin_user, grafana_admin_password))
    if response.status_code == 200:
        token = response.json()['key']
        print("Service account token created successfully")
        return token
    else:
        print(f"Failed to create service account token: {response.status_code} - {response.text}")
        return None

def create_grafana_api_key():
    service_account_id = create_grafana_service_account()
    if service_account_id:
        return create_grafana_service_account_token(service_account_id)
    else:
        print("Failed to create service account or retrieve existing one.")
        return None

# Start port forwarding
port_forward_process = port_forward_grafana()

# Example usage
GRAFANA_API_KEY = create_grafana_api_key()

def inject_data_to_grafana():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GRAFANA_API_KEY}"
    }
    with open('dummy_data.json', 'r') as file:
        data = file.read()
        response = requests.post(GRAFANA_URL, headers=headers, data=data)
        if response.status_code == 200:
            print("Data injected successfully")
        else:
            print(f"Failed to inject data: {response.status_code} - {response.text}")

def close_existing_connection(port):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for conn in proc.net_connections(kind='inet'):
                if conn.laddr.port == port:
                    proc.terminate()
                    proc.wait()
        except AccessDenied:
            continue  # Ignore processes where access is denied

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/dummy_data.json':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open('dummy_data.json', 'r') as file:
                self.wfile.write(file.read().encode())
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as file:
                self.wfile.write(file.read().encode())
        elif self.path == '/inject_data':
            inject_data_to_grafana()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Data injection initiated")
        else:
            self.send_response(404)
            self.end_headers()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

close_existing_connection(PORT)

try:
    with ReusableTCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
finally:
    port_forward_process.terminate()