import chat
import requests
from bs4 import BeautifulSoup
import util

taskDesc = 'Requests the URL in the "payload" from the Internet.'

def run(payload):
	respGot = requests.get(payload, timeout = 10)
	respSoup = BeautifulSoup(respGot.content, 'html.parser')
	respText = respSoup.get_text()
	while len(respText) > 1000:
		respText = util.summarizeText(respText)
	chat.addSystemMessage('Text on URL (summarized if over 1000 chars):' + respText)
