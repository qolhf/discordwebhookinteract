import requests
print("Discord Webhook Interactor!")
print()
print("This tool allows you to interact with the Discord Webhook Tool!")
print("I will add updates to this tool soon, but for now, enjoy this!")
print()
username = input("Enter Username To Send From: ")
message = input("Enter Message To Send: ")
webhook = input("Enter Discord Webhook: ")
send = requests.post('{}'.format(webhook), {
'username': username,
'content': message,
})
if send.status_code == 204:
	print("Message Sent!")
else:
	print("Message Failed!")
