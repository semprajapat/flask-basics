from flask import Flask, render_template

app = Flask(__name__)
@app.route('/result')

def result():
    dict = {'Subject':'Marks','english':50,'maths':80,'Hindi':100}
    return render_template('for.html',result = dict)

if __name__ == '__main__':
    app.run(debug=True)