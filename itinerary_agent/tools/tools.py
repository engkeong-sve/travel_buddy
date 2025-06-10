import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
from google.adk.tools import ToolContext



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
    
    
def add_user_reminder_item(reminder_title: str, reminder_item: str, tool_context: ToolContext) -> bool:
    """
    Adds a reminder item to the user's reminder list in the tool context.

    Args:
        reminder_title (str): Title of the reminder item.
        reminder_item (str): Description of the reminder item.
        tool_context (ToolContext): Context object to store state and results.

    Returns:
        bool: True if the item was added successfully, False otherwise.
    """
    try:
        if 'reminder_list' not in tool_context.state:
            tool_context.state['reminder_list'] = []

        tool_context.state['reminder_list'].append({
            'title': reminder_title,
            'item': reminder_item,
            'timestamp': datetime.datetime.now()
        })
        print("✅ Reminder item added successfully.")
        return True

    except Exception as e:
        print("❌ Failed to add reminder item:", str(e))
        return False
    
def remove_user_reminder_item(reminder_title: str, tool_context: ToolContext) -> bool:
    """
    Removes a reminder item from the user's reminder list in the tool context.

    Args:
        reminder_title (str): Title of the reminder item to remove.
        tool_context (ToolContext): Context object to store state and results.

    Returns:
        bool: True if the item was removed successfully, False otherwise.
    """
    try:
        if 'reminder_list' in tool_context.state:
            tool_context.state['reminder_list'] = [
                item for item in tool_context.state['reminder_list'] if item['title'] != reminder_title
            ]
            print("✅ Reminder item removed successfully.")
            return True
        else:
            print("❌ Reminder list is empty.")
            return False

    except Exception as e:
        print("❌ Failed to remove reminder item:", str(e))
        return False
    
def get_user_reminder_list(tool_context: ToolContext) -> list:
    """
    Retrieves the user's reminder list from the tool context.

    Args:
        tool_context (ToolContext): Context object to store state and results.

    Returns:
        list: The user's reminder list, or an empty list if no items exist.
    """
    return tool_context.state.get('reminder_list', [])
