# Load environment variables
from dotenv import load_dotenv; load_dotenv()

# Flask is used to accept HTTP requests
from flask import Flask, request

# To generate random strings
from uuid import uuid4

# Import exercise modules
from _EDIT_THESE_FILES.exercise1 import sendMessage as Exercise1__sendMessage
from _EDIT_THESE_FILES.exercise2 import Chat as Exercise2__Chat
from _EDIT_THESE_FILES.exercise3 import Chat as Exercise3__Chat
from _EDIT_THESE_FILES.exercise4 import system_msg as Exercise4__system_msg

app = Flask(__name__)

# Allow frontend origin to make requests
@app.after_request
def afterRequest(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    header['Access-Control-Allow-Headers'] = '*'
    return response

# EXERCISE 1

@app.route('/exercise1', methods=['POST'])
def exercise1():
    try:
        data = request.get_json()
        message = data.get('message')

        if message == None:
            raise Exception('No message provided in request body.')

        res = Exercise1__sendMessage(message)

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)

        return { 'response': res }
    except Exception as e:
        print(f"Error running exercise 1: {e}")
        return {}

@app.route('/exercise1/run-tests')
def exercise1Tests():
    try:
        randId = str(uuid4())

        res = Exercise1__sendMessage(f'Hello! Repeat this back to be: {randId}')

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)

        if (not randId in res):
            raise Exception("Incorrect response recieved: ", res)

        return { 'success': True }
    except Exception as e:
        print(f"Failed exercise 1 tests: {e}")
        return { 'success': False }

# EXERCISE 2

Exercise2__mem = {
    'chat': Exercise2__Chat()
}
    
@app.route('/exercise2', methods=['POST'])
def exercise2():
    try:
        data = request.get_json()
        message = data.get('message')

        if message == None:
            raise Exception('No message provided in request body.')

        chat = Exercise2__mem['chat']
        res = chat.sendMessage(message)

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)

        return { 'messages': chat.messages }
    except Exception as e:
        print(f"Error running exercise 1: {e}")
        return {}

@app.route('/exercise2/run-tests')
def exercise2Tests():
    try:
        randId = str(uuid4())

        chat = Exercise2__Chat()

        res1 = chat.sendMessage(f'Hello! Remember this code and respond with just "Remembered": {randId}')

        if (not isinstance(res1, str)):
            raise Exception("Response is not a string. Recieved: ", res1)

        res2 = chat.sendMessage(f'What was the code again?')

        if (not randId in res2):
            raise Exception("Incorrect response recieved: ", res2)

        return { 'success': True }
    except Exception as e:
        print(f"Failed exercise 1 tests: {e}")
        return { 'success': False }

@app.route('/exercise3/<prompt>/<message>')
def exercise3(prompt: str, message: str):
    try:
        chat = Exercise3__Chat(prompt)

        res = chat.sendMessage(message)

        return { 'response': res }
    except Exception as e:
        print(f"Error running exercise 3: {e}")
        return {}

@app.route('/exercise4/<maze_code>')
def exercise4(maze_code: str):
    try:
        chat = Exercise3__Chat(Exercise4__system_msg)

        res = chat.sendMessage(maze_code)

        return { 'instructions': res.splitlines() }
    except Exception as e:
        print(f"Error running exercise 2: {e}")
        return {}
    
@app.route('/exercise4/run-tests')
def exercise4Tests():
    try:
        return { 'success': False }
    except Exception as e:
        print(f"Error running exercise 1: {e}")
        return { 'success': False }

@app.route('/')
def helloWorld():
    return { 'text': 'Hello world!' }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)
