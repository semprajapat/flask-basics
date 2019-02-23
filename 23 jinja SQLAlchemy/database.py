from flask import Flask, render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sem123@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = 'shhhh...iAmASecret!'

class Stud(db.Model):
    sno = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50)) 
    def __init__(self, sno, name):
        self.sno = sno
        self.name = name


@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['sno'] or not request.form['name']:
            flash('Please enter all the fields', 'error')
        else:
            student = Stud(request.form['sno'], request.form['name'])     
        db.session.add(student)
        db.session.commit()
        flash('Record was successfully added')
    return render_template('success.html')

@app.route('/')
def index():
    return render_template('from.html')

if __name__ == "__main__":
    app.run(debug=True)


