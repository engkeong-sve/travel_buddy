import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def get_current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")



def send_email(to_email: str, subject: str, html_body: str) -> bool:
    """
    Sends an email with HTML content using Gmail SMTP.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject line.
        html_body (str): HTML content of the email.

    Returns:
        bool: True if email was sent successfully, False otherwise.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        # Compose the email
        from_email = os.getenv("EMAIL_ADDRESS")
        app_password = os.getenv("EMAIL_APP_PASSWORD")
        msg = MIMEMultipart("alternative")
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(html_body, "html"))

        # Send via Gmail SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, app_password)
            server.sendmail(from_email, to_email, msg.as_string())

        print("✅ Email sent successfully.")
        return True

    except Exception as e:
        print("❌ Failed to send email:", str(e))
        return False