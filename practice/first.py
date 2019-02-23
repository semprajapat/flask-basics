from flask import Flask

app = Flask(__name__)

@app.route('/first')
def first():
    return 'hello fisrt flask'

if __name__ == '__main__':
    app.run(debug=True)
