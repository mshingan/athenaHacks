# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACad92a5094df25b847bb064650e650ad2'
auth_token = '516a23ce73cd5b9b68e58435836d0c73'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16507419499',
                     to='+14082203759'
                 )

print(message.sid)
