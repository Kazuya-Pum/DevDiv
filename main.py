from system import system
from flask import Flask, request, send_file, make_response
from wordcloud import WordCloud
import json
from io import BytesIO


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
	return app.send_static_file('index.html')


@app.route('/divination', methods=['POST'])
def divination():
	body = json.loads(request.get_data())
	owner = body['owner']
	repo = body['repo']
	extension = body['extension']

	res = make_response(system.execute(owner, repo, extension))
	res.headers['Access-Control-Allow-Origin'] = '*'

	return res


@app.route('/makeimage', methods=['POST'])
def makeimage():
	body = json.loads(request.get_data())
	text = body['text']

	output_image = WordCloud(background_color="white", width=900, height=500).generate(text)

	img = BytesIO()
	output_image.to_image().save(img, 'PNG')
	img.seek(0)
	return send_file(img, mimetype='image/png')

app.run(debug=False)
