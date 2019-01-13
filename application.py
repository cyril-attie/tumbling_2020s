#!/home/murichun/web/CS50/bin/python

from flask import Flask, render_template, request

app=Flask(__name__, static_folder='static')

@app.route('/')
def landing():
  return render_template('landing.html')

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/crisis')
def crisis():
  return render_template("crisis.html")

@app.route("/forecasting")
def forecasting():
  return render_template('forecasting.html')

@app.route("/economics")
def economics():
  return render_template('economics.html')