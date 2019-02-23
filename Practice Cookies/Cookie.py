from flask import Flask, render_template,request,make_response

app = Flask(__name__)

@app.route('/')
def see():
    return render_template('form.html')

@app.route('/form',methods = ['POST','GET'])
def set():
    if request.method =='POST':
        user = request.form['txt']
        passwd = request.form['passwod']
        if user == 'Sem' or passwd == "123":
            resp = make_response(render_template('new.html'))
            resp.set_cookie('userID',user)
            resp.set_cookie('pas',passwd)
            return resp
        else:
            return '<h1>Worng Details </h1>'

@app.route('/getcookie')
def get():
    name = request.cookies.get('userID')
    passw = request.cookies.get('pas')
    return '<h1>name : '+name+'<br>pass : '+passw+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)
