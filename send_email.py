import smtplib, ssl


def send_email(email, topic, message):
    host = "smtp.gmail.com"
    port = 465
    username = "gdelucasde@gmail.com"
    receiver = "gdelucasde@gmail.com"
    context = ssl.create_default_context()
    message = f"""\
Subject: {topic}!
{message}
"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(email, receiver, message)