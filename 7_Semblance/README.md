# Semblance

| **Key Error** | **Fix** | **References** |
|---------------|---------|----------------|
| `bash: grafana-cli: command not found` | Ensure that `grafana-cli` is installed and added to your system's PATH. | [ERROR_RUNNING_SCRIPT.MD](./ERROR_RUNNING_SCRIPT.MD) |
| `bash: ./grafana_cli_install: No such file or directory` | Verify that the `grafana_cli_install` script exists in the current directory and has execute permissions. | [ERROR_RUNNING_SCRIPT.MD](./ERROR_RUNNING_SCRIPT.MD) |
| `Error: ✗ pluginsDir (/var/lib/grafana/plugins) is not a writable directory` | Request elevated permissions or use an environment where you have write access to `/var/lib/grafana/plugins`. | [ERROR_DOWNLOADING_DUMMY_DATA_PLUGIN.MD](./ERROR_DOWNLOADING_DUMMY_DATA_PLUGIN.MD) |
| `ConnectionRefusedError: [Errno 111] Connection refused` | Ensure that the Grafana service is running and listening on the specified port. | [FIX_SERVE_PYTHON_DATA_SCRIPT.MD](./FIX_SERVE_PYTHON_DATA_SCRIPT.MD) |
| `urllib3.exceptions.MaxRetryError: HTTPConnectionPool...` | Check network connectivity and Grafana service availability, then retry the connection. | [FIX_SERVE_PYTHON_DATA_SCRIPT.MD](./FIX_SERVE_PYTHON_DATA_SCRIPT.MD) |
| `kubectl get secret grafana-admin --namespace default -o jsonpath="{.data.GF_SECURITY_ADMIN_PASSWORD}" \| base64 -d` | Use this command to retrieve the Grafana admin password. | [FIX_SERVE_PYTHON_DATA_SCRIPT.MD](./FIX_SERVE_PYTHON_DATA_SCRIPT.MD) |
