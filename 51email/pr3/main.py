from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

email1 = EmailMessage()
html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'Bob', 'date': 'tomorrow'})

email1['from'] = 'Bob <bs@gmail.com>'
email1['to'] = 'friend@gmail.com'
email1['subject'] = "Email with image"
email1.set_content(html_content, 'html')
with open('images/email.gif', 'rb') as img:  # rb - read binary
    image_data = img.read()
    email1.add_attachment(image_data, maintype='image', subtype='gif', filename='email.gif')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(email1)
    print("Email was sent!")
