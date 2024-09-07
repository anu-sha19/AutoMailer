##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "scubidoo@gmail.com"
password = "jfyx jqtv qdmh zgkt"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
#take today's date and time
now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
#retrieve a row from month and day
birthday_dict = {(rows.month, rows.day): rows for (index, rows) in data.iterrows()}


#check if the month and day matches
if today_tuple in birthday_dict:
    name = birthday_dict[today_tuple]["name"]

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter_choice = file.read()
        final_letter = letter_choice.replace("[NAME]", name)

    # 4. Send the letter generated in step 3 to that person's email address.
    #establish a connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  #securing connection to email server

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="miathermopolis@yahoo.com",
                            msg=f"Subject:Happy Birthday\n\n{final_letter}")
