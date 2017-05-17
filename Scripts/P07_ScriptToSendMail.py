# Author: OMKAR PATHAK

import smtplib

fadd = ''                                       # sender's email address
tadd = ''                                       # receiver's email address
msg = 'Mail sent through Python!'               # Message to be sent!
username = ''                                   # Your username(email ID)
password = ''                                   # Your password for above email ID
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,msg)
