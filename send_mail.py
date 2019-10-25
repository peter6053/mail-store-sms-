import smtplip
from email.mime.text import mimetxt

def send_mail(customer,dealer,rating,comments):
    port = 25252
    smtp_server ='smtp.mailtrap.io'
    login ='	2d77a3ea070c43'
    password = 'c988e20abab831'
    message f"<h3>new feedback submission </h3>
    <ul>li>customer: {customer}</li></ul>
    <ul>li>dealer:{dealer}</li></ul>
    <ul>li>dealer:{rating}</li></ul>"

    send_email = 'peternjuguna76@gmail.com'
    receiver_email ='peternjuguna76@gmail.com'
    msg = MIMEtext()(me ssage, 'html')
    msg['subject'] ='lexus feedback'
    msg['from'] = sender_email
    msg[ 'to']  = receiver_email

    #sendmail
    with smtplib.smtp(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(send_email, receiver_email, msg.as_string())

