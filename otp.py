import boto3
import pyotp as pyotp
import time
import datetime
from customer import Customers


class OtpInterface:
    def __init__(self):
        # Create empty pyotp object
        self.totp = pyotp.TOTP(pyotp.random_base32(), interval = 300)

    # Returns the pyotp object
    def getObj(self):
        return self.totp

    # Function to create pyotp object with an otp changing every 5 minutes. Sends the first OTP to the input phone number using AWS SNS service.
    def send_otp(self, phone):
        # Append country code to phone number
        phone = "+1" + phone

        # Create seeded pyotp object
        # self.totp = pyotp.TOTP(pyotp.random_base32(), interval = 300)
        
        # Create SNS client
        client = boto3.client(
            "sns",
            aws_access_key_id="AKIAYO35KQMIIX4E5MNG",
            aws_secret_access_key="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",
            region_name="us-east-1"
        )
        # Send SMS with current generated OTP
        client.publish(
            PhoneNumber=phone,
            Message=str(self.totp.now())
        )
        return 'OTP Sent'

    # Function to verify an OTP
    def verify_otp(self, otp):
        if self.totp is not None:
            if(self.totp.verify(otp)):
                self.totp = None
                return 'verified'
            else:
                return 'OTP not verified'
        else:
            return 'Must send OTP first before verification'