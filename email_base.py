import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import config

def send_mail(message,receivers=config['smtp_receivers']):
    """
        Module that sends emails. 
        Message should be a dictionary containing the following keys:
            subject -> Subject of the email
            text -> The plain text part of the email
        uses options from config.py
    """
    sender = config['smtp_sender']
    print sender
    print receivers
    print message
    try:
        smtpObj = smtplib.SMTP_SSL(config['smtp_server'],config['smtp_port'])
        smtpObj.login(config['smtp_login'],config['smtp_password'])
        if not receivers:
            return True
        smtpObj.sendmail(sender, receivers, message)
        smtpObj.quit()
        return True 
    except Exception, exc:
         print >> sys.stderr, "Exception From email_base"
         print >> sys.stderr, exc 
         return False
if __name__ == '__main__':
    send_mail('Test message')
