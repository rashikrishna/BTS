from flask import Flask, render_template, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

@app.route("/", methods=["POST"])
def index():
	#return "Hello"
	session["user"]="new user"
	session["user"]=request.form.get("userid")
	return render_template("index.html",user=session["user"])

@app.route("/about")
def about():
	return render_template("form1.html")

@app.route("/signin")
def signin():
	return render_template("form.html")

if (__name__ == "__main__"):
	app.run(port = 5000)
