import uuid
import time

import chromadb
client = chromadb.Client(chromadb.config.Settings(
	chroma_db_impl='duckdb+parquet',
	persist_directory='chromadb',
))

memoryCol = None

def createMemoryCollection():
	global memoryCol
	try:
		memoryCol = client.get_collection('memory')
	except ValueError as e:
		print('memory collection not found, creating')
		memoryCol = client.create_collection('memory')
		addMemory('this is my first memory')

def addMemory(text):
	memoryCol.add(
		documents = [text],
		metadatas = [{'time': int(time.time())}],
		ids = [str(uuid.uuid4())],
	)

def searchMemories(text, returnCount, maxDist = 999):
	results = memoryCol.query(
		query_texts = [text],
		n_results =  min(returnCount, memoryCol.count()),
	)

	returnMemories = []

	for at, memory in enumerate(results['documents'][0][:returnCount]):
		if at > returnCount:
			break
		if results['distances'][0][at] > maxDist:
			break
		memory = {'text': memory, 'dist': results['distances'][0][at], 'time': results['metadatas'][0][at]['time']}
		returnMemories.append(memory)

	return returnMemories

createMemoryCollection()
