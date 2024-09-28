import smtplib
from bots.mongodbhelper import get_single_document


def send():
    try:
        x = smtplib.SMTP('smtp.gmail.com', 587)
        x.starttls()
        config_data=get_single_document("config",{"name":"email_config"},{"username":1, "password":1,"_id":0})
        print(config_data)
        x.login(config_data['username'],config_data['password'])
        subject="Testing"
        TEXT="My name is jd"
        message = 'Subject: {}\n\n{}'.format(subject, TEXT)
        x.sendmail("sender", "receiver", message)
        print("Success")

    except Exception as exception:
        print(exception)
        print("Failure")

if __name__ == '__main__':
    send()