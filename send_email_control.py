import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_address = 'comisionsg.fiee@epn.edu.ec'
sender_pass = 'Acreditar2018*'
receiver_address = ''
text_file = "text_control.txt"
emails_list = "base_automatizacion.csv"

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Encuesta a Graduados'   

textfile = open(text_file, "r",encoding='utf-8')
content = textfile.readlines()
email_text=' '.join(content)

message.attach(MIMEText(email_text, 'plain'))
text = message.as_string()

session = smtplib.SMTP('smtp.office365.com', 587)
session.starttls()
session.login(sender_address, sender_pass)

email_file = open(emails_list,"r")
data = list(csv.reader(email_file, delimiter=","))
j=1
for i in data:
  try:
    mail = str(i[0])
    message['To'] = mail
    receiver_address = mail
    session.sendmail(sender_address, receiver_address, text)
    print(str(j)+": send email to: "+ mail)
    j=j+1
    print('Mail Sent')
  except Exception as e:
    print(e) 
    print('Mail was NOT Sent')

session.quit()
textfile.close()
email_file.close()

