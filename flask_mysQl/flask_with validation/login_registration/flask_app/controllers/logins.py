from os import rename
from re import S
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)
from flask import render_template,redirect,request, session
from flask_app.models.login import Login


@app.route('/')
def log():
    return render_template('login.html')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/logout')
    data= {
        'id': session['user_id']
    }

    return render_template('success.html', user=Login.get_by_id(data))

@app.route('/register', methods=["POST"])
def register():
    if not Login.validate_login(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    user_id = Login.save(data)
    session['user_id']= user_id

    return redirect('/success')

@app.route('/login', methods=["POST"])
def login():
    data = {"email" : request.form["email"] }
    user_in_db = Login.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id']= user_in_db.id
    session['first_name']= user_in_db.first_name
    return redirect('/success')

@app.route('/logout')
def logout():
    print(session.clear())
    session.clear()
    return redirect('/')
