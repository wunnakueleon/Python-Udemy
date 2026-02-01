##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
import pandas
import datetime as dt

# 2. Check if today matches a birthday in the birthdays.csv
birthday = dt.datetime.now()
dates_csv = pandas.read_csv("birthday-wisher-extrahard-start/birthdays.csv")
date = dates_csv[dates_csv.day == birthday.day]
print(date)
print(birthday.day)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for index, row in date.iterrows():
    name = row['name']
    email = row['email']
    print(name)
    print(email)

# 4. Send the letter generated in step 3 to that person's email address.




