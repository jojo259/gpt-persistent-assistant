import datetime
import database
import config
import openairequester

def getTimestamp(fromTime):
	return datetime.datetime.fromtimestamp(fromTime).strftime('%Y-%m-%d %H:%M:%S')

def getMemories(searchStr):
	memoriesStr = 'Relevant memories:\n'
	recalledMemories = database.searchMemories(searchStr, 16, 2)
	for memory in recalledMemories:
		timeStr = getTimestamp(memory['time'])
		memoryStr = memory['text']
		memoriesStr += f'{timeStr} — {memoryStr}\n'
	memoriesStr = memoriesStr[:-1]
	return memoriesStr

def summarizeText(text):
	while len(text) > 1000:
		summaryText = ''
		summaryParts = int(len(text) / 1000) + 1
		for i in range(summaryParts):
			summarizeConversation = []
			summarizeConversation.append(openairequester.constructMessage('system', 'You must summarize the user\'s text concisely. Do not include any special formatting.'))
			summarizeConversation.append(openairequester.constructMessage('user', text[i * 1000:i* 1000 + 1000]))
			summary = openairequester.doRequest(summarizeConversation, config.openAiGptModelFast)
			summaryText += summary + '\n'
			print(f'{config.colorInfo}Summarized part {i + 1}/{summaryParts + 1}: {summary}')
		text = summaryText
	return text
