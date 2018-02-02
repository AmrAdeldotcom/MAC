from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8c6ca6ddb7168a16a20e10029dd09b4f"
# Your Auth Token from twilio.com/console
auth_token  = "9905ea9c49249995718a144b4ea0d16b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+201222121231",
    from_="+12023350747",
    body="Hello from Python!")

print(message.sid)
