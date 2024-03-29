#This file is created to seperately handle all routes in one file.

from application import app
from flask import render_template, jsonify, request, Response
import json
import os

course_data = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, 
                {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, 
                {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, 
                {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, 
                {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

#The following decoraters specify the patterns for which the index function will be called
#So it is called for "/", "index" and "home".
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", index=True)

@app.route('/login')
def login():
    return render_template("login.html", login=True)

@app.route('/register')
def register():
    return render_template("register.html", register=True)

@app.route('/classes/')
@app.route('/classes/<term>')
def classes(term="Spring 2019"):
    return render_template("course.html",courseData = course_data, courses=True,term=term)

@app.route('/enrollment', methods = ["GET", "POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enroll.html", enrollment=True, course = {"id": id, "title": title, "term": term})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx==None):
        jData = course_data
    else:
        jData = course_data[int(idx)]

    return Response(json.dumps(jData), mimetype="application/json")
