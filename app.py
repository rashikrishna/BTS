from flask import Flask, render_template, request
#from flask.ext.session import Session
#from flask_session import Session
#import os

app = Flask(__name__)

#app.config["SESSION_PERMANENT"]=False
#app.config["SESSION_TYPE"]="filesystem"
#Session(app)
#app.secret_key=os.urandom(24)
user="New User"

@app.route("/", methods=["POST","GET"])
def index():
#	if request.method=="POST":
#		if request.form.get("userpwd")=="password":
#				user=request.form.get("userid")
#				return render_template("index,html",user=user)
	#session["user"]=request.form.get("userid")
	return render_template("index.html",user=user)

	#return render_template("index.html",user=user)

@app.route("/index.html")
def index1():
	#session["user"]=request.form.get("userid")
	return render_template("index.html",user=user)

@app.route("/about.html")
def about():
	return render_template("about.html")

@app.route("/signin.html")
def signin():
	return render_template("signin.html")

@app.route("/members.html")
def members():
	return render_template("members.html")



if (__name__ == "__main__"):
	app.run(port = 5000)
