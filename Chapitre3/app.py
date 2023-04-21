from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/user/<username>')
def user(username):
    return render_template("user.html", name=username)

