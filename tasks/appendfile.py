import config
import chat

taskDesc = 'Appends text to a file. The payload should be formatted as <filepath>;<text>.'

def run(payload):
	with open(payload.split(';')[0], 'a', encoding = 'utf-8') as file:
		file.write(';'.join(payload.split(';')[1:]))
		chat.addSystemMessage(f'Appended to file.')
