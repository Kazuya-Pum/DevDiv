from system import system
from bottle import Bottle

app = Bottle()

@route('/divination', method='POST')
def divination():
	owner = app.request.forms.owner
	repo = app.request.forms.repo
	extension = app.request.forms.extension
	return system.execute(owner, repo, extension)

app.run(host='localhost', port='8080', debug=True)
