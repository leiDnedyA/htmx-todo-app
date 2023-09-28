from flask import Flask, send_file
import random

app = Flask(__name__)

phrases = ["Live long and prosper", "Rawr", "Hey gurrrrrrl"]
def random_phrase():
	return phrases[random.randrange(len(phrases))]

@app.route('/')
def home():
	return send_file("index.html")

@app.get('/random_phrase')
def getPhrase():
	return f'<h2>{random_phrase()}</h2>'

if __name__ == "__main__":
	app.run(port=8080, debug=True)
