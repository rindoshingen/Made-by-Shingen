from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/soto-zen')
def zen():
	return render_template('pages/soto-zen.html')

@app.route('/coding')
def coding():
	return render_template('pages/coding.html')

@app.route('/bookshelf')
def books():
	return render_template('pages/bookshelf.html')

@app.route('/resources')
def resources():
	return render_template('pages/resources.html')

@app.route('/colophon')
def colophon():
	return render_template('pages/colophon.html')

app.run(debug=True)
