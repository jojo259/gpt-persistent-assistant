import json
import time
import re
import openairequester
import importlib
import traceback
import config
import systemmessages
import chat
import database
import util

chat.addSystemMessage(systemmessages.initial)

while True: # main loop

	while True: # loop to force correct response format

		assistantResponse = openairequester.doRequest(chat.getMessages(), config.openAiGptModelAdvanced)
		chat.addAssistantMessage(assistantResponse)

		try:
			respJson = json.loads(assistantResponse)
			if sorted(respJson.keys()) == sorted(['task', 'payload']):
				break
			else:
				chat.addSystemMessage('Assistant did not respond with the correct JSON fields: "task" and "payload". You (assistant) must respond only with a correctly formatted JSON e.g. {"task":"input","payload":"Hello."}')
		except json.JSONDecodeError as e:
			print(f'{config.colorError}JSON Decode Error, attempting to fix JSON: {assistantResponse}')

			foundJson = re.search(r'\{(.|\n)*\}', assistantResponse)
			if foundJson:
				print(f'{config.colorError}Fixed JSON')
				try:
					respJson = json.loads(foundJson.group())
					break
				except json.JSONDecodeError as e:
					pass

			print(f'{config.colorError}Could not fix JSON')
			chat.addSystemMessage('There was an error decoding the JSON response. You (assistant) must respond only with a correctly formatted JSON e.g. {"task":"input","payload":"Hello."}')

	# print task and payload (if not input task)

	print(f'{config.colorInfo}Task: {respJson["task"]}')
	if respJson['task'] != 'input':
		print(f'{config.colorInfo}Payload: {respJson["payload"]}')

	# execute task

	try:
		taskModule = importlib.import_module(f'tasks.{respJson["task"]}')
		taskModule.run(respJson['payload'])
	except Exception as e:
		stackTraceStr = traceback.format_exc()
		chat.addSystemMessage(stackTraceStr)

	# evaluate

	chat.addSystemMessage(systemmessages.evaluate)

	while True:
		assistantResponse = openairequester.doRequest(chat.getMessages(), config.openAiGptModelFast)
		chat.addAssistantMessage(assistantResponse)
		if assistantResponse.startswith('CURRENT GOAL:') and 'TASK EVALUATION:' in assistantResponse and 'NEXT ACTIONS:' in assistantResponse and 'REASONING:' in assistantResponse:
			print(f'{config.colorAssistant}{assistantResponse}')
			break
		else:
			print(f'{config.colorError}Wrong evaluation format: {assistantResponse}')
			chat.addSystemMessage(f'{config.colorError}Wrong evaluation response format.')

	# summarize interaction

	chat.addSystemMessage(systemmessages.summarize)

	assistantResponse = openairequester.doRequest(chat.getMessages(), config.openAiGptModelFast)
	chat.addAssistantMessage(assistantResponse)
	database.addMemory(assistantResponse)
	print(f'{config.colorInfo}Summarization: {assistantResponse}')

	# get relevant memories

	chat.addSystemMessage(util.getMemories(assistantResponse))

	continue
