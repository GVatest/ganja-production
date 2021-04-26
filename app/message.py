import smtplib
from config import Config
from email.message import EmailMessage


def send_msg(name, surname, address, content):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)

        msg = EmailMessage()
        msg['From'] = 'NEW MESSAGE'
        msg['To'] = Config.EMAIL_RECEIVER
        msg['Subject'] = name + ' ' + surname
        msg.set_content(' (' + address + ') ' + content)

        smtp.send_message(msg)


def send_review(name, address, content):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Config.EMAIL_SENDER, Config.EMAIL_PASSWORD)

        msg = EmailMessage()
        msg['From'] = 'NEW REVIEW'
        msg['To'] = Config.EMAIL_RECEIVER
        msg['Subject'] = name
        msg.set_content('(' + address + ') ' + content)

        smtp.send_message(msg)

