import smtplib
import ssl
import os

def send_email(message):
    """
    Send Email:
    Function send the email
    """
    host = "smtp.gmail.com"
    port = 465

    username = os.environ.get("username")
    password = os.environ.get("password")

    receiver = os.environ.get("receiver")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
