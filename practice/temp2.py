from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def name():
    return render_template('temp2.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        passwd = request.form['passwd']
        if name == 'kp' and passwd == '123':
            return render_template('temp1.html')
        else:
            return redirect(url_for('name'))


if __name__ == "__main__":
    app.run(debug=True)
