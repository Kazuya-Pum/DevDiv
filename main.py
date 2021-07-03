from system import system
from flask import Flask, request
from wordcloud import WordCloud
import json
import os


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

	return (system.execute(owner, repo, extension), 200, {"Access-Control-Allow-Origin": "*"})


@app.route('/makeimage', methods=['POST'])
def makeimage():
	body = json.loads(request.get_data())
	text = body['text']

	output_image = WordCloud(background_color="white", width=900, height=500).generate(text)
	output_image.to_file("/Users/kazuya/GitHub/DevDiv/wordcloud_sample.png")
	return 0

app.run(debug=True)
