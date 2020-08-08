from twilio.rest import Client

account_sid = 'AC51ea8c82a245c46c095d437b6ac34a68'
auth_token = 'a5fe54676723db37abbdcd19cc45720e'

sender ='+19143807864'
receiver = '+919840241351'

client = Client(account_sid, auth_token)

with open("script.txt","r") as f:
	for lines in f:
		for word in lines.split():
			message = client.messages.create(
				body = word,
				from_=sender,
				to = receiver)
 