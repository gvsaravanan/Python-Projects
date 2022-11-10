import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Gautham Saravanan'
email['to'] = 'email_address'
email['subject'] = 'This email was sent by my python file!'

email.set_content(html.substitute({'name': 'Test'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('test.email@gmail.com', 'test_password')
  smtp.send_message(email)
  print('all good boss!')