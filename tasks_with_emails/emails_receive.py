import imaplib
import getpass
import email

username = getpass.getpass('Please enter your email')
password = getpass.getpass('Please enter your password')


def receive_email(username, password):
    M = imaplib.IMAP4_SSL('imap.gmail.com')
    M.login(username, password)
    print(M.list())
    M.select('INBOX')
    typ, data = M.search(None, 'SUBJECT "TEST email subject"')
    print(typ, data)
    for num in data[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        print('Message %s\n%s\n' % (num, data[0][1]))
        raw_email_string = data[0][1].decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for part in email_message.walk():
            if part.get_content_type == 'text/plain':
                body = part.get_payload(decode=True)
                print(body)
    M.close()
    M.logout()


receive_email(username, password)
