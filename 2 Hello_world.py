from flask import Flask

app = Flask(__name__)  #it is a construtor

@app.route('/') # it is use for the assign the ip address default like 
#127.0.0.1:5000    and 5000 is a port no. of that it is also a default

def hello():
    return 'Hello Sem Bhai'

if __name__ == '__main__':
    app.run(debug=True) # debug is used for automatically 
    #restart don't run again the program