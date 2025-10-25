from flask import Flask

app = Flask(__name__)


# declaration of th route
@app.route('/')
def index():
    return '<h1>Hello World</h1>'


app.add_url_rule('/', 'index', index)  # the URL, the endpoint name, and the view function


# urls with username
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
