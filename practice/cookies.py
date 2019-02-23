from flask import Flask, redirect, render_template, url_for, request,make_response
app = Flask(__name__)

@app.route('/')
def log():
    return render_template('temp4.html')

@app.route('/login',methods = ['POST','GET'])
def setcookie():
    if request.method == 'POST':
        name = request.form['txt']
        passwd = request.form['passwd']
        resp = make_response(render_template('temp4.html'))
        resp.set_cookie('userID',name)
        resp.set_cookie('passwd', passwd)
        return resp
    else:
        return redirect(url_for('log'))

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    pas = request.cookies.get('passwd')
    return '<h1>name : '+name+'<br>pass : '+pas+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)