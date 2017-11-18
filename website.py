# Imports
from flask import Flask, render_template, request, json, g, Session
from flask.ext.session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from local_db import User, Cards, session


# App Setup
sess = Session()

def create_app():
    app = Flask(__name__)
    sess.init_app(app)
    return app


# APP.ROUTEs
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

    # TODO Make this hashed password code readable...did I? Oh PyCharm tell me I did...

    _hashed_password = generate_password_hash(_password)
    new_user = User(name=_name, email=_email, password=_hashed_password)
    session.add(new_user)
    if len(data) is 0:
        session.commit()
        return json.dumps({'message': 'User created successfully !'})
    else:
        return json.dumps({'error': str(data[0])})


@app.route('/login')
def show_login():
    return render_template('login.html')

# TODO have Chris check this. Totally made this up. Also, does return current_user_id give me a good variable? How can I keep this cached?
@app.route('/postlogin', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


def do_user_login():
    if request.form['password'] == 'password' and request.form['username'] == '_name':
        session['logged_in] = True
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
        return current_user_id, json.dumps({'message' : 'User Authenticated !'})
        session.commit()
    else:
        return json.dumps({'message' : 'User Authentication Failed !'})
    return render_template('gameplay.html')


@app.route('/sams')
def sams():
    return render_template('sams.html')

#Calling the Program
if __name__ == "__main__":
    app.run()
