# Error Running Script

```markdown

## Steps to Reproduce

1. Navigate to the `5_Formula` directory:
    ```sh
    @NawalC >/workspaces/grafana (main) $ cd 5_Formula/
    ```

2. Attempt to install the `simpod-json-datasource` plugin:
    ```sh
    @NawalC >/workspaces/grafana/5_Formula (main) $ grafana-cli plugins install simpod-json-datasource
    ```
    **Error:** `bash: grafana-cli: command not found`

3. Attempt to run the `grafana_cli_install` script:
    ```sh
    @NawalC ->/workspaces/grafana/5_Formula (main) $ ./grafana_cli_install
    ```
    **Error:** `bash: ./grafana_cli_install: No such file or directory`

4. Make the `grafana_cli_install.sh` script executable:
    ```sh
    @NawalC ->/workspaces/grafana/5_Formula (main) $ chmod +x grafana_cli_install.sh
    ```

5. Run the `grafana_cli_install.sh` script:
    ```sh
    @NawalC >/workspaces/grafana/5_Formula (main) $ ./grafana_cli_install.sh
    ```
    **Output:** `Reading package lists ... Done`

## Additional Information

- `resourceVersion: ""`

## Screenshot of Error

