from flask import Flask, render_template

app = Flask(__name__)

@app.route('/sem/<name>')
def name(name):
    return render_template('temp1.html', name = name)

if __name__ == "__main__":
    app.run(debug=True)