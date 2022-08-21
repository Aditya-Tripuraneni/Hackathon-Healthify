from datetime import datetime, timedelta
import os
from turtle import clear
from twilio.rest import Client

def send_sms(number, appointmentDate, reminder_type):
    # create a Twilio client
    account_sid = "AC9fe0ec3c146fd177aea7f56574972655"
    auth_token = "d60f770a96186f1818286222456fb1b4"
    client = Client(account_sid, auth_token)

    # schedule message to be sent 61 minutes after current time
    send_when =  ((appointmentDate + timedelta(hours=4))) + timedelta(minutes=16)
    print(send_when)
    # send_when = datetime.utcnow() + timedelta(minutes=16)

    # send the SMS
    messaging_service_sid = "MGeebb5010283a9b09cb887fce7e513288"
    message = client.messages.create(
        from_=messaging_service_sid,
        to='+1'+number,  # ← your phone number here
        body='Friendly reminder that you have a ' + reminder_type + " on " + str(appointmentDate),
        schedule_type='fixed',
        send_at=send_when.isoformat() + 'Z',
    )
    print(message.sid)
    # # print(datetime.utcnow())
    # print(number, appointmentDate, reminder_type)