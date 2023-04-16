import chat
import util

taskDesc = 'Outputs the current date and time (payload is unused).'

def run(payload):
	chat.addSystemMessage(f'The current date and time is: {util.getTimestamp(time.time())}')
