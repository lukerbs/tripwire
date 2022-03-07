# Test twilio to sms
from twilio.rest import Client

account_sid = "AC3bf727d99cb53f9942d00a30d50d4f54"
auth_token  = "5ff7f66c4ea4a02bfcf5b98eab0fa81b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14087064249", 
    from_="+19378639987",
    body="Motion Detected!")

print(message.sid)
