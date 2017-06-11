from flask import Flask
from flask import request
from flask import render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.debug('A value for debugging')
    random = os.urandom(24)
    return random

@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'jack':
            error = 'valid username/password'
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/multi',methods=['GET','POST'])
def multiRequest():
    if request.method == 'GET':
        return 'this is get'
    else:
        return 'this is post'

@app.route('/render')
@app.route('/render/<name>')
def renderPage(name=None):
    return render_template('index.html',name=name)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

def valid_login(name,password):
    return 1==1

def log_the_user_in(name):
    app.logger.debug(name)
    return name

if __name__ == "__main__":
    app.run()
