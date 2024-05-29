
# Fleetmetrica Login/Screenshot Script

This project automates logging into the FMCSA portal, taking a screenshot, and sending it via email.

## Prerequisites

- Python 3.6+
- Google Chrome and ChromeDriver (or Firefox and geckodriver)
- Docker (for containerization)

- Kubernetes (for deployment)
- SMTP server for sending emails

## Setup

### 1. Clone the Repository

```bash
git clone https://your-repo-url.git
cd selenium_login_project
```

### 2. Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Script

Execute the script by running:

```bash
python login_script.py
```

## Docker Instructions

### 1. Build the Docker Image

```bash
docker build -t selenium-script .
```

### 2. Run the Docker Container

```bash
docker run -it selenium-script
```

## Kubernetes Instructions

### 1. Apply the Deployment

Ensure you have the `deployment.yaml` file in your project directory. Then, apply the deployment:

```bash
kubectl apply -f deployment.yaml
```

## Notes

- Ensure you replace placeholder values in the `.env` file with your actual credentials and settings.
- Make sure your WebDriver is correctly set up and in your system PATH.

---
