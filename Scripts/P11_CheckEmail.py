# Author: OMKAR PATHAK

# This script helps to read the latest emails and entieve the contents of the selected email
# First turn on this: https://myaccount.google.com/lesssecureapps?pli=1

import email, getpass, imaplib, os
detach_dir = '.'                # directory where to save attachments (default: current)
# user = input("Enter your Gmail Username:")
pwd = getpass.getpass("Enter your Gmail Password: ")
# connecting to the gmail imap server

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login('omkarpathak.comp@mmcoe.edu.in', pwd)
mail.list()
mail.select('INBOX') # Specify from where to retrieve the email

response, ids = mail.search(None, '(ALL)') # search all types of mails
ids = ids[0].split()
ids = ids[::-1]             # getting latest emails first

i = 0
for emailid in ids:
    i += 1
    response, data = mail.fetch(emailid, "(RFC822)") # fetching the mail
    email_body = data[0][1]                          # getting the mail content
    mailFetch = email.message_from_bytes(email_body) # parsing the mail content to get a mail object

    #Check if any attachments at all
    if mailFetch.get_content_maintype() != 'multipart':
        continue

    mailFetch['Subject'] = mailFetch['Subject'].replace(r'=?utf-8?q?', '')
    mailFetch['Subject'] = mailFetch['Subject'].replace('_', ' ')
    # print(type(mailFetch['Subject']))
    print ("["+mailFetch["From"]+"]:" + mailFetch['Subject'].replace('=?utf-8?q?', '').replace('_', ' ').replace('=3F?=', '?').replace('?=',''))

    # we use walk to create a generator so we can iterate on the parts and forget about the recursive headach
    for part in mailFetch.walk():
        # multipart are just containers, so we skip them
        if part.get_content_maintype() == 'multipart':
            continue

        # is this part an attachment ?
        if part.get('Content-Disposition') is None:
            continue

        filename = mailFetch["From"] + "_hw1answer"

        att_path = os.path.join(detach_dir, filename)

        #Check if its already there
        if not os.path.isfile(att_path) :
            # finally write the stuff
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()

    if (i == 10):       # Get only ten latest emails
        break
