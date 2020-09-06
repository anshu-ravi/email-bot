import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# sender email address
email_user = 'youremail@gmail.com'

# sender email password for login purposes
email_password = 'your_password'

# list of users to whom email is to be sent
email_send = ['to_email@gmail.com']
subject = 'EMAIL_SUBJECT'
msg = MIMEMultipart()
msg['From'] = email_user
# converting list of recipients into comma separated string
# msg['To'] = ", ".join(email_send)
msg['Subject'] = subject
body = 'Enter text here'
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)
server.sendmail(email_user, email_send, text)
server.quit()
