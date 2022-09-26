import pandas as pd 
import smtplib
from email.mime.text import MIMEText 
import os 

os.chdir('/Users/wilhigh/Downloads/RPA를 이용한 업무자동화/UiPath')
contact = pd.read_csv('contact.csv')
recipients = contact.email.values 

host =  'smtp.naver.com'
port = 587 
email = 'hobbangpai@naver.com'
pwd = 'password' #if there is wrong password, Error: unable to send email.

for i in range(len(recipients)):
    text = "안녕하세요?"
    msg = MIMEText(text.encode('utf-8'),_charset='UTF-8')
    msg['Subject']="hello " + str(contact.first_name[i])
    msg['From']=email
    msg['To']=recipients[i]

#SMTP서버를 이용해 메일 보내기

    try:
        s = smtplib.SMTP(host, port)
        s.starttls()
        s.login(email, pwd)
        s.sendmail(email, recipients[i], msg.as_string())
        print('Successfully sent email!')
    except Exception:
        print('Error: unable to send email.')
    finally:
        s.close()