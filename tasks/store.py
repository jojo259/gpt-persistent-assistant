import chat
import database

taskDesc = 'Stores a memory in your memory database (the payload is the plaintext memory that will be stored). The memory will have the time stored as metadata so you only need to provide relative time information. Each memory should be very short.'

def run(payload):
	database.addMemory(payload)
	chat.addSystemMessage('Memory stored successfully.')
