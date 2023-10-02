##################### Extra Hard Starting Project ######################

import pandas as pd
import smtplib
import random
import datetime as dt

# 1. Update the birthdays.csv
#filled it manually

# 2. Check if today matches a birthday in the birthdays.csv

my_email = "haran.hariharanj@gmail.com"
password = "nvrm lmby aexo bvqn"

today = (dt.datetime.now().month,dt.datetime.now().day)
file = pd.read_csv("Day32/Automated birthday sender project/birthday-wisher-extrahard-start/birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in file.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter_num = random.randint(1,3)
    with open(f"Day32/Automated birthday sender project/birthday-wisher-extrahard-start/letter_templates/letter_{letter_num}.txt") as letter:
        content = letter.read()
        new_letter = content.replace("[NAME]",birthday_person['name'])   
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],msg=f"Subject:Happy birthday {birthday_person['name']}\n\n{new_letter}")    



