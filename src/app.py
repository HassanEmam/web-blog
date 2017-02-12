from flask import Flask
from flask import render_template
from flask import request
from flask import session

from src.common.database import Database
from src.models.user import User

app = Flask(__name__)
app.secret_key="jose"


@app.route('/')
def home_template():
    return render_template('login.html')


@app.before_first_request
def initialize_db():
    Database.initialize()


@app.route('/login')
def login_template():
    return render_template('login.html')

@app.route('/register')
def register_template():
    return render_template('register.html')


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email=email, password=password):
        User.login(email=email)
    else:
        session['email'] = None

    return render_template('profile.html', email=session['email'])

@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    User.register(email=email, password=password)
    return render_template('profile.html', email=session['email'])

if __name__ == '__main__':
    app.run(port=5000)