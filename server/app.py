#!/usr/bin/env python3

from flask import Flask
import re

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<printvar>')
def print_string(printvar):
    print(printvar)
    return f'{printvar}'

@app.route('/count/<countvar>')
def count(countvar):
    countstr = ""
    for n in range(int(countvar)):
        countstr+=str(n)+"\n"
    return countstr

@app.route('/math/<num1>/<op>/<num2>')
def math(num1, op, num2):
    res = 0
    if op=='div': res = int(num1)/int(num2)
    elif op=='*': res = int(num1)*int(num2)
    elif op=='+': res = int(num1)+int(num2)
    elif op=='-': res = int(num1)-int(num2)
    elif op=='%': res = int(num1)%int(num2)
    return f'{res}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
