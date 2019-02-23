# set the cookies and get the cookies by this 

from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def see():
    return render_template('setcookie.html')

@app.route('/setcookie',methods = ['POST','GET'])
def set():
    if request.method == 'POST':
        user = request.form['txt']
        resp = make_response(render_template('respons.html'))
        resp.set_cookie('userId',user)
        return resp

@app.route('/get_cookie')
def get():
    name = request.cookies.get('userId')
    return '<h1>WelCome '+name+' Bro!</h1>'

if __name__ == '__main__':
    app.run(debug=True)