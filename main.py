from system import system
from bottle import Bottle, request, static_file
import json

app = Bottle()

@app.route('/')
def index():
	return static_file('index.html', './static')

@app.route('/<filename>')
def index(filename):
	return static_file(filename, './static')


@app.route('/divination', method='POST')
def divination():
	body = json.load(request.body)
	owner = body['owner']
	repo = body['repo']
	extension = body['extension']
	return system.execute(owner, repo, extension)

app.run(host='localhost', port='8080', debug=True)
