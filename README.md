
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

### 2. Create a `.env` File

Create a `.env` file in the project root directory with the following content:

```plaintext
EMAIL=your_email@example.com
PASSWORD=your_password
OTP_SECRET=your_otp_secret
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
FROM_EMAIL=your_email@example.com
FROM_EMAIL_PASSWORD=your_email_password
TO_EMAIL=recipient_email@example.com
```

### 3. Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the Script

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