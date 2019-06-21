from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	#return "Hello"
	name="xyz";
	return render_template("index.html",name=name)

@app.route("/about")
def about():
	return render_template("form1.html")

@app.route("/signin")
def signin():
	return render_template("form.html")
	
if (__name__ == "__main__"):
	app.run(port = 5000)
