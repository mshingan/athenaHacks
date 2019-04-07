# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio_kit import send_alert, create_connection, go_through_clients

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
	"""Send a dynamic reply to an incoming text message"""
	# Get the message the user sent our Twilio number
	body = request.values.get('Body', None)
	number = request.values.get('From',None)
	summary = '''
	from: {}\n
	message: {}'''.format(number, body)

	# Start our TwiML response
	resp = MessagingResponse()

	if body is None:
		resp.message("We have not received your message, try again?")
		return summary

	resp.message("We recieved your message, and will send it out to people in the area")

	conn = create_connection("db.sqlite3")
	if conn is None:
		summary = "ERROR UNABLE TO CONNECT TO DB!!!"
	else:
		with conn:
			go_through_clients(body)
			#send_alert(conn, number, message)

	return summary


'''
def sms_ahoy_reply():
	"""Respond to incoming messages with a friendly SMS."""
	# Start our response
	resp = MessagingResponse()

	# Add a message
	resp.message("Ahoy! Thanks so much for your message.")


	return str(resp)

'''
if __name__ == "__main__":
	app.run(debug=True)
