from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<string:name>')
def hi(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:words>/')
def repeat(num,words):
    return f"Hi {num * words}"




if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  