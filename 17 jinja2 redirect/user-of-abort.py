from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['txt']
        if name == 'Sem':
            return redirect(url_for('success'))
        else:
            abort(401) # this abort function are used for authentication for user are correct or not
            #its uesd is very usefull for over PROJECT
    return redirect(url_for('index'))# redirect function always take a location of your function name ok they don't take the URL path of the html ok remember that

@app.route('/success')
def success():
    return '<html><body>successfull login</body></html>'

if __name__ == '__main__':
    app.run(debug=True)
