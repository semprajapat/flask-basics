from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods = ['POST','GET'])
def lo():
    if request.method == 'POST':
        name = request.form['txt']
        passwd = request.form['passwd']
        resp = make_response(render_template('new.html'))
        resp.set_cookie('userID',name)
        resp.set_cookie('pass',passwd)
        return resp

if __name__ == '__main__':
    app.run(debug=True)

