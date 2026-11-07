import smtplib
from email.message import EmailMessage

email = EmailMessage()

email["from"] = "python <ahmedmotinho10@gmail.com"
email["to"] = "qardhaas2021@gmail.com"
email["subject"] = "congratulation on your first email"

email.set_content("I write and send this email from python")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()

    smtp.starttls()
    smtp.ehlo()
    smtp.login("ahmedmotinho10@gmail.com", "sxva bvcy pfve mfsr")
    smtp.send_message(email)
    print("the email is sent")
