from flask import Flask

app = Flask(__name__)
@app.route('/')
def hoe():
    return 'nahi yaar'

@app.route('/Hello')
def Hello():
    return 'Sem Hello'


def home():         # add this url by using this function 'add_url_rule('/','home',home) '
    return 'sem Home'

app.add_url_rule('/sem','home',home)


if __name__ == '__main__':
    app.run(debug=True)