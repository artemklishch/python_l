from email.message import EmailMessage
import smtplib

email1 = EmailMessage()
email1['from'] = 'Bob'
email1['to'] = 'test@gmail.com'
email1['subject'] = "Hello from Python"
email1.set_content("Hey! Hoq are you doing?")

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(email1)
    print("Email was sent!")
