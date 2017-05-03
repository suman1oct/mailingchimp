from django.core.mail import EmailMessage

class EmailMessaging(EmailMessage):

    def send(self):
        result = super(EmailMessaging, self).send()
        if(result):
            print('success')
        else:
            print('fail') 
