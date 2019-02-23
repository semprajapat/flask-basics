from flask import Flask, render_template

app = Flask(__name__)

@app.route('/state/<int:score>')

def hello(score):
    return render_template('statement.html',mark = score)

if __name__ == '__main__':
    app.run(debug=True)