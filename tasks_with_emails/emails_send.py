import smtplib
import getpass
from email.mime.text import MIMEText

email = getpass.getpass('Please enter your email')
password = getpass.getpass('Please enter your password')
subject = "TEST email subject"
body = "This is the body of the TEST text message"
sender = email
recipient = email

def send_email_1(subject, body, sender, recipient, password):
    """Option 1 - function for sending email"""
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(email, password)
    header = f'To: {recipient}\n' + f'From: {sender}\n' + f'Subject: {subject}\n'
    msg = header + f'\n {body}\n\n'
    smtp_server.sendmail(sender, recipient, msg)
    print('Message sent!')
    smtp_server.quit()


send_email_1(subject, body, sender, recipient, password)


def send_email_2(subject, body, sender, recipient, password):
    """Option 2 - function for sending email"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")


send_email_2(subject, body, sender, recipient, password)
