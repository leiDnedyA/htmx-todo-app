from flask import Flask, send_file
from sqlalchemy import create_engine, text
import random

app = Flask(__name__)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

phrases = ["Live long and prosper", "Rawr", "Hey gurrrrrrl"]
def random_phrase():
	return phrases[random.randrange(len(phrases))]

def start_engine():
	with engine.connect() as conn:
		result = conn.execute(text("select 'hello world'"))
		print(result.all())

@app.route('/')
def home():
	return send_file("index.html")

@app.get('/random_phrase')
def getPhrase():
	return f'<h2>{random_phrase()}</h2>'

if __name__ == "__main__":
	start_engine()
	app.run(port=8080, debug=True)
