# create the dynamic url by this program
#and also use learn how to get the data on flask by the url

from flask import Flask

app = Flask(__name__)

@app.route('/Hello/<name>') #<name> treated as a string

def Hello(name):
    return 'Sem %s !' %name 

@app.route('/int/<int:id>') #<int:id> treated as a integer  url is :http://127.0.0.1:5000/int/45
def k(id):
    return 'Enter Id : %d'%id

if __name__ == '__main__':
    app.run(debug=True)