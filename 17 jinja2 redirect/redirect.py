from flask import Flask, request, render_template, redirect, url_for

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
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return '<html><body>successfull login</body></html>'

if __name__ == '__main__':
    app.run(debug=True)
