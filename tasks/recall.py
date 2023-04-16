import chat
import database
import util

taskDesc = 'Searches your memory database for the keyword (the payload is the keyword).'

def run(payload):
	memoriesStr = util.getMemories(payload)
	chat.addSystemMessage(memoriesStr)
