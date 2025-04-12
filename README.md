# Flask Reverse IP Application
This project is a Flask-based web application that provides a simple API to reverse the IP address of the client making the request. It also includes a health check endpoint to monitor the application's status. The application is containerized using Docker and can be deployed to Azure using Azure Container Registry (ACR) and Azure Container Instances (ACI).

## Prerequisites

- Python 3.9 or higher
- Docker
- Azure CLI
- Azure DevOps account (for CI/CD)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/deel-home-task.git
cd deel-home-task
```

### 2. Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/app.py
```

Access the application at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 3. Run with Docker

Build the Docker image:

```bash
docker build -t flask-reverse-ip:latest -f app/Dockerfile .
```

Run the container:

```bash
docker run -p 5000:5000 flask-reverse-ip:latest
```

Access the application at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 4. Run Tests

Run unit tests:

```bash
python -m unittest tests/test-app.py
```

## Deployment to Azure

### 1. Configure Azure Resources

Update the parameters in the Bicep templates located in `ado/templates/`.

### 2. Deploy Using Azure DevOps

Use the pipeline defined in `ado/pipeline/server-build-deploy.yml` to validate, build, and deploy the application.

### 3. Manual Deployment

Login to Azure:

```bash
az login
```

Deploy the Bicep templates:

```bash
az deployment group create \
    --resource-group <RESOURCE_GROUP> \
    --template-file ado/templates/main.bicep \
    --parameters acrName=<ACR_NAME> imageTag=<IMAGE_TAG>
```

## CI/CD Pipeline

The Azure DevOps pipeline (`ado/pipeline/server-build-deploy.yml`) automates the following steps:

1. **Validation**: Runs unit tests to validate the Flask application.
2. **Build and Push**: Builds the Docker image and pushes it to Azure Container Registry.
3. **Deploy**: Deploys the application to Azure Container Instance using Bicep templates.

## Features

- Reverse IP Endpoint: Returns the client's IP address and its reversed version.
- Health Check Endpoint: Provides a simple health status of the application.
- Dockerized: Easily build and run the application in a containerized environment.
- Azure Deployment: Automates deployment to Azure using Bicep templates and Azure DevOps pipelines.

## Endpoints

### 1. Reverse IP Endpoint

- **URL**: `/reverse-ip`
- **Method**: `GET`
- **Description**: Returns the client's IP address and its reversed version.
- **Response**:
    ```json
    {
        "original_ip": "127.0.0.1",
        "reversed_ip": "1.0.0.127"
    }
    ```

### 2. Health Check Endpoint

- **URL**: `/health`
- **Method**: `GET`
- **Description**: Returns the health status of the application.
- **Response**:
    ```json
    {
        "status": "ok"
    }
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any questions or issues, please contact [kkumarmohit@gmail.com](kkumarmohit@gmail.com).