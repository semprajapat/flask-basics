from flask import Flask
from flask_mail import Message, Mail


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kamlesh.prajapat@sait.ac.in'
app.config['MAIL_PASSWORD'] = 'Sem123##'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
@app.route('/')
def index():
    msg = Message('Hello',sender='kamlesh.prajapat@sait.ac.in', recipients=['semprajapat31@gmail.com'])
    msg.body = 'ha bhai kesa h ?'
    mail.send(msg)
    return 'message Send'

if __name__ == '__main__':
    app.run(debug=True)