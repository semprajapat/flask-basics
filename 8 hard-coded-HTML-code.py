from flask import Flask

app = Flask(__name__)

@app.route('/')
def inedx():
    str = '''<html><body><h1>Hello Sem
    we use a render form template hHahaha </h1> </body></html>''' #render templates form
    return str

if __name__ == '__main__':
    app.run(debug=True)