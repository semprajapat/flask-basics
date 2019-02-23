from flask import Flask, session, render_template,redirect,url_for, request

app = Flask(__name__)

app.secret_key = 'Kamlesh'

@app.route('/')
def index():
    if 'username' in session and 'password' in session:
        name = session['username']
        passwd = session['password']
        return 'You are Login name = '+name+' password = '+passwd+ '<br><a href = "/logout">Click To Logout</a>'
    else:
        return 'You are not Login so <a href = "/login">click here</a>'

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['txt']
        session['password'] = request.form['passwd']
        if session['username'] == 'Sem' and session['password'] == '123':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('temp5.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('password',None)
    return redirect(url_for('login'  ))

if __name__ == '__main__':
    app.run(debug=True)
