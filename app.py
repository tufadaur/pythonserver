from crypt import methods
from operator import truediv
from re import S
from flask import Flask, render_template , request , url_for  ,redirect , session ,g 
import time
import json

app = Flask(__name__)

app.secret_key ="peppeminchia"


@app.route('/', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
          session['loggedin'] = True
          session['user'] = request.form['username']
          return redirect(url_for('home'))
    return render_template('index.html')
       

@app.route('/home')
def home():
  if g.loggedin:
   return render_template('home.html' , user = session['user'])
  return redirect (url_for('login'))

@app.route('/logout')
def logout():
  session.pop('loggedin', None )
  session.pop('user', None )
  return render_template('index.html')

@app.before_request
def before_request():
    g.loggedin = False
    g.user = None

    if 'loggedin' in session:
          g.loggedin = True
    
    if 'user' in session:
          g.user = session['user']
          


if __name__ == '__main__':
    app.debug = True
    #app.run(host="0.0.0.0" , port = 80)
    app.run()