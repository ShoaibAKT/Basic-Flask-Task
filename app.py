from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f'Hello {name}!'
    else:
        return 'Please provide a name.'

@app.route('/square')
def square():
    num = request.args.get('num')
    if num:
        try:
            num = int(num)
            result = num ** 2
            return f'The square of {num} is {result}.'
        except ValueError:
            return 'Please provide a valid integer.'
    else:
        return 'Please provide a number.'
