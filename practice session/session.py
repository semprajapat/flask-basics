from flask import Flask, request, render_template, session, redirect, url_for

app =Flask(__name__)
app.secret_key = 'by  kamlesh'

@app.route('/')
def index():
    if 'username' in session or 'password' in session:
        name = session['username']
        passwd = session['password']
        return 'your are Loged in '+name+' and  '+passwd+''+\
        "<br><a href ='/logout'>click here to Logout</a>"
    return "you are not Login So <a href = '/login'>click here to Login</a>"
 
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if session['username'] == 'Sem' and session['password'] == '123':
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('password',None)
    return redirect(url_for('login'  ))


if __name__ == '__main__':
    app.run(debug=True)