from unicodedata import name
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'letSecretKey=*7strawberry' 

@app.route('/')
def index():
    return render_template("dojo.html")

@app.route('/process', methods=['POST'])
def receive():
    print('info received')
    session['name'] = request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comments']= request.form['comments']
    session['personality']= request.form['rate']
    session['age']= request.form['age']
    print(request.form)
    return redirect('/result')

@app.route('/result')
def disp_result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)