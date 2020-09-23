import smtplib, ssl
from celery import Celery
import gevent
import virtualenv
from time import sleep

app=Celery('tasks',broker='amqp://localhost',
            backend='rpc://')

@app.task
def sendmail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "anushamanoj19@gmail.com"  # Enter your address
    receiver_email = "anushamanoj1996@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = """\
    Subject: Celery mini project

    This is my second celery mini project.

    Thank You!"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        sleep(15)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!!!")

if __name__=="__main__":
    sendmail()

