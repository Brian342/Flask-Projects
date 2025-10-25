from flask import Flask, request

app = Flask(__name__)


# declaration of the route
# @app.route('/')
# def index():
#
#     return '<h1>Hello World</h1>'
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p> Your Browser is {}</p>'.format(user_agent)


app.add_url_rule('/', 'index', index)  # the URL, the endpoint name, and the view function


# urls with username
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
