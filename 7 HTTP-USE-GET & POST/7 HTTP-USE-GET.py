#post and get method how we use in flask

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/wel/<name>")
def wel(name):
    return "welcome %s Bro!"%name

@app.route("/login",methods = ['POST','GET'])

def login():
    if request.method =='POST':
        user = request.form['txt']
        return redirect(url_for("wel",name = user))
    else:
        user = request.args.form['txt']
        return redirect(url_for('wel',name = user))

if __name__ == "__main__":
    app.run(debug=True) 