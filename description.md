# Selenium Script Description

## Overview

This script automates the login process to the FMCSA portal using Selenium WebDriver. It navigates to the login page, clicks the "Sign in with Login.gov" button, enters the provided credentials, handles two-factor authentication (2FA) using PyOTP, takes a screenshot upon successful login, and sends an email with the screenshot attached.

## Features

1. **Automated Login**:
   - Navigates to the FMCSA portal login page.
   - Clicks the "Sign in with Login.gov" button.
   - Enters the provided email and password.

2. **Two-Factor Authentication (2FA)**:
   - Generates a one-time password (OTP) using PyOTP.
   - Enters the OTP to complete the login process.

3. **Screenshot Capture**:
   - Takes a screenshot after a successful login.
   - Saves the screenshot as `login_success.png`.

4. **Email Notification**:
   - Sends an email with the screenshot attached.
   - Uses SMTP settings provided via environment variables.

5. **Environment Configuration**:
   - Configurable via environment variables for flexibility and security.
   - Supports running in different environments (e.g., development, Docker).

## Environment Variables

The script uses the following environment variables to configure its behavior:

- `LOGIN_URL`: The URL of the FMCSA portal login page.
- `LOGIN_GOV_LINK_TEXT`: The link text for the "Sign in with Login.gov" button.
- `EMAIL`: The email address used for login.
- `PASSWORD`: The password used for login.
- `OTP_SECRET`: The secret key for generating OTP.
- `SCREENSHOT_PATH`: The path to save the screenshot.
- `SMTP_SERVER`: The SMTP server address.
- `SMTP_PORT`: The SMTP server port.
- `FROM_EMAIL`: The sender email address.
- `FROM_EMAIL_PASSWORD`: The password for the sender email address.
- `TO_EMAILS`: The recipient email addresses (comma-separated).
- `ENVIRONMENT`: The environment in which the script is running (e.g., `development`, `docker`).

## Fallbacks and Error Handling

1. **Timeouts**:
   - The script uses WebDriverWait to wait for elements to be clickable or present.
   - If an element is not found within the specified timeout, an exception is raised.

## Usage

1. **Running Locally**:
   - Ensure the required environment variables are set.
   - Install dependencies using: `pip install -r requirements.txt`
   - Run the script using Python: `python login_script.py`.

2. **Running in Docker**:
   - Build the Docker image: `docker build -t selenium-script:latest .`
   - Run the Docker container: `docker run -it selenium-script:latest`

3. **Deploying to Kubernetes (locally) **:
   - Start Minikube: `minikube start`
   - Configure Docker CLI to use Minikube's Docker daemon: `eval $(minikube -p minikube docker-env)`
   - Build the Docker image: `docker build -t selenium-script:latest .`
   - Apply the ConfigMap and Secret: `kubectl apply -f configmap.yaml && kubectl apply -f secret.yaml`
   - Apply the Deployment: `kubectl apply -f deployment.yaml`
   - Check the status of the pods: `kubectl get pods`
   - Check the logs of the pods: `kubectl logs <pod-name>`

## Prerequisites

- Python 3.6 or later.
- Selenium WebDriver.
- Google Chrome and ChromeDriver.
- Docker (for running in a Docker container).
- Minikube (for local Kubernetes deployment).

## Dependencies

The script requires the following Python packages:

- selenium
- pyotp
- pillow
- smtplib
- email
- os
- sys

## Future Additions

1. **Secrets Management**:
   - Integrate AWS Secrets Manager to securely manage sensitive information like email passwords, OTP secrets, and other credentials.
   - Replace environment variables with secrets fetched dynamically from AWS Secrets Manager.

2. **AWS Email Service**:
   - Integrate AWS Simple Email Service (SES) for sending emails.
   - Utilize AWS SES to improve email sending reliability and scalability, replacing the current SMTP configuration.

3. **Enhanced Error Handling and Logging**:
   - Implement structured logging for better tracking and debugging.
   - Add more detailed error handling and retry mechanisms for robust operation.

4. **Scalability and Monitoring**:
   - Add support for horizontal scaling and load balancing in Kubernetes.
   - Integrate monitoring tools like Prometheus and Grafana to track the performance and health of the application.
