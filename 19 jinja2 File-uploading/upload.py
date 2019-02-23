import os
from flask import Flask, request, render_template

app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/hp/Desktop/python/Flask__Framwork/19 jinja2 File-uploading/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index():
    return render_template('file.html')

@app.route('/uploaded', methods = ['GET','POST'])
def uploaded():
    if request.method == 'POST':
        file = request.files['file']
        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)
        return '<html><body>successfully</body></html>'


if __name__ == '__main__':
    app.run(debug=True)