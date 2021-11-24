#!/usr/bin/env python3

import smtplib 
import ssl
import configparser


config = configparser.ConfigParser()

def main():
    
    config.read('example.ini')
    
    SENDER_MAIL=config['emails']['send_mail']
    JRNL_MAIL=config['emails']['jrnl_mail']
    GMAIL_PASSWORD=config['secrets']['gmail_password']
    
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = SENDER_MAIL
    receiver_email = JRNL_MAIL
    password = GMAIL_PASSWORD
    
    # Message
    jrnl_entry = """\
    Subject: Hi there other me
    
    This message is sent from Python."""
    
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, jrnl_entry)

    print("Message Sent!")

    print(f"SENDER: {SENDER_MAIL} JRNL: {JRNL_MAIL}")


if __name__ == "__main__":
    exit(main())
