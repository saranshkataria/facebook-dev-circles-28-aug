import smtplib
from config import EMAIL_ID, PASSWORD, FROM, SMTP_SERVER, SMTP_PORT

def is_send_email(email_dict, html_template, subject):
    TO = email_dict['email']
    SUBJECT = subject

    # Prepare actual message
    message = """From: %s\nSubject: %s\n\n%s
    """ % (FROM, SUBJECT, html_template)
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ID, PASSWORD)
        server.sendmail(FROM, TO, message)
        server.close()
        return True
    except:
        return False