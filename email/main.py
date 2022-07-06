import smtplib


with smtplib.SMTP("smtp.gmail.com") as connection:
   connection.starttls()
   connection.login(user="username", password="123456")
   connection.sendmail(from_addr="alihser@yahoo.com", to_addrs="alisherkabil@gmail.com", msg="Say hello")
   connection.close()

