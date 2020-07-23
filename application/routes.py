#This file is created to seperately handle all routes in one file.

from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")