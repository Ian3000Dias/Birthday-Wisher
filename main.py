import smtplib
import random
import datetime as dt


my_email = "iandias228@gmail.com"
password = "gudbwgxunzzhetfo"

with open("Birthday Wisher (Day 32) start\quotes.txt", "r") as quotes:
    data = list(quotes)

def sendmail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="iandias72@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{message}"
        )


now = dt.datetime.now()
day = now.weekday()
print(day)
if day == 0:
    message = random.choice(data)
    sendmail()
