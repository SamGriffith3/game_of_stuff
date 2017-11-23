# Imports
from flask import Flask, render_template, request, json, g, redirect, abort, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from local_db import User, Cards, session
from flask import session as sess

# App Setup

app = Flask(__name__)


# APP.ROUTEs
@app.route("/")
def main():
    return render_template('index.html')


@app.route('/signup')
def show_sign_up():
    return render_template('signup.html')


@app.route('/postsignup', methods=['POST'])
def post_sign_up():
    name = request.form['inputName']
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    check = session.query(User).filter(User.email == email).one_or_none()
    if not check:
        _hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password=_hashed_password)
        session.add(new_user)
        session.commit()
        print("new user signed up!")
        return "logged in!"
    return abort(403)


@app.route('/login')
def show_login():
    return render_template('login.html')


@app.route('/postlogin', methods=['POST'])
def do_login():
    stored = session.query(User).filter(User.name == request.form['username']).one_or_none()
    if stored:
        if check_password_hash(stored.password, request.form['password']):
            sess['logged_in'] = True
    return main()


@app.route('/sams')
def sams():
    return render_template('sams.html')
                
               
@app.route('/gameplay')
def gameplay():
  return render_template('gameplay.html')

                
#Calling the Program
if __name__ == "__main__":
    app.run()
