from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def anasayfa():
    return render_template("index.html")



@app.route("/secondpage")
def secondpage():
    return render_template("a.html")


@app.route("/thirdpage")
def thirdpage():
    return render_template("b.html")

@app.route("/fourthpage")
def fourthpage():
    return render_template("c.html")

app.run(debug=True)