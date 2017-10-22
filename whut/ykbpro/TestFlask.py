from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return '<h1>Welcome~</h1>'


@app.route('/signIn', methods=['GET'])
def sign_in_get():
    return '''<form action="/signIn" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signIn', methods=['POST'])
def log_in():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return render_template('signIn.html', message='Welcome', username=request.form['username'])
    return render_template('signIn.html', message='Failed', username=request.form['username'])


@app.route('/signInUser', methods=['GET'])
def sign_in_user():
    if request.args.get('me', '') == 'me':
        return '<h3>Hello, me!</h3>'
    return '<h3>nothing!</h3>'


if __name__ == '__main__':
    app.run()
