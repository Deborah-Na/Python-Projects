from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.email import Email

@app.route("/")
def index():
    
    return redirect("/email")

@app.route('/email')
def display_users():
    return render_template('add_email.html', emails=Email.get_all())


@app.route('/email/create', methods=["POST"])
def add_emails():
    if not Email.validate_email(request.form):
        return redirect('/')

    Email.save(request.form)
    return redirect('/email/success')

@app.route('/email/success')
def succeed():
    return render_template("registered_email.html", emails=Email.get_all())

@app.route('/email/delete/<int:id>')
def delete(id):
    data={"id": id}
    Email.delete(data)
    return redirect('/email')


# @app.route('/user/display/<int:id>')
# def display(id):
#     data= {"id": id}
#     return render_template("display.html", user=User.get_one(data))

# @app.route('/users/update/<int:id>', methods=['POST'])
# def update(id):
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/users/edit/<int:id>')
# def edit_user(id):
#     data= {"id": id}
#     return render_template("edit.html", user=User.get_one(data))

# @app.route('/users/delete/<int:id>')
# def deleted(id):
#     data={"id": id}
#     User.delete(data)
#     return redirect('/users')