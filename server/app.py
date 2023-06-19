from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(parameter + 1))
    return numbers.rstrip('\n') + '\n'

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return str(result)

def test_count_range_10(self):
    '''counts through range of parameter in "/count/<parameter" on separate lines.'''
    response = app.test_client().get('/count/10')
    count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9'
    assert response.data.decode() == count
     
def test_count_range_10(self):
    '''counts through range of parameter in "/count/<parameter" on separate lines.'''
    response = app.test_client().get('/count/10')
    count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
    assert response.data.decode() == count
