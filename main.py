##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas
my_email="abc@gmail.com"
password="need to change google settings"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now=dt.datetime.now()
data=pandas.read_csv("birthdays.csv")
today=(now.month,now.day)

birth_dict={(datarow["month"],datarow["day"]):datarow for(index,datarow) in data.iterrows()}

if today in birth_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    birth_person=birth_dict[today]
    num=random.randint(1,3)
    with open(f"letter_templates/letter_{num}.txt") as file:
        letter=file.read()
        letter=letter.replace("[NAME]" ,birth_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birth_person["email"],
                            msg=f"Subject:Birthday\n\n{letter}")


