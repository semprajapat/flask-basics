from flask import Flask, redirect, request, render_template, flash, url_for

app = Flask(__name__)
app.secret_key = 'flash message'

@app.route('/')
def index():
    return render_template('first_see.html')

@app.route('/login', methods= ['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['txt']
        passs = request.form['passwd']
        if name != 'Sem' or passs != '123':
            error = 'Invalid User name and Password'
        else:
            flash('you are login successfully')
            flash('please logout for next time login')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)

if __name__ == '__main__':
    app.run(debug=True)