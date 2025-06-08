import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from google.adk.tools import ToolContext

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
    
    
def add_user_todo_item(todo_title: str, todo_item: str, tool_context: ToolContext) -> bool:
    """
    Adds a todo item to the user's todo list in the tool context.

    Args:
        todo_title (str): Title of the todo item.
        todo_item (str): Description of the todo item.
        tool_context (ToolContext): Context object to store state and results.

    Returns:
        bool: True if the item was added successfully, False otherwise.
    """
    try:
        if 'todo_list' not in tool_context.state:
            tool_context.state['todo_list'] = []

        tool_context.state['todo_list'].append({
            'title': todo_title,
            'item': todo_item,
            'timestamp': get_current_datetime()
        })
        print("✅ Todo item added successfully.")
        return True

    except Exception as e:
        print("❌ Failed to add todo item:", str(e))
        return False
    
def remove_user_todo_item(todo_title: str, tool_context: ToolContext) -> bool:
    """
    Removes a todo item from the user's todo list in the tool context.

    Args:
        todo_title (str): Title of the todo item to remove.
        tool_context (ToolContext): Context object to store state and results.

    Returns:
        bool: True if the item was removed successfully, False otherwise.
    """
    try:
        if 'todo_list' in tool_context.state:
            tool_context.state['todo_list'] = [
                item for item in tool_context.state['todo_list'] if item['title'] != todo_title
            ]
            print("✅ Todo item removed successfully.")
            return True
        else:
            print("❌ Todo list is empty.")
            return False

    except Exception as e:
        print("❌ Failed to remove todo item:", str(e))
        return False
    
def get_user_todo_list(tool_context: ToolContext) -> list:
    """
    Retrieves the user's todo list from the tool context.

    Args:
        tool_context (ToolContext): Context object to store state and results.

    Returns:
        list: The user's todo list, or an empty list if no items exist.
    """
    return tool_context.state.get('todo_list', [])
