import config
import chat
import io
import importlib

taskDesc = 'Executes the provided payload as Python code. You will receive the code\'s print() output. You must use importlib to import inside the exec function.'

def run(payload):
	print(f'{config.colorAssistant}Executing the following code:\n{payload}')
	execPermission = input(f'{config.colorInfo}Enter "y" to execute the code\n{config.colorUser}> ')
	if execPermission != 'y':
		print(f'{config.colorAssistant}Execution cancelled.')
		return
	outputBuffer = io.StringIO()
	exec(payload, globals(), {'print': lambda x: print(x, file = outputBuffer)})
	execOutput = outputBuffer.getvalue()
	chat.addSystemMessage(f'Executed payload. Output:\n{execOutput}')
