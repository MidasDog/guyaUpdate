from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import ssl
import smtplib
import requests
import time

num = 252
sender_email = "nthngregorius50@gmail.com"
receiver_email = "nathangregorius50@gmail.com"
my_secret = "minecartofgt"

context = ssl.create_default_context()

base_link = "https://guya.moe/read/manga/Kaguya-Wants-To-Be-Confessed-To/"

def linkMaker() :
  global url
  url = base_link + str(num) + "/1/"


def findUpdate() :
  requests.head(url)

linkMaker()
while 1 :
  try :
      r = requests.head(url)
      answer = r.status_code
      if answer == 200 :
        print("success")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls(context=context)
        s.login(sender_email, my_secret)
        html = MIMEText(u'<a href="%s">New chapter is out!</a>' % url, 'html')
        msg = MIMEMultipart("alternative")
        msg['from'] = sender_email
        msg["to"] = receiver_email
        msg["Subject"] = "Kaguya-Sama Update!"
        msg.attach(html)
        s.sendmail(sender_email, receiver_email, msg.as_string())
        print("sent")
        time.sleep(14400)
        num += 1
        linkMaker()
        print(url)
        continue

  except requests.ConnectionError :
      time.sleep(86400)
      continue