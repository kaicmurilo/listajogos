

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
Bcrypt = Bcrypt(app)

# importacao views
from views_user import *
from views_game import *

if __name__ == '__main__':
    app.run(debug=True)
