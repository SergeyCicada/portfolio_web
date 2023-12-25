import smtplib
from email.mime.text import MIMEText


def send_email(message: str) -> str:

    sender = ""
    password = ""

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Work"
        server.sendmail(sender, sender, msg.as_string())
    except Exception as e:
        return f"{e}, Error"


