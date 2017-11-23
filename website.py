# Imports
from flask import Flask, render_template, request, json, g, flash
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

    _hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=_hashed_password)
    session.add(new_user)
    session.commit()


@app.route('/login')
def show_login():
    return render_template('login.html')

# TODO have Chris check this. Totally made this up. Also, does return current_user_id give me a good variable? How can I keep this cached?
@app.route('/postlogin', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        sess['logged_in'] = True
    else:
        flash('wrong password!')
    return main()


def do_user_login():
    if request.form['password'] == 'password' and request.form['username'] == 'name':
        sess['logged_in'] = True
    else:
        flash('wrong password!')
    return main()


def login():
    email = request.form['inputEmail']
    password = request.form['inputPassword']
    return email, password


def authentication():
    email, password = login()
    checked_password = check_password_hash(password)
    if email and checked_password in User():
        current_user_id = session.query(User).filter(User.email == email).one()
        return current_user_id, json.dumps({'message': 'User Authenticated !'})

    else:
        return json.dumps({'message' : 'User Authentication Failed !'})


@app.route('/sams')
def sams():
    return render_template('sams.html')
                
               
@app.route('/gameplay')
def gameplay():
  return render_template('gameplay.html')

                
#Calling the Program
if __name__ == "__main__":
    app.run()
