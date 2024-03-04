## Orbit D3 Charts Templates

This Flask application serves as a backend for visualizing data from Google Sheets. It uses the `gspread` library to connect to Google Sheets, the `oauth2client` service for authentication, and `pandas` for data manipulation. The app provides endpoints to format and serve data in JSON format suitable for creating hierarchical chart data and graph data consisting of nodes and links.

## Features

- Connect to Google Sheets to fetch data using OAuth2 authentication.
- Convert spreadsheet data into JSON format for use in charts.
- Serve hierarchical chart data and graph data through RESTful APIs.
- Enable CORS for cross-origin requests.

## Installation

Before running the application, ensure you have Python and pip installed on your system. Then, follow these steps to install the necessary dependencies:

1. Clone the repository to your local machine.
2. Navigate to the application's root directory in your terminal.
3. Install the required Python packages using pip:

```bash
pip install Flask gspread oauth2client pandas flask-cors
```

4. Obtain Google Sheets API credentials:

   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project.
   - Enable the Google Sheets API for your project.
   - Create credentials for a service account.
   - Download the JSON key file for the service account.
5. Place the service account's JSON key file in the application's root directory and rename it to `credentials.json`. If you use different names or multiple credential files, adjust the file paths in the code accordingly.

## Usage

To start the Flask application, run the following command in the terminal from the application's root directory:

```bash
flask run --host=0.0.0.0 --port=8080
```

### Endpoints

- `GET /getnodeschartdata`: Fetches and returns graph data for nodes and links from a specified Google Sheet.
- `GET /getchartdata`: Fetches and formats data from a Google Sheet to serve as hierarchical chart data.

### Accessing the API

You can access the API endpoints using tools like `curl` or Postman, or by making requests from your frontend application. Here's an example `curl` command to access the `/getchartdata` endpoint:

```bash
curl -X POST http://localhost:8080/getchartdata
```

## Customization

To customize the application for different datasets or spreadsheets, you may need to modify the `spreadsheetConnect` function parameters to match your Google Sheets file names and sheet indices. Additionally, the `formatData` function can be adjusted to cater to different data structures.

