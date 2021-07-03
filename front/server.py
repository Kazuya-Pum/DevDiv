from bottle import route, run, template, request
from datetime import datetime
from time import sleep

@route('/hello')
def hello():
	now = datetime.now()
	# return template('Hello World! {{now}}', now=now)
	return template('views/index_template.tpl', owner='',repo='',extension='')

@route('/hello', method='POST')
def do_hello():
	# sleep(10)
	input_owner = request.forms.owner
	input_repo = request.forms.repo
	input_extension = request.forms.extension
	return template('views/index_template.tpl', owner=input_owner,repo=input_repo,extension=input_extension)

run(host='localhost', port='8080', debug=True)