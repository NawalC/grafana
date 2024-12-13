# Install Grafana in Minikube using Bitnami

## Summary

Easily deploy Grafana on Minikube with Bitnami's Helm chart.

## Prerequisites

### Start Minikube

Ensure Minikube is running:

```sh
minikube start
```

### Check Minikube Status

Verify Minikube status:

```sh
minikube status
```

### Check if Helm is Installed

Confirm Helm installation:

```sh
helm version
```

If Helm is not installed, follow the [official Helm installation guide](https://helm.sh/docs/intro/install/).

### Add Bitnami Repo

Add the Bitnami repository:

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

### Update Helm

Update Helm repositories:

```sh
helm repo update
```

### Install Grafana

Deploy Grafana using Helm:

```sh
helm install grafana bitnami/grafana
```

### Access Grafana

Forward Grafana service to localhost:

```sh
kubectl port-forward svc/grafana 8080:3000 &
```

## Notes

- Ensure Minikube is running before starting the installation.
- Use `kubectl get all` to check the status of your Grafana deployment.

Enjoy your Grafana setup! 🎉
