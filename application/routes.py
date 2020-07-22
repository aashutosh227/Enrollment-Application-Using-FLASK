#This file is created to seperately handle all routes in one file.

from application import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello World!!</h1>"