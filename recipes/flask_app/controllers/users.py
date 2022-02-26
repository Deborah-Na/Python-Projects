from os import rename
from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)


@app.route('/')
def log():
    if 'user_id' not in session:
        return render_template('login.html')
    else: 
        return redirect('/success')

# @app.route('/')
# def log():
#     return render_template('login.html')

# @app.route('/success')
# def success():
#     if session['user_id']== False:
#         return redirect('/')
#     data= {
#         'id': session['user_id']
#     }
#     session['user_id']= True

#     return render_template('success.html', user=User.get_by_id(data))

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    data= {
        'id': session['user_id']
    }

    return render_template('success.html', users=User.get_one(data), recipes= Recipe.get_all_recipes())

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

    User.save(data)
    session['user_id']= User.save(data)
    return redirect('/success')

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
    return redirect('/success')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')