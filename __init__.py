from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/bills")
def bills():
    return render_template("bills.html")


@app.route("/groups")
def groups():
    return render_template("groups.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)