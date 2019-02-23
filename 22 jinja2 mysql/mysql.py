from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('from.html')

@app.route('/data',methods=['POST','GET'])
def data():
    if request.method == 'POST':
        id = request.form['txt']
        name = request.form['txt1']
        db = pymysql.connect(host = "localhost",user = "root",passwd = "Sem123",database = "test")
        mycursor = db.cursor()
        mycursor.execute("insert into stud values(%s,%s)",(id,name))
        db.commit()
        msg = 'inserted'
    else:
        msg = 'not error error'
    return render_template('success.html',msg = msg)

if __name__ == '__main__':
    app.run(debug=True)