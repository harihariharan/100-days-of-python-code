#excercise 1: Just sending an email

# import smtplib

# my_email = "haran.hariharanj@gmail.com"
# password = "nvrm lmby aexo bvqn"

# with smtplib.SMTP("smtp.gmail.com") as Connection:
#     Connection.starttls()
#     Connection.login(user=my_email, password=password)
#     Connection.sendmail(from_addr=my_email, 
#                         to_addrs="harijanakiraman12@gmail.com", 
#                         msg="Subject:Hello\n\nThis is the body of my email.")

#excercise 2: Sending motivational emails on Monday via emails

import datetime as dt
import smtplib
import random

my_email = "haran.hariharanj@gmail.com"
password = "nvrm lmby aexo bvqn"

with open("Day32/Birthday Wisher (Day 32) start/quotes.txt") as file:
    data = file.readlines()
    quote = random.choice(data)
now = dt.datetime.now()    
day = now.weekday()   
if day == 5:
    with smtplib.SMTP("smtp.gmail.com") as Connection:
        Connection.starttls()
        Connection.login(user=my_email, password=password)
        Connection.sendmail(from_addr=my_email, 
                            to_addrs="harijanakiraman12@gmail.com", 
                            msg=f"Subject:Motivation\n\n{quote}")