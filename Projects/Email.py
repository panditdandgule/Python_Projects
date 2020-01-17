import smtplib

#create SMTP session
s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

#Authentication
s.login("panditdandgule777@gmail.com","password9623639868")

#message to be sent
message="Message_you_need_to_send"

#sending the mail
s.sendmail("panditdandgule777@gmail.com","dandgulepandit@gmail.com",message)

#Terminating the session
s.quit()
'''

import smtplib

## email sending function
def email_sender(input_message, email_to, client):
    # function to send email 
    to = 'dandgulepandit@gmail.com'
    gmail_user = 'panditdandgule777@gmail.com' ## email of sender account
    gmail_pwd = 'password9623639868' ## password of sender account
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' +'Subject:site down! \n'
    input_message = input_message + client
    msg = header + input_message
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
'''
