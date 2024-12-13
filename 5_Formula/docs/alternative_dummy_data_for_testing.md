# Alternative Dummy Data for Testing

You can use this JSON data in your testing environment by serving it through a simple HTTP server or by loading it directly into your application. Here is an example of how to serve this JSON data using Python's built-in HTTP server:

Save the JSON data to a file named `dummy_data.json`.

Create a simple HTTP server to serve the JSON file:

## Alternative Dummy Data for Basic Testing

Here is an example of dummy JSON data that you can use for basic testing:

```json
{
    "header": "Dummy Data for Testing",
    "metadata": {
        "HTTP/2": "200",
        "date": "Fri, 13 Dec 2024 16:39:29 GMT",
        "content-type": "application/json",
        "content-length": "134",
        "cache-control": ["no-cache", "no-store"],
        "expires": "Thu, 01 Jan 1970 00:00:00 GMT",
        "pragma": ["no-cache", "no-cache"],
        "set-cookie": ".Tunnels.Relay.WebForwarding.Cookies=CfDJ8E0FHi1JCVNKrny-ARCYWxPqdDoRwMQ0Rj8SuGGrNeDrUuINI2SJIxbzFG0glm-6TLIii65nyD5yVlSwMC6ZJdJvHzJtdpNQslBX3Gz6dGJ7ZtpZvL5pc9DgZ01ujTf8iyFifFyFz7T9fRw34X2VXW3v1pqfubW3noCYuvxCWsJloAbhA6qfe7LA7brCJc0vXjdGf_m-cKmWTt2ASFiz-bIZg5tMppWpfVP1LEak9wsQpiGml76vmWwocjXIgzTj3Gng2lV1ku0UbuBT2-FOXv5tofMBgW6q068zNrlTlmxlKXL_atCKX2L3W3K0KdFkwP5Vr7gsNEBwoMIDaylU31IlDQ-bOQeaFuLxQYS7bfGlwGGaXtVaxIAYUpSzOQxMAyMcG8ZxwHh7a5ZqXMd_FzIcH_IOB-GOh9h4K_kOikSQVDtVskM7aBF84_VUqdCRhLa3xC2Jls08fDctO6xeFh4FcBD9phNQovn69PDs8xtiVSJcP3qi2zcwRlGkoGeRBJD2R_vxU7Xak3a6cPInfDPynW8I2nnAlHqcEpFLR0l4BuABOIVotA7mEbqZjMfYpVePu-h0knK2sP46KRY51oAlmdYv1kCgYiTNxkV-9VfmAdvINxjTmqvj1RRapeTSYMEpp404F-_rz-P5K9RpE7BqNPT5JwxJlvulo3RlDpjAJRX1o-aVDlhXPUg7UZxpE8Y7vyLTqewGHNtKQP4SoPwe6P63pgplpiz1QVlLzqWV7gLr0o6w35Ij6SMkF-645X4ucE88GZ4Rar9fzEX11bupfYhpZlqUu_H8N_m55O8V2lVbb-jf9QIAqM9unJaT2IO_yYFQhscDj-OwgOcSCk1Iaj8EgUfbml7rPDz_2bq5tFBdO-WBw-QvzkfWc5FPqztTfhN_EpQ-BXG5xgVcFz43ollU9-x-kgrqZfBOpskJWhvur-tTxYyxc8oN-mQa1eaHOQeVDjauaRd797SsHTpXUT2W7C7i78Gs4_fzZMW05xjab83rR0Vd9xA4w6LyrQ; path=/; secure; samesite=none",
        "via": "1.1 grafana",
        "x-content-type-options": ["nosniff", "nosniff"],
        "ratelimit-limit": ["HttpRequestRatePerPort:1500/m", "ClientConnectionsPerPort: max 1000"],
        "ratelimit-remaining": ["HttpRequestRatePerPort:1499", "ClientConnectionsPerPort:1000"],
        "ratelimit-reset": ["HttpRequestRatePerPort:38s", "HttpRequestRatePerPort:1s"],
        "x-report-abuse": ["https://msrc.microsoft.com/report/abuse", "https://msrc.microsoft.com/report/abuse"],
        "x-ms-ratelimit-limit": ["1500", "1500"],
        "x-ms-ratelimit-remaining": ["1497", "1496"],
        "x-ms-ratelimit-used": ["3", "4"],
        "x-ms-ratelimit-reset": ["0", "0"],
        "content-security-policy": "sandbox",
        "referrer-policy": "same-origin",
        "vssaas-request-id": "8add10ff-6e99-44ca-90c0-1136f315714c",
        "x-frame-options": "deny",
        "x-robots-tag": "noindex, nofollow",
        "x-served-by": "tunnels-prod-rel-uks1-v3-cluster",
        "x-xss-protection": "1; mode=block",
        "strict-transport-security": "max-age=31536000; includeSubDomains"
    },
    "data": [
        {
            "timestamp": "2023-10-01T00:00:00Z",
            "value": 10
        },
        {
            "timestamp": "2023-10-01T01:00:00Z",
            "value": 15
        },
        {
            "timestamp": "2023-10-01T02:00:00Z",
            "value": 20
        },
        {
            "timestamp": "2023-10-01T03:00:00Z",
            "value": 25
        },
        {
            "timestamp": "2023-10-01T04:00:00Z",
            "value": 30
        }
    ]
}
```

To check if Python is installed in your environment, you can run the following command in your terminal:

```sh
python --version
```

or

```sh
python3 --version
```

If Python is installed, this command will display the version of Python that is currently installed. If Python is not installed, you will need to install it before running the script.

Save the following Python script to a file named `serve_dummy_data.py`:

```python
import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
                if self.path == '/dummy_data.json':
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        with open('dummy_data.json', 'r') as file:
                                self.wfile.write(file.read().encode())
                else:
                        self.send_response(404)
                        self.end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
```

Save the following HTML content to a file named `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dummy Data Server</title>
</head>
<body>
    <h1>Welcome to the Dummy Data Server</h1>
    <p>Access the dummy JSON data at <a href="/dummy_data.json">/dummy_data.json</a>.</p>
</body>
</html>
```

Run the Python script to start the server:

```sh
python serve_dummy_data.py
```

Access the dummy JSON data at `http://localhost:8000/dummy_data.json`.

By following these steps, you can serve the dummy JSON data for basic testing in your environment.
