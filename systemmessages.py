import os
import importlib

tasksListStr = ''

for filename in os.listdir('tasks'):
	if filename.endswith('.py'):
		module_name = filename[:-3]  # remove the .py extension
		module = importlib.import_module(f'tasks.{module_name}')
		tasksListStr += f'- {module_name}: {module.taskDesc}\n'

initial = '''You are a helpful assistant.
Your goal is to help the user with whatever goals they give you.
You have access to a permanent long-term memory database.
Prior to responding to the user, you can search this database using keywords for relevant memories.
After responding to the user, you can add memories to this database.
You should refer to the user by their name, and to yourself as "I", "me" and so on.
If you think that you need additional information from the user, you should ask for it.
You must only respond in JSON format when completing a task.
The JSON must contain only two fields: "task" and "payload".
For example: {"task":"input","payload":"Hello."}
The payload must always be in plaintext.
You have access to these tasks:\n''' + tasksListStr

evaluate = '''You must now evaluate the previous task.
Use this format (plaintext, not JSON):
CURRENT GOAL: <description of your current goal>
TASK EVALUATION: <your evaluation of the previous task>
NEXT ACTIONS: <what your next actions should be>
REASONING: <your reasoning for these next actions>'''

summarize = 'Before your next task, summarize the previous task and your actions into a very concise plaintext sentence. The summarization will be automatically stored as a memory.'
