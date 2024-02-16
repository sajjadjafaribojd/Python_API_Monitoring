import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

# Dictionary mapping endpoints to their corresponding email and SMS recipients
endpoint_recipients = {
    "https://example.com/api/heartbeat1": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat2": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat3": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat4": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat5": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat6": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat7": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat8": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat9": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat10": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"],
    "https://example.com/api/heartbeat11": ["oncall1@gmail.com", "oncall2@gmail.com", "09151234567"]
}

# SMTP configuration
smtp_server = "mail.exmaple.com"
smtp_port = 465
smtp_username = "monitoring@example"
smtp_password = "123456"

def send_email(subject, body, recipients):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipients, msg.as_string())

def send_sms(message, recipients):
    # Implement SMS sending logic here
    print(f"Sending SMS to {recipients}: {message}")

def monitor_endpoints():
    log_file = "monitor_log.txt"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"Monitoring started at {current_time}\n")
    for endpoint, recipients in endpoint_recipients.items():
        try:
            response = requests.get(endpoint)
            if response.status_code != 200:
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"Endpoint {endpoint} returned status code {response.status_code} at {current_time}"
                with open(log_file, "a") as f:
                    f.write(message + "\n")
                send_email("API Monitoring Alert", message, recipients[:2])  # Send email to the first two recipients
                send_sms(message, recipients[2:])  # Send SMS to the next recipient
        except Exception as e:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"Error occurred while accessing endpoint {endpoint}: {str(e)}"
            with open(log_file, "a") as f:
                f.write(message + "\n")
            send_email("API Monitoring Alert", message, recipients[:2])  # Send email to the first two recipients
            send_sms(message, recipients[2:])  # Send SMS to the next recipient

# Call the monitor_endpoints function to run the monitoring
monitor_endpoints()
