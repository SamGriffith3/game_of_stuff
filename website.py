# Imports
from flask import Flask, render_template, request, json, g
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash


# App Setup
app = Flask(__name__)

Base = declarative_base()
Session = sessionmaker()
session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/signup')
def show_sign_up():
    return render_template('signup.html')


@app.route('/postsignup', methods=['POST'])
def post_sign_up():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

    # TODO Make this hashed password code readable

    _hashed_password = generate_password_hash(_password)
    cursor.callproc('sp_createUser', (_name, _email, _hashed_password))
    data = cursor.fetchall()
    new_user = User(name=_name, email=_email, password=_hashed_password)
    session.add(new_user)
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message': 'User created successfully !'})
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/login')
def show_login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()