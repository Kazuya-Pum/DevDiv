from system import system
from bottle import route, run, template, request


@route('/divination', method='POST')
def divination():
	owner = request.forms.owner
	repo = request.forms.repo
	extension = request.forms.extension
	return system.execute(owner, repo, extension)

run(host='localhost', port='8080', debug=True)
