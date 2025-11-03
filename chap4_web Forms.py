from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
Bootstrap = Bootstrap(app)
moment = Moment(app)


if __name__ == "__main__":
    app.run(debug=True)