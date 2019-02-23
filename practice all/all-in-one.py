from flask import Flask,request, render_template, redirect, url_for, make_response
import os

UPLOAD_FILE = 'C:/Users/hp/Desktop/python/Flask Framwork/practice all/upload/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FILE

@app.route('/')
def index():
    return render_template('form.html')


@app.route('/login',methods = ['POST','GET'])

def login():
    if request.method == 'POST':
        name = request.form['txt']
        passwd = request.form['passwd']
        file = request.files['file']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
        if name == 'Sem' or passwd == '123':
            resp = make_response(render_template('k.html'))
            resp.set_cookie('userId',name)
            resp.set_cookie('pass',passwd)
            return resp
        
            
        

@app.route('/logout')
def logout():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)