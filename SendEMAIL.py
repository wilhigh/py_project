
import smtplib
from email.mime.text import MIMEText 

host =  'smtp.naver.com'
port = 587 
email = 'hobbangpai@naver.com'
pwd = 'password'

text = '안녕하세요'
msg = MIMEText(text.encode('utf-8'), _charset='UTF-8')
msg['Subject'] = 'test email'
msg['From'] = email 
recipient = 'hobbangpai@naver.com'
msg['To'] = 'hobbangpai@naver.com'

try:
    s = smtplib.SMTP(host, port)
    s.starttls()
    s.login(email, pwd)
    s.sendmail(email, recipient, msg.as_string())
    print('Successfully sent email!')
except Exception:
    print('Error: unable to send email.')
finally:
    s.close()

