from os import rename
from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.user import User
from flask_app.models.task import Task
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)


@app.route('/')
def log():
    if 'user_id' not in session:
        return render_template('login.html')
    else: 
        return redirect('/dashboard')

@app.route('/dashboard')
def success():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session["user_id"]
    }
    this_user= User.get_one(data)
    task_list= Task.get_all_tasks_with_user()
    print("this is my user object!!")
    # final run, can run stuff into the return
    return render_template('dashboard.html', all_task= task_list, user= this_user)

@app.route('/register', methods=["POST"])
def register():
    if not User.validate_login(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    session['user_id']= User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=["POST"])
def login():
    data = {"email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect('/')
# put this portion into model with return False
    session['user_id']= user_in_db.id
    session['first_name']= user_in_db.first_name
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





@app.route('/testing')
def testing():
    print("this is my testing page!")
    return "all test ran successfully!"