# FastAPI Slack Events Receiver

This FastAPI application serves as an event receiver from Slack, storing messages in a JSON file and offering an endpoint to retrieve stored messages.

## Requirements

- Python 3.x
- Pip (Python package installer)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/your_backend_repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_backend_repository
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Ensure you have the necessary credentials for the Slack API.

2. Update the `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI` variables in the `app.py` file with your Slack OAuth app credentials.

## Running the Application

To run the FastAPI application, execute the following command in your terminal:

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
This will start the FastAPI application and make it accessible at http://localhost:8080.
```

### Running with HTTPS using Nginx and Ngrok
Install and configure Nginx to proxy requests to your FastAPI application.

Install Ngrok and run it to create a secure tunnel to your local server:

```bash
ngrok http 8080
```

Ngrok will provide a secure HTTPS URL (e.g., https://your-ngrok-url.ngrok.io). Update the REDIRECT_URI variable in the app.py file with this URL.

Restart your FastAPI application.

Access your FastAPI application via the HTTPS URL provided by Ngrok.

### Usage
Once the application is running, you can send Slack events to the /slack/events endpoint.

To fetch stored messages, make a GET request to the /slack/messages endpoint.

You can customize the CORS settings in the app.py file to allow specific origins to access the API.

### Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License.
Feel free to adjust the content according to your specific setup and requirements.