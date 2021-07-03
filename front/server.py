from bottle import route, run, template, request
from datetime import datetime
from time import sleep

@route('/hello')
def hello():
	now = datetime.now()
	# return template('Hello World! {{now}}', now=now)
	return template('index_template', text='')

@route('/hello', method='POST')
def do_hello():
	sleep(10)
	input_text = request.forms.input_text
	return template('index_template', text=input_text)

run(host='localhost', port='8080', debug=True)