from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    #return '<h1>home!!</h1>'
    return render_template('home.html')

@app.route('/signin', methods=['get'])
def signin_form():
    # return '<form action="/signin" method= "POST">' \
    #        '<p><input name="username"></p>' \
    #        '<p><input password="password"></p>' \
    #        '<p><button type="submit">signin</button></p>' \
    #        '</form>'
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if request.form['username']=='admin':
        # return '<h3>Hello, admin!</h3>'
        return render_template('signin-ok.html',username= username)
    # return '<h3>Bad username or password.</h3>'
    return render_template('form.html',message='Bad username or password', username=username)


if __name__ == "__main__":
    app.run()