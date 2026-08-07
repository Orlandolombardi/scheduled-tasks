import os
import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
for today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL,
                            to_addrs=birthday_person.email,
                            msg=f"Subject:Happy Birthday\n\n{content}")
