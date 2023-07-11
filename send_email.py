from dotenv import load_dotenv
import os
import smtplib, ssl

load_dotenv()


def send_email(email, topic, message):
    username = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    port = int(os.environ.get('PORT'))
    receiver = username
    context = ssl.create_default_context()
    message = f"""\
Subject: {topic}!
{message}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(email, receiver, message)