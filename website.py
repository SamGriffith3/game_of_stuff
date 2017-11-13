from flask import Flask, render_template, request, json
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

    if _name and _email and _password:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/login')
def show_login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
