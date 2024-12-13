# Error Downloading Dummy Data Plugin

**Command:**

```sh
grafana-cli plugins install simpod-json-datasource
```

**Error:**

```sh
Error: ✗ pluginsDir (/var/lib/grafana/plugins) is not a writable directory
```

## Context

This error occurred in a GitHub Codespaces testing environment where the user does not have the necessary permissions to modify the `/var/lib/grafana/plugins` directory. As a result, the plugin cannot be installed.

## Possible Solutions

1. **Request Elevated Permissions**:
   - Contact the administrator or owner of the environment to request the necessary permissions to modify the directory.

2. **Use a Different Environment**:
   - If possible, use a local development environment or another environment where you have the necessary permissions to install plugins.

3. **Alternative Installation Methods**:
   - Explore alternative methods to install the plugin that do not require modifying the `/var/lib/grafana/plugins` directory, such as using a different directory or containerized solutions.

## Additional Information

- Ensure that you have the necessary permissions to modify system directories in your development environment.
- Consult the Grafana documentation for more details on plugin installation and permissions.
