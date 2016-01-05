from flask import Flask, render_template, request, redirect, url_for, abort, session
from socket import gethostname
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@db:5432/flask'

from models import User,db

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    user = User(request.form['username'], request.form['message'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('message', username=user.username))

@app.route('/message/<username>')
def message(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('message.html', username=user.username,
                                           message=user.message)