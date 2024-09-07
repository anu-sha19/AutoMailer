import smtplib
import datetime as dt
import random

my_email = "learnPythonin100@gmail.com"
password = "jfyx jqtv qdmh zgkt"

#take today's date and time
now = dt.datetime.now()
day = now.weekday()

#change the text file into a list
with open("quotes.txt") as file:
    file = file.readlines()
    random_quote = random.choice(file)

    if day == 2:
        # Build and secure the connection
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # securing connection to email sever

            # Login and write the sender and receiver credentials
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="learnPythonin100@yahoo.com",
                                msg=f"Subject:Tuesday Motivation\n\n{random_quote}\nyou are a beautiful being. You are cheerful, kind, hardworking and disciplined.You are a world renowned Computer Scientist!")
