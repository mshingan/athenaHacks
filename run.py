# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio_kit import send_alert, create_connection

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
	"""Send a dynamic reply to an incoming text message"""
	# Get the message the user sent our Twilio number
	bdy = request.values.get('Body', None)
	number = request.values.get('From',None)
	print(bdy)
	print(number)
	# Start our TwiML response
	resp = MessagingResponse()
	conn = create_connection("db.sqlite3")
	with conn:
		send_alert(conn, body)

	# Determine the right reply for this message
#	if bdy == 'hello':
#		resp.message("Hi!")
#	elif bdy == 'bye':
#		resp.message("Goodbye")
	resp.message("We recieved your message, and will send it out to people in the area")


	return str(resp)


'''
def sms_ahoy_reply():
	"""Respond to incoming messages with a friendly SMS."""
	# Start our response
	resp = MessagingResponse()

	# Add a message
	resp.message("Ahoy! Thanks so much for your message.")


	return str(resp)

'''

phone = row[0].encode('ascii')
if __name__ == "__main__":
	app.run(debug=True)
