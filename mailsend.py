#mail sending program with attachment
import os
import smtplib
from email.message import EmailMessage

def send_mail(sender,app_password, receiver, subject, body, attachment_path):
    if not os.path.exists(attachment_path):
        print("Attachment not found")
        return
    
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    with open(attachment_path, "rb") as fobj:
        data = fobj.read()

    msg.add_attachment(data, maintype="text", subtype="plain",filename = os.path.basename(attachment_path))
    
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(sender,app_password)
        smtp.send_message(msg)

    print("Mail sent successfully")


sender = "corestack.connect@gmail.com"
app_password = "ymme lpvf qpye vjjo"
receiver = "kundanjangale8@gmail.com"
subject = "Demo mail with attachment"
body = "This is a demo mail sent through python program"
attachment_path = "sample.log"

send_mail(sender,app_password,receiver,subject,body,attachment_path)

"""
K:\PythonTeaching\sample.log

sample.log

"""