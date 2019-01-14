import smtplib
import praw
import requests
import os
import shutil
import random
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

username = os.environ.get('REDDIT_USERNAME')
id = os.environ.get('REDDIT_CLIENT_ID')
secret = os.environ.get('REDDIT_CLIENT_SECRET')
password = os.environ.get('REDDIT_PASSWORD')
my_number = os.environ.get('MY_NUMBER')
her_number = os.environ.get('HER_NUMBER')
email = os.environ.get('MY_EMAIL')
email_password = os.environ.get('GMAIL_PASSWORD')


def random_subreddit():
    subs = ['aww', 'Eyebleach', 'MEOW_IRL', 'teefies', 'floof', 'corgis',
            'tuckedinkitties', 'incorgnito', 'Daww', 'catsonglass', 'blep',
            'catbellies', 'pimpcats', 'Delighfullychubby', 'aww', 'floof',
            'cats', 'Awwducational', 'hardcoreaww', 'kittens', 'CatsInSinks',
            'stolendogbeds', 'Sleepinganimals']
    return random.choice(subs)


def get_image(sub):
    file_type = 'png'
    reddit = praw.Reddit(client_id=id,
                         client_secret=secret,
                         password=password,
                         user_agent='testscript by me',
                         username=username)

    submission = reddit.subreddit(sub).search(query='site:i.imgur.com',
                                              sort='top', time_filter='day',
                                              limit=20)

    for result in submission:
        file_type = result.url.split('.')[-1]
        title = result.title
        if file_type not in 'gifv':
            response = requests.get(result.url, stream=True)

            with open('img.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            break

    return title


def create_message(title):
    img_data = open('img.png', 'rb').read()
    msg = MIMEMultipart()
    image = MIMEImage(img_data, _subtype='png')
    msg.attach(image)
    if(title):
        msg.attach(MIMEText(title))

    return msg


def send_message(msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, email_password)
    server.sendmail(email, my_number, msg.as_string())
    server.sendmail(email, her_number, msg.as_string())
    server.quit()


sub = random_subreddit()
image_type = get_image(sub)
message = create_message(image_type)
send_message(message)
