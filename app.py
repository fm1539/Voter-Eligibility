# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import vote_eligibility_determiner


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/results', methods=["GET", "POST"])
def results():
    age = int(request.form['age'])
    eligible = vote_eligibility_determiner(age)
    if eligible:
        msg = "You are eligible to vote! Go register now"
    else:
        yearsLeft = 18 - age
        msg = "Sorry, not eligible. You have " + str(yearsLeft) + " years left to wait in order to be eligible."
    return render_template('results.html', message = msg)