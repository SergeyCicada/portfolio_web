import smtplib
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv


def send_email(message: str) -> str:
    """
        Function for sending message by email
    """
    load_dotenv()

    sender = os.environ.get('MAIL_SENDER')
    password = os.environ.get('MAIL_PASSWORD')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Work"
        server.sendmail(sender, sender, msg.as_string())
    except Exception as e:
        return f"{e}, Error"


