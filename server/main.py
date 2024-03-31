from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

on = True

@app.route("/")
def home():
    return render_template("home.html", on=on);

@app.route("/toggle")
def toggle():
    global on

    on = not on
    return redirect(url_for("home"))

@app.route("/get")
def get():
    global on
    return {"active": on}
