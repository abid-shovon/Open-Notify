import smtplib
from email.mime.text import MIMEText
from datetime import datetime

sender_email = "abidshovon945@gmail.com"
receiver_email = "shovonhasan333@gmail.com"
password = "---- ---- ---- ----"    # Use 16 digit gmail app password. Ex: "zskc yvlo uevj tafm"

now = datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

subject = "Laptop Alert: Shovon someone is open your laptop."
body = f"Your laptop is open now.\nTime: {time_str}"

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
