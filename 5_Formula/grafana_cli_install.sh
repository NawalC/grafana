#!/bin/bash
# Step 0: Add the Grafana GPG key to your system.
curl https://packages.grafana.com/gpg.key | sudo apt-key add -
# Step 1: Install software-properties-common package, which provides an abstraction of the used apt repositories.
sudo apt-get install -y software-properties-common

# Step 2: Add the Grafana APT repository to your system's software repository list.
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"

# Step 3: Update the package list to include the latest packages from the newly added Grafana repository.
sudo apt-get update