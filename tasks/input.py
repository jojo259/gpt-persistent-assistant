import chat
import config

taskDesc = 'Takes input from the user. The payload is outputted to the user. This is the only task that the user can see the output of.'

def run(payload):
	print(config.colorAssistant + payload)
	userMessage = input(config.colorUser + '> ')
	chat.addUserMessage(userMessage)
