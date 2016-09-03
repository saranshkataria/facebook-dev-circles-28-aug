# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 09:07:34 2016

@author: pratikgujral
"""

# Sends email
import smtplib

def send_email(list_of_recipients, sender_name, sender_email, sender_password, email_subject, html_template):
    """ Sends email to the list_of_recipients. 
Every element of list_of_recipients is a tuple (name, email-id) pair

For example: 

>>> list_of_recipients = [('Pratik Gujral', 'pratikgujral@gmail.com')]

>>> body_html = "<html><head><title>Title Here</title></head><body><h1>Heading1</h1><p>This is a paragraph</p></body></html>"

>>> send_email(list_of_recipients, 'Pratik Gujral', 'pratikgujral@gmail.com', '**PASSWORD_HERE**', 'TestSubject', body_html)      
    
    """
    
    for recipient in list_of_recipients:
        message = """FROM: %s
TO: %s
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s
""" %(sender_name, recipient[0], email_subject, html_template)
        #print "\n\n\n", message
        
        try:
            server = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
            server.ehlo()
            server.starttls()
            server.login(user = sender_email, password = sender_password)
            server.sendmail(sender_email, recipient[1], message)
            server.close()
        except Exception, e:
            print "Exception occurred:", e