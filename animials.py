import smtplib
import praw
import requests
import os
import shutil
import random
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


class Animials():

    def __init__(self):
        self.username = os.environ.get('REDDIT_USERNAME')
        self.id = os.environ.get('REDDIT_CLIENT_ID')
        self.secret = os.environ.get('REDDIT_CLIENT_SECRET')
        self.password = os.environ.get('REDDIT_PASSWORD')
        self.my_number = os.environ.get('MY_NUMBER')
        self.her_number = os.environ.get('HER_NUMBER')
        self.email = os.environ.get('MY_EMAIL')
        self.email_password = os.environ.get('GMAIL_PASSWORD')

    def random_subreddit(self):
        subs = ['aww', 'Eyebleach', 'MEOW_IRL', 'teefies', 'floof', 'corgis',
                'tuckedinkitties', 'incorgnito', 'Daww', 'catsonglass', 'blep',
                'catbellies', 'pimpcats', 'Delighfullychubby', 'aww', 'floof',
                'cats', 'hardcoreaww', 'kittens',
                'stolendogbeds', 'Sleepinganimals', 'CatsInSinks',
                'supermodelcats']
        return random.choice(subs)

    def get_image(self, sub):
        reddit = praw.Reddit(client_id=self.id,
                             client_secret=self.secret,
                             password=self.password,
                             user_agent='Script by me',
                             username=self.username)

        submission = reddit.subreddit(sub).search(query='site:i.imgur.com',
                                                  sort='top', time_filter='day',
                                                  limit=20)

        for result in submission:
            file_type = result.url.split('.')[-1]
            if file_type != 'gifv':
                response = requests.get(result.url, stream=True)

                with open('img.' + file_type, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
                return result

    def title(self, submission):
        return submission.title

    def file_type(self, submission):
        print(submission.url.split('.')[-1])
        return submission.url.split('.')[-1]

    def create_message(self, title, file_type):
        img_data = open('img.' + file_type, 'rb').read()
        msg = MIMEMultipart()
        image = MIMEImage(img_data, _subtype=file_type)
        msg.attach(image)
        if(title):
            msg.attach(MIMEText(title))

        return msg

    def send_message(self, msg):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.email_password)
        server.sendmail(self.email, self.my_number, msg.as_string())
        server.sendmail(self.email, self.her_number, msg.as_string())
        server.quit()

        return True
