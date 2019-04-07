# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACad92a5094df25b847bb064650e650ad2'
auth_token = '516a23ce73cd5b9b68e58435836d0c73'
client = Client(account_sid, auth_token)

def send_message(recipients, message = "Thank you for signing up for our app!"):
    '''Sends the message to the recipient number(s), returns the sid'''
    message = client.messages.create(
                     body = message,
                     from_ ='+16507419499',
                     to = recipients)

    return(message.sid)

def validate_number(number):
    '''validates the given number with the given name, returns a validation code.
    The user will receive a phone call and will be prompted for this code.'''
    validation_request = client.validation_requests.create(
                                phone_number= number)

    # Can only verify 2 numbers every 72 hours :(
    # https://www.twilio.com/docs/errors/10002

    # TODO::Add a StatusCallbackURL so we can verify if it was successful
    # https://www.twilio.com/docs/voice/api/outgoing-caller-ids#statuscallback-parameter

    return(validation_request.validation_code)

print(send_message('+14082203759'))
