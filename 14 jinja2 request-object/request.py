from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def hell():
    return render_template("form.html") #calling the form.html for insert the data on that

@app.route("/result", methods = ['POST','GET'])

def hello():
    if request.method == 'POST':
        resul = request.form 
        return render_template("result.html", result = resul)# use for receive the requested
        # data on the result.html to print that data as a table form by using the syntax of
        # jinja2 templates use expression tag......

if __name__ == '__main__':
    app.run(debug=True)