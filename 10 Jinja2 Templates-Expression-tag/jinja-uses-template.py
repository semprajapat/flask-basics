from flask import Flask, render_template

app = Flask(__name__)
@app.route('/jinja/<jin>')

def hello(jin):
    return render_template('Hello.html',name = jin )

if __name__ == '__main__':
    app.run(debug=True)