from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
	user = request.form['nm']
	return render_template('hello.html',name = user)

if __name__ == '__main__':
	app.run(debug='true')