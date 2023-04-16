import os
import dotenv
from colorama import Fore

dotenv.load_dotenv()

openAiKey = os.environ['openaikey']
openAiGptModelAdvanced = os.environ['openaigptmodeladvanced']
openAiGptModelFast = os.environ['openaigptmodelfast']

colorSystem = Fore.YELLOW
colorAssistant = Fore.CYAN
colorInfo = Fore.GREEN
colorError = Fore.RED
colorUser = Fore.WHITE
