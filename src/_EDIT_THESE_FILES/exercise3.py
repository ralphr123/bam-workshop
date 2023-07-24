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

class Chat:
	def __init__(self, system_msg: str = None):
		self.messages = []

		if (system_msg):
			self.addSystemMessage(system_msg)

	def addSystemMessage(self, message: str) -> None:
		self.messages.append({'role': 'system', 'content': message})

	def addUserMessasge(self, message: str) -> None:
		self.messages.append({'role': 'user', 'content': message})

	def addAIMessasge(self, message: str) -> None:
		self.messages.append({'role': 'assistant', 'content': message})

	def sendMessage(self, message: str) -> str:
		self.addUserMessasge(message)

		res = openai.ChatCompletion.create(
			model='gpt-3.5-turbo-16k',
			messages=self.messages,
			temperature=0
		)

		message = res['choices'][0]['message']['content']
		
		self.addAIMessasge(message)

		return message
	
	def getChatMessages(self) -> List:
		chatMessages = []

		for message in self.messages:
			if message['role'] != 'system':
				chatMessages.append(message)
		
		return chatMessages

if __name__ == '__main__':
	print("Exercise 3 optional test area.")
