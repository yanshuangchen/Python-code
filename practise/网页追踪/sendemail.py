import smtplib
from email.mime.text import MIMEText
from email.header import Header

def email():

    HOST = "smtp.163.com"
    SUBJECT = "Test email from Python"
    TO = "669042387@qq.com"
    FROM = "13862810574@163.com"
    text = "news come!"
    BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
    ))
    server = smtplib.SMTP()
    server.connect(HOST, 25)
    server.login(FROM, "TEXBTZHUUHIHXGOS")
    server.set_debuglevel(1)
    server.sendmail(FROM, [TO], BODY)
    server.quit()