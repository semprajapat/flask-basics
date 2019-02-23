from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route('/wel/<name>')

def wel(name):
    return "welcome %s !"%name

@app.route('/login',methods =['get','post'])

def login():
    if request.method == 'post':
        lo = request.form['txt']
        return redirect(url_for('wel',name = lo))
    else:
        lo = request.form['txt']
        return redirect(url_for('wel',name = lo))

if __name__ == '__main__':
    app.run(debug=True)