from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5c41a268ef916654fb10ed3ed9106007"
# Your Auth Token from twilio.com/console
auth_token  = "1f317b96feba14fb74d5c00e826dfe1f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16479744206", 
    from_="+15815000484",
    body="Hello from Python!")

print(message.sid)
