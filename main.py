from system import system
from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')


@app.route('/divination', methods=['POST'])
def divination():
	body = request.get_json()
	owner = body['owner']
	repo = body['repo']
	extension = body['extension']
	return system.execute(owner, repo, extension)

# app.run()
