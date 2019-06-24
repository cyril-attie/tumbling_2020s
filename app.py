# home/murichun/web/CS50/bin/python3.7
import os,config
from flask import Flask, render_template, request
from flask_sslify import SSLify
from models import *
# from OpenSSL import SSL
# context = SSL.Context(SSL.SSLv23_METHOD)


app = Flask(__name__)
#sslify = SSLify(app)
app.config.from_object(config.DevelopmentConfig)

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/beginner_economics')
def beginner():
    """Display Tumblien's tale"""
    return render_template('beginner_economics.html')


@app.route('/intermediate_economics')
def intermediate():
    """Display economic crises explanaition"""
    return render_template('intermediate_economics.html')


@app.route('/advanced_economics')
def advanced():
    """Display the Tumbling 20's forecast and cryptofund proposal"""
    return render_template('advanced_economics.html')


@app.route("/about_us")
def about():
    return render_template("about.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/user_page", methods=["POST", "GET"])
def logged_in():
    return render_template("user_page.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # context=('host.cert','host.key')
    app.run(debug=True, host='0.0.0.0', port=port)#, ssl_context=context)
    

