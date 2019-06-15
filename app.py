# home/murichun/web/CS50/bin/python3.7
import os

from flask import Flask, render_template, request
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


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


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    app.run(debug=True)
