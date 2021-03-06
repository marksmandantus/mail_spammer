from smtplib import SMTP
import time

while True:

    try:
        subject = "Test"
        message = "This is a test message."
        content = "Subject:{0}\n\n{1}.".format(subject,message)

        my_mail_address = "Enter your mail address"
        my_password = "Enter your password"

        send_to = "Enter the e-mail to be sent "

        mail = SMTP("smtp-mail.outlook.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login(my_mail_address,my_password)
        mail.sendmail(my_mail_address,send_to,content.encode("utf-8"))
        print("Sending e-mail successful!")

        time.sleep(1)

    except Exception as e:
        print("Something went wrong!\n{0}".format(e))
        
    except KeyboardInterrupt:
        print("Spam stopped")


