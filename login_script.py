from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyotp
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

# Load environment variables from .env file
# todo: AWS Secrets Manager to store sensitive data
#load the environment variables if they do not exist
if not os.getenv('EMAIL'):
    load_dotenv()
# otherwise, use the environment variables injected by Kubernetes

# Constants from environment variables
LOGIN_URL = "https://portal.fmcsa.dot.gov/login"
LOGIN_GOV_LINK_TEXT = "Sign in with Login.gov"
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
OTP_SECRET = os.getenv('OTP_SECRET')
SCREENSHOT_PATH = 'login_success.png'
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))
FROM_EMAIL = os.getenv('FROM_EMAIL')
FROM_EMAIL_PASSWORD = os.getenv('FROM_EMAIL_PASSWORD')
TO_EMAILS = os.getenv('TO_EMAILS', '').split(',')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

def take_screenshot(driver, path):
    driver.save_screenshot(path)
    img = Image.open(path)
    img.show()

#todo: use aws email service to send email
def send_email(subject, body, attachment_path):
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = ', '.join(TO_EMAILS)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(FROM_EMAIL, FROM_EMAIL_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAILS, msg.as_string())

def main():
    # Set up WebDriver options
    
    # note: use the headless mode in the docker environment or when running in a CI/CD pipeline
    chrome_options = Options()
    if ENVIRONMENT == 'docker':
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(LOGIN_URL)

    # Click "Sign in with Login.gov"
    sign_in_button = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.LINK_TEXT, LOGIN_GOV_LINK_TEXT))
    )
    sign_in_button.click()

    # Wait for the login page to load and enter email
      #lets use the name attribute instead of id
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "user[email]"))
    )
    email_input.send_keys(EMAIL)

    # Enter password
    password_input = driver.find_element(By.NAME, "user[password]")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    # Wait for 2FA input

    otp_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@id, 'code')]"))
    )
    # Generate OTP
    totp = pyotp.TOTP(OTP_SECRET)
    otp = totp.now()

    # Enter OTP
    otp_input.send_keys(otp)
    otp_input.send_keys(Keys.RETURN)

    # Wait for login to complete
    #use a time.sleep instead of WebDriverWait
    time.sleep(7)
    # Take a screenshot
    take_screenshot(driver, SCREENSHOT_PATH)
    driver.quit()

    # Send email
    send_email(
        subject="Login Screenshot",
        body="Attached is the screenshot of the successful login.",
        attachment_path=SCREENSHOT_PATH
    )

if __name__ == "__main__":
    main()
