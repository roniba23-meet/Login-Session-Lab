from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET' ,'POST']) # What methods are needed?
def home():
	try:
		if request.method=='POST':
			print("hghfgfh")
			login_session['age']= request.form['age']
			login_session['quote']= request.form['quote']
			login_session['author']= request.form['name']
			return render_template('thanks.html')
		print("777676")
		return render_template('home.html')
	except:
		print("something else")
		return render_template('error.html')
	



@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', age= login_session['age'], quote=login_session['quote'], name=login_session['author'])


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)