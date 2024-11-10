from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

on = [ True, True, True, True, True ]

@app.route("/")
def home():
    return render_template("home.html", on=on);

@app.route("/toggle/<int:i>")
def toggle(i: int):
    global on

    on[i] = not on[i]
    return redirect(url_for("home"))

@app.route("/get")
def get():
    global on
    return {"active": on}

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
