from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'letSecretKey=*7strawberry' #set a secret key for security purposes



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])



            
# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
# # Never render a template on a POST request.
# # Instead we will redirect to our index route.
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
