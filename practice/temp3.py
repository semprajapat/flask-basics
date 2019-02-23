from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def sdfl():
    return render_template('temp3.html')

if __name__ == '__main__':
    app.run(debug=True)