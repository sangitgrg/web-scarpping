import smtplib,ssl
from email.mime.text import MIMEText

def SendMail(messages):
    port = 465 #forssl
    smtp_server = 'smtp.gmail.com'
    sender_email = ''
    receiver_email =['']

    password = '' #input('type-your-password-here: ')
    msg = MIMEText(messages)
    msg['Subject'] = 'Room notification'
    msg['From'] = ''
    msg['To'] = ''

    #using a secure ssl context
    context = ssl.create_default_context()
    #this will be used to send our mail

    with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,msg.as_string())