# Create a Dummy JSON Data Source in Grafana

## Prerequisites

1. **Install Grafana CLI**:

   - If Grafana CLI is not installed, refer to the [Grafana CLI installation guide](link_to_installation_guide).

2. **Ensure Grafana is Installed**:

   - If Grafana is not installed, follow the instructions on the [Grafana installation page](https://grafana.com/docs/grafana/latest/installation/).

3. **Run the Plugin Installation Command**:

   - Once Grafana CLI is installed and in your PATH, you can run the plugin installation command:

   ```sh
   grafana-cli plugins install simpod-json-datasource
   ```

By following these steps, you should be able to install the `simpod-json-datasource` plugin using `grafana-cli`.

## Install the JSON Data Source Plugin

1. **Install the JSON Data Source Plugin**:

   - Navigate to the Grafana plugins directory.
   - Install the JSON data source plugin using the following command:

   ```sh
   grafana-cli plugins install simpod-json-datasource
   ```

   - Restart the Grafana server to load the new plugin.

2. **Add the JSON Data Source**:

   - Open Grafana and go to **Configuration** > **Data Sources**.
   - Click on **Add data source**.
   - Select **JSON** from the list of available data sources.

3. **Configure the JSON Data Source**:

   - Set the **Name** for your data source.
   - Enter the **URL** of your JSON endpoint. For dummy data, you can use a local server or a mock API service.
   - Save & Test the data source to ensure it is working correctly.

4. **Create a Dashboard with Dummy Data**:

   - Go to **Create** > **Dashboard**.
   - Add a new panel and select the JSON data source you created.
   - Configure the panel to display the dummy data from your JSON endpoint.

Example of dummy JSON data:

```json
[
  {
    "time": "2023-01-01T00:00:00Z",
    "value": 10
  },
  {
    "time": "2023-01-01T01:00:00Z",
    "value": 15
  },
  {
    "time": "2023-01-01T02:00:00Z",
    "value": 20
  }
]
```

This will help you visualize dummy data in Grafana using the JSON data source.

## Add Data Source to Grafana via Code

You can also add the JSON data source to Grafana programmatically using the Grafana HTTP API. Here is an example using `curl`:

1. **Create a JSON file** (`json_data_source.json`) with the following content:

   ```json
   {
     "name": "Dummy JSON Data Source",
     "type": "simpod-json-datasource",
     "url": "http://localhost:3000",
     "access": "proxy",
     "basicAuth": false
   }
   ```

2. **Use `curl` to add the data source**:

   ```sh
   curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY"\
   -d @json_data_source.json http://localhost:3000/api/datasources
   ```

Replace `YOUR_API_KEY` with your Grafana API key. This will add the JSON data source to your Grafana instance.
