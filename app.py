from flask import Flask, render_template, request

app = Flask(__name__)

users = {}

@app.route('/')
def homeHandler():
	return render_template('home.html')

@app.route('/sign-up', methods=[ 'GET', 'POST' ])
def signUpHandler():
	if request.method == 'GET':
		return render_template("sign-up.html")
	else:
		u_name = request.form['user_name']
		password = request.form['password']

		if users.get( u_name ):
			return 'User already exists. Please <a href="/sign-in">sign in</a> to continue.'
		else:
			users[ u_name ] = password
			return 'I am signing up %s' %u_name

@app.route('/sign-in', methods=[ 'GET', 'POST' ])
def signInHandler():
	if request.method == 'GET':
		return render_template("sign-in.html")
	else:
		return 'I am signing in'


if __name__ == '__main__':
	app.run(debug=True)