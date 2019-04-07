# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from django.db import models 
import sqlite3
from sqlite3 import Error


clientList = ['+14082203759'] 
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACad92a5094df25b847bb064650e650ad2'
auth_token = '516a23ce73cd5b9b68e58435836d0c73'
client = Client(account_sid, auth_token)

def send_message(recipient, message = "Thank you for signing up for our app!"):
	'''Sends the message to the recipient number(s), returns the sid'''
	
	message = client.messages.create(
					 body = message,
					 from_ ='+16507419499',
					 to = recipient)

#	print(message.body)
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

def create_connection(db):
	try:
		conn = sqlite3.connect(db)
		return conn
	except Error as e:
		print(e)

	return None


def get_recipients(conn):
	cur = conn.cursor()
#	cur.execute("ALTER TABLE blog_blog RENAME COLUMN title TO email")
#	cur.execute("ALTER TABLE blog_blog ADD zipcode")
	cur.execute("ALTER TABLE blog_blog ADD phoneNumber")
	cur.execute("SELECT email FROM blog_blog")
	rows = cur.fetchall()
	for row in rows:
		print(row)

def go_through_clients(recipients):
	for i in recipients: 
		send_message(i) 

#conn = create_connection("db.sqlite3")
#with conn:
#	print(get_recipients(conn))
go_through_clients(clientList)
#print(go_through_clients(['+14082203759']))
