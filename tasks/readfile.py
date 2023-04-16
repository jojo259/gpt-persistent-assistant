import config
import chat

taskDesc = 'Reads the contents of a file with the payload as the file path.'

def run(payload):
	with open(payload, 'r', encoding = 'utf-8') as file:
		chat.addSystemMessage(f'File contents: {file.read()}')
