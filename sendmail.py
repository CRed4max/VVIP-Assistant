import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import os

def send_email(data):
   
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context =context)
    server.ehlo()

    # sender_gmail = data['sender_email']
    # sender_password = data['sender_password']
    # receiver_gmail = data['receiver_email']
    # subject_mail = data['subject_mail']
    # message = data['message_body']
    # attachment = data['attachement_path']

    sender_gmail = data[0]
    sender_password = data[1]
    receiver_gmail = data[2]
    subject_mail = data[3]
    message = data[4]
    attachment = data[5]


    server.login(sender_gmail, sender_password)

    msg1  = MIMEMultipart()
    msg1['From'] = sender_gmail
    msg1['To'] = receiver_gmail
    msg1['Subject'] = subject_mail
    

    msg1.attach(MIMEText(message, 'plain'))

    # filename = input("Please write name of your attachment file")
    # files = input("enter file paths: ")
    # files = attachment
    filenames = attachment.split(" ")
    # print(filenames)
    # print(msg)
    for file in filenames:
        print(file)
        attachment = open(file, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
    #C:\Users\DELL\OneDrive\Desktop\MailBox_Automation\attachfile.jfif
        fileName = os.path.basename(file)
        p.add_header('content-Disposition', f'attachment; filename = {fileName}')
        msg1.attach(p)



    text = msg1.as_string()
    server.sendmail(sender_gmail,receiver_gmail,text)
    print("mail sent successfully")

    return "mail sent successfully"

# d = {
#     "sender_email": "rajkamalgomladu27@gmail.com",
#     "sender_password": "jaheevrgfdgichku",
#     "receiver_email": "rajgomladu27@gmail.com",
#     "subject_mail": "hello ",
#     "message_body": "hello message",
#     "attachement_path": []
# }

# send_email(d)

# while giving input of files : file paths should be space separated without ""