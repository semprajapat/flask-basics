from flask import Flask

app = Flask(__name__)
@app.route('/')
def hoe():
    return 'nahi yaar'

@app.route('/Hello')
def Hello():
    return 'Sem Hello'

if __name__ == '__main__':
    app.run(debug=True)