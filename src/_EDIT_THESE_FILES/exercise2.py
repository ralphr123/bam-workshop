# Load environment variables from .env
from dotenv import load_dotenv; load_dotenv()

# Fetch environment variables from .env
import os

# OpenAI Python SDK to allow us to make requests to GPT
import openai

# Use this function to print to the console for debugging
def printToConsole(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end, flush=True)

# ===========================
# === MODIFY THIS SECTION ===
# ===========================

class Chat:
	def __init__(self):
		self.messages = []

	# Add a message of role "user" to the self.messages array
	def addUserMessasge(self, message: str) -> None:
		self.messages.append({'role': 'user', 'content': message})

	# Add a message of role "assistant" to the self.messages array
	def addAIMessasge(self, message: str) -> None:
		self.messages.append({'role': 'assistant', 'content': message})

	# Send a message to GPT and return the response string
	def sendMessage(self, message: str) -> str:
		# 1. Use the function you completed to add the message as a user message
		self.addUserMessasge(message)

		# 2. Call Azure to send the message to GPT
		res = openai.ChatCompletion.create(
			model='gpt-3.5-turbo-16k',
			messages=self.messages,
		)

		message = res['choices'][0]['message']['content']
		
		# 3. Use the function you completed to add the response as an AI message
		self.addAIMessasge(message)

		# 4. Return the response string
		return message
