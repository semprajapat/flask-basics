from flask import Flask

app = Flask(__name__)

@app.route('/')
def first():
    return '<html><body> ha bhai <br><a href = "/second">click MOOD</a></body></html>'

@app.route('/second')
def secon():
    return 'tu ja yaar'

if __name__ == '__main__':
    app.run(debug=True)