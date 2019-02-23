from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('kp'))

@app.route('/kp')
def kp():
    return 'redirected values'


if __name__ == "__main__":
    app.run(debug=True)