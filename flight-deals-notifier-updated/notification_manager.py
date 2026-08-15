import os

import smtplib

import requests

from dotenv import load_dotenv

load_dotenv()

APP_PASSWORD = os.environ.get('APP_PASSWORD')

EMAIL = os.environ.get('EMAIL_ADDRESS')


class NotificationManager:

    def __init__(self):

        pass

    def send_sms(self, message):

        """Prints or sends SMS alert for found flight deal."""

        print(f"\n📱 ALERT TRIGGERED:\n{message}")

    def send_email(self , email , message): 

        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

            connection.starttls()

            connection.login(EMAIL , APP_PASSWORD)

            email_message = f"Subject: Flight Deal Alert!\n\n{message}"

            connection.sendmail(EMAIL , email , email_message)
