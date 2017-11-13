# Imports
from flask import Flask, render_template, request, json, g

from werkzeug.security import generate_password_hash, check_password_hash


# App Setup
app = Flask(__name__)


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


@app.route('/postlogin')
def login():
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    return email, password
    
def authentication():
    email, password = login()
    


if __name__ == "__main__":
    app.run()
