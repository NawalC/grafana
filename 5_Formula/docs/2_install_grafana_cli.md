# Install Grafana CLI

1. **Ensure Grafana is Installed**:
    - If Grafana is not installed, you can install it using Helm by following the instructions on the [Grafana installation page](https://grafana.com/docs/grafana/latest/installation/kubernetes/).

2. **Add Grafana CLI to PATH**:
    - If Grafana is installed but `grafana-cli` is not in your PATH, you need to add it. Typically, Grafana CLI is located in the Grafana installation directory.

3. **Install Grafana CLI**:
    - If Grafana CLI is not installed, you can install it using the following commands:

    ```sh
    # Verify- Run the following command to add the public key:
    curl https://packages.grafana.com/gpg.key | sudo apt-key add -

    # Refresh the package list to include the latest packages from the newly added Grafana repository:
    sudo apt-get update

    # Install Grafana CLI using the apt package manager:
    sudo apt-get install grafana
    ```

4. **Start Grafana Service**:
    - Since `systemd` is not running in your container, use the `service` command to start the Grafana service:

    ```sh
    sudo service grafana-server start
    ```

## Updated Script: `grafana_cli_install.sh`

```bash
#!/bin/bash

# Step 1: Add the Grafana GPG key to your system.
curl https://packages.grafana.com/gpg.key | sudo apt-key add -

# Step 2: Update the package list to include the latest packages from the newly added Grafana repository.
sudo apt-get update
