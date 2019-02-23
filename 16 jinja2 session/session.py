from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'any random string'
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as <b>'+ username +'</b><br>'+\
        "<a href ='/logout'>click here to logout</a>"
    return "You are not loged in<br> <a href = '/login'>click here to login</a>"


@app.route('/login', methods = ['POST','GET'])

def login():         #login path to set and rediredted to index and many thing
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)