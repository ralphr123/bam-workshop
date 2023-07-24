# Load environment variables from .env
from dotenv import load_dotenv; load_dotenv()

# Fetch environment variables from .env
import os

# Typings are good practice to know what your code is producing
from typing import List

# OpenAI Python SDK to allow us to make requests to GPT
import openai

# Store OpenAI environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Use this function to print to the console for debugging
def printToConsole(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end, flush=True)

# ===========================
# === MODIFY THIS SECTION ===
# ===========================

class Chat:
	def __init__(self, system_msg: str = None):
		self.messages = []

		if (system_msg):
			self.addSystemMessage(system_msg)

	# Add a message of role "system" to the self.messages array
	def addSystemMessage(self, message: str) -> None:
		self.messages.append({'role': 'system', 'content': message})

	# Add a message of role "user" to the self.messages array
	def addUserMessasge(self, message: str) -> None:
		self.messages.append({'role': 'user', 'content': message})

	# Add a message of role "assistant" to the self.messages array
	def addAIMessasge(self, message: str) -> None:
		self.messages.append({'role': 'assistant', 'content': message})

	# Send a message to GPT and return the response string
	def sendMessage(self, message: str) -> str:
		# 1. Use the function you wrote to add the message to the array as a user message
		self.addUserMessasge(message)

		# 2. Call Azure to send the message to GPT
		res = openai.ChatCompletion.create(
			model='gpt-3.5-turbo-16k',
			messages=self.messages,
			temperature=0
		)

		message = res['choices'][0]['message']['content']
		
		# 3. Add the response string to the array as an AI message
		self.addAIMessasge(message)

		# 4. Return the response string
		return message
	
	# Get all non-system messages from array
	def getChatMessages(self) -> List:
		# Feel free you use any method you'd like to filter out the system message
		# Ex. loop, python filter function, subarrays, etc.
		
		chatMessages = []

		for message in self.messages:
			if message['role'] != 'system':
				chatMessages.append(message)
		
		return chatMessages

