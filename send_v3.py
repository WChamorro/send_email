import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_address = 'comisionsg.fiee@epn.edu.ec'
#sender_pass = 'ajpqrorhotliqhcy'
sender_pass = 'Acreditar2018*'
receiver_address = ''

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Encuesta a Graduados'   

textfile = open("text.txt", "r")
content = textfile.readlines()
email_text='-'.join(content)

message.attach(MIMEText(email_text, 'plain'))
text = message.as_string()

session = smtplib.SMTP('smtp.office365.com', 587)
session.starttls()
session.login(sender_address, sender_pass)

email_file = open("emails.csv","r")
data = list(csv.reader(email_file, delimiter=","))
for i in data:
  mail = str(i[0])
  print("send email to: "+ mail)
  message['To'] = mail
  receiver_address = mail
  session.sendmail(sender_address, receiver_address, text)


session.quit()
textfile.close()
email_file.close()
print('Mail Sent')
