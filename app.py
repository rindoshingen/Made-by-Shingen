from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/soto-zen')
def zen():
	return render_template('soto-zen.html')

@app.route('/coding')
def coding():
	return render_template('coding.html')

@app.route('/bookshelf')
def books():
	return render_template('bookshelf.html')

@app.route('/resources')
def resources():
	return render_template('resources.html')

@app.route('/colophon')
def colophon():
	return render_template('colophon.html')

app.run(debug=True)
