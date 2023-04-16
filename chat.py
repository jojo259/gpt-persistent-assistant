import openairequester
import config
import systemmessages

curMessages = []

def getMessages():
	return [openairequester.constructMessage('system', systemmessages.initial)] + curMessages[-8:]

def addUserMessage(content):
	curMessages.append(openairequester.constructMessage('user', content))

def addAssistantMessage(content):
	curMessages.append(openairequester.constructMessage('assistant', content))

def addSystemMessage(content):
	print(config.colorSystem + content)
	curMessages.append(openairequester.constructMessage('system', content))
