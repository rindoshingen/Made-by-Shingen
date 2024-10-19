from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	breadcrumbs = [{'name': 'Home', 'url': '/'}]
	return render_template('index.html', page_title="Home", breadcrumbs=breadcrumbs, show_header=False)

@app.route('/soto-zen')
def zen():
	breadcrumbs = [{'name': 'Home', 'url': '/'}, {'name': 'Soto Zen', 'url': '/soto-zen'}]
	return render_template('pages/soto-zen.html', page_title="[S]oto Zen", breadcrumbs=breadcrumbs, show_header=True)

@app.route('/coding')
def coding():
	breadcrumbs = [{'name': 'Home', 'url': '/'}, {'name': 'Coding', 'url': '/coding'}]
	return render_template('pages/coding.html', page_title="[C]oding", breadcrumbs=breadcrumbs, show_header=True)

@app.route('/bookshelf')
def books():
	breadcrumbs = [{'name': 'Home', 'url': '/'}, {'name': 'Bookshelf', 'url': '/bookshelf'}]
	return render_template('pages/bookshelf.html', page_title="[B]ookshelf", breadcrumbs=breadcrumbs, show_header=True)

@app.route('/resources')
def resources():
	breadcrumbs = [{'name': 'Home', 'url': '/'}, {'name': 'Resources', 'url': '/resources'}]
	return render_template('pages/resources.html', page_title="[R]esources", breadcrumbs=breadcrumbs, show_header=True)

@app.route('/colophon')
def colophon():
	breadcrumbs = [{'name': 'Home', 'url': '/'}, {'name': 'Colophon', 'url': '/colophon'}]
	return render_template('pages/colophon.html', page_title="[C]olophon", breadcrumbs=breadcrumbs, show_header=True)

app.run(debug=True)
