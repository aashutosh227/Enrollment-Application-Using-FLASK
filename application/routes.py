#This file is created to seperately handle all routes in one file.

from application import app
from flask import render_template, jsonify
import json
import os

#The following decoraters specify the patterns for which the index function will be called
#So it is called for "/", "index" and "home".
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template("index.html", login=False)

@app.route('/login')
def login():
    return render_template("login.html", login=False)

@app.route('/register')
def register():
    return render_template("register.html", login=False)

@app.route('/courses')
def courses():
    course_data = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, 
                {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, 
                {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, 
                {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, 
                {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

    # if os.path.exists(os.path.join(os.getcwd(), 'courses.json')):
    #     with open(os.path.join(os.getcwd(), 'courses.json')) as courses_file:
    #         course_data = json.load(courses_file)
    #         print(course_data)
    # else:
    #     print(os.getcwd())
    #     print("path dosen't exists")
    print(course_data)
    return render_template("course.html", courseData=course_data)