from datetime import datetime, timedelta
import os
from turtle import clear
from twilio.rest import Client

# create a Twilio client
account_sid = "AC9fe0ec3c146fd177aea7f56574972655"
auth_token = "a93bd4ca7d4e3a4331782b2b3885c645"
client = Client(account_sid, auth_token)

# schedule message to be sent 61 minutes after current time
send_when = datetime.utcnow() + timedelta(minutes=16)

# send the SMS
messaging_service_sid = "MGeebb5010283a9b09cb887fce7e513288"
message = client.messages.create(
    from_=messaging_service_sid,
    to='+16479881095',  # ← your phone number here
    body='Friendly reminder that you have an appointment with us next week.',
    schedule_type='fixed',
    send_at=send_when.isoformat() + 'Z',
)

# print(message.sid)