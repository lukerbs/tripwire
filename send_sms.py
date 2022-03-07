# Test twilio to sms
from twilio.rest import Client

account_sid = "xxxxxx"
auth_token  = "xxxxxx"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14087064249", 
    from_="+19378639987",
    body="Motion Detected!")

print(message.sid)
