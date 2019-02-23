from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return "Hello Admin Broo!"


@app.route('/gue/<guest>')
def guest(guest):
    return 'Hello %s as a GUest'%guest


@app.route('/user/<name>')
def user(name):
    if name =='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest = name))


if __name__ == '__main__':
    app.run(debug=True)