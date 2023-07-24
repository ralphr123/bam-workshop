# Load environment variables
from dotenv import load_dotenv; load_dotenv()

# Flask is used to accept HTTP requests
from flask import Flask, request, make_response

# To generate random strings
from uuid import uuid4

# To generate random numbers
from random import randint

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
    header['Access-Control-Allow-Origin'] = '*'
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

        return { 'success': True  }
    except Exception as e:
        print(f"Failed exercise 1 tests: {e}")
        return { 'success': False }

# EXERCISE 2
    
@app.route('/exercise2', methods=['POST'])
def exercise2():
    try:
        data = request.get_json()
        messages = data.get('messages')

        if messages == None:
            raise Exception('No message provided in request body.')

        chat = Exercise2__Chat()
        chat.messages = messages[:-1]
        res = chat.sendMessage(messages[-1].get('content'))

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)

        return { 'messages': chat.messages }
    except Exception as e:
        print(f"Error running exercise 2: {e}")
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

        return { 'success': True  }
    except Exception as e:
        print(f"Failed exercise 2 tests: {e}")
        return { 'success': False }

# EXERCISE 3

@app.route('/exercise3', methods=['POST'])
def exercise3():
    try:
        data = request.get_json()
        system_msg = data.get('systemMessage')
        messages = data.get('messages')

        if system_msg == None or messages == None:
            raise Exception('No message provided in request body.')

        chat = Exercise3__Chat(system_msg)
        chat.messages += messages[:-1]
        res = chat.sendMessage(messages[-1].get('content'))

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)

        return { 'messages': chat.messages[1:] if system_msg else chat.messages }
    except Exception as e:
        print(f"Error running exercise 3: {e}")
        return {}
    
@app.route('/exercise3/run-tests')
def exercise3Tests():
    try:
        randId = str(uuid4())
        system_msg = f"You are a droid, and you end off every message with -{randId}"
        chat = Exercise3__Chat(system_msg)
        res = chat.sendMessage('Hello!')

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)

        if (not randId in res):
            raise Exception("Incorrect response recieved: ", res)

        return { 'success': True  }
    except Exception as e:
        print(f"Failed exercise 3 tests: {e}")
        return { 'success': False }

@app.route('/exercise4/<maze_code>')
def exercise4(maze_code: str):
    try:
        chat = Exercise3__Chat(Exercise4__system_msg)
        res = chat.sendMessage(maze_code)

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)

        return { 'instructions': res.splitlines() }
    except Exception as e:
        print(f"Error running exercise 4: {e}")
        return {}
    
@app.route('/exercise4/run-tests')
def exercise4Tests():
    try:
        maze_code = f'\\instr -R {randint(0, 4)} -U {randint(0, 2)} -L {randint(0, 5)}'
        chat = Exercise3__Chat(Exercise4__system_msg)
        res = chat.sendMessage(maze_code)

        if (not isinstance(res, str)):
            raise Exception("Response is not a string. Recieved: ", res)
        
        instructions = res.splitlines()

        generated_maze_code = '\\instr'
        for instruction in instructions:
            split_instruction = instruction.split(' ')

            if not len(split_instruction) == 4:
                raise Exception(f"Malformed instructions, recieved: {instructions}")

            _, direction, steps, _ = split_instruction

            generated_maze_code += f" -{direction[0].upper()} {steps}"

        if not generated_maze_code == maze_code:
            raise Exception(f"Generated code: {generated_maze_code} does not match maze code: {maze_code}")
        
        return { 'success': True  }
    except Exception as e:
        print(f"Failed exercise 4 tests: {e}")
        return { 'success': False }

@app.route('/')
def helloWorld():
    response = make_response({ 'success': True  })
    response.set_cookie(key='bex-exercise4', value='true', domain="localhost")

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)
