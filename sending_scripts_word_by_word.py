from twilio.rest import Client

account_sid = ''
auth_token = ''

sender =''
receiver = ''

client = Client(account_sid, auth_token)

with open("script.txt","r") as f:
	for lines in f:
		for word in lines.split():
			message = client.messages.create(
				body = word,
				from_=sender,
				to = receiver)
 