import smtplib
from email.mime.text import MIMEText
from email.header import Header

me = 'tmd9544@gmail.com'  #보내는 사람
you = 'tmd9544@naver.com'

subject = 'testMail'
contents = '''
이건 실험으로 보내는 메일입니다
'''

msg = MIMEText(contents.encode('utf-8'),_subtype='plain',_charset='utf-8')
msg['Subject'] = Header(subject.encode('utf-8'),'utf-8')
msg['From'] = me
msg['To'] =you

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(me,'fhgkswnhatowboxx')
s.sendmail(me,[you],msg.as_string())
s.quit()