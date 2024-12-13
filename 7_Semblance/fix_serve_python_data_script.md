
# Grafana Dummy Data Injection Script

The Python script `serve_dummy_data.py` is designed to facilitate the injection of dummy data into a Grafana instance running in a Kubernetes cluster. The script handles several key tasks, including port forwarding, retrieving Grafana admin credentials, creating service accounts and tokens, and injecting data into Grafana.

## Key Functions and Their Roles

1. **Port Forwarding**:
   The `port_forward_grafana` function establishes a port-forwarding connection to the Grafana service running in the Kubernetes cluster. It first checks if the default port (8085) is in use using the `is_port_in_use` function. If the port is occupied, it switches to an alternative port (8086). This ensures that the script can still function even if the default port is unavailable.

   ```python
   def is_port_in_use(port):
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           return s.connect_ex(('localhost', port)) == 0

   def port_forward_grafana():
       port = 8085
       if is_port_in_use(port):
           print(f"Port {port} is already in use. Trying a different port.")
           port = 8086
       process = subprocess.Popen(
           ["kubectl", "port-forward", "svc/grafana", f"{port}:3000", "--namespace", "default"],
           stdout=subprocess.PIPE,
           stderr=subprocess.PIPE
       )
       time.sleep(5)
       return process, port
   ```plaintext

2. **Retrieving Grafana Admin Password**:

   The `get_grafana_admin_password` function retrieves the Grafana admin password from a Kubernetes secret. This password is necessary for authenticating API requests to Grafana.

3. **Creating Service Accounts and Tokens**:
   The script includes functions to create a Grafana service account and generate an API token for it. These functions ensure that the script can authenticate and interact with the Grafana API.

   ```python
   def create_grafana_service_account():
       # ...existing code...
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
           return None
       else:
           print(f"Failed to create service account: {response.status_code} - {response.text}")
           return None
   ```

4. **Injecting Data into Grafana**:
   The `inject_data_to_grafana` function reads dummy data from a JSON file and sends it to Grafana using an HTTP POST request. This function uses the API token generated earlier for authentication.

   ```python
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
   ```

### Handling Errors

The script includes error handling to manage various scenarios, such as:

- **Port in Use**: If the default port is in use, the script switches to an alternative port.
- **Failed API Requests**: The script checks the status codes of API responses and prints appropriate error messages if requests fail.
- **Access Denied**: When closing existing connections, the script handles `AccessDenied` exceptions to avoid crashing.

By addressing these potential issues, the script ensures a smoother and more reliable operation when interacting with Grafana.

#### Examples of Errors

Here are some examples of errors you might encounter and their causes:

1. **Connection Refused**:
   This error occurs when the script tries to connect to a port that is not open or the Grafana service is not running.

   ```bash
   ConnectionRefusedError: [Errno 111] Connection refused
   ```

2. **Max Retries Exceeded**:
   This error occurs when the script fails to establish a connection after multiple attempts.

   ```bash
   urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=8085): Max retries exceeded with url: /api/serviceaccounts (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x79f08343baa0>: Failed to establish a new connection: [Errno 111] Connection refused'))
   ```

By addressing these potential issues, the script ensures a smoother and more reliable operation when interacting with Grafana.

Overall, this Python script automates the process of setting up and injecting data into Grafana, making it easier to manage and test Grafana dashboards in a Kubernetes environment.
