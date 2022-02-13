from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'letSecretKey=*7strawberry'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session['strawberry']=request.form['strawberry']
    session['raspberry']=request.form['raspberry']
    session['apple']=request.form['apple']
    session['name']=request.form['first_name']
    session['last_name']=request.form['last_name']
    print(request.form)
    print('Charging{{Customer name}} for {{count}} fruits')
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    