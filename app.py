from flask import Flask, render_template, request
#from flask_session import Session
import os

app = Flask(__name__)

#app.config["SESSION_PERMANENT"]=False
#app.config["SESSION_TYPE"]="filesystem"
#Session(app)
#app.secret_key=os.urandom(24)

@app.route("/", methods=["POST","GET"])
def index():
	if request.method=="POST" :
		#session["user"]="new user"
		user="New User"
		if requst.form.get("pwd")=="password" :
			#session["user"]=request.form.get("userid")
			user=request.form["userid"]
			return render_template("index.html",user=user)

	return render_template("index.html",user=user)


@app.route("/about")
def about():
	return render_template("form1.html")

@app.route("/signin")
def signin():

	return render_template("form.html")


if (__name__ == "__main__"):
	app.run(port = 5000)
