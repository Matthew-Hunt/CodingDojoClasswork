from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/success')
def success():
    return "You have successfully rendered a page"

@app.route('/hello/<string:name>')
def hello(name):
    return "Hello welcome to Flask " + name

@app.route('/<owner>/<bank>')
def owner_bank(owner, bank):
    return owner + " owns " + bank

@app.route('/<bank>/<int:number>')
def bank_number(bank, number):
    return f"{bank} has {number} of customers";

if __name__=="__main__":
    app.run(debug=True)