import os
from flask import Flask, request, render_template
app = Flask(__name__)
 
uploaddd= 'C:/Users/hp/Desktop/python/Flask Framwork/practice/uploads'
app.config['UPLOAD_FOLDER'] = uploaddd

@app.route('/')
def index():
    return render_template('temp6.html')

@app.route('/upload', methods = ['POST','GET'])
def uplooad():
    if request.method == 'POST':
        file = request.files['file']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
        return '<h2>Successfully Uploads</h2>'


if __name__ == '__main__':
    app.run(debug=True)