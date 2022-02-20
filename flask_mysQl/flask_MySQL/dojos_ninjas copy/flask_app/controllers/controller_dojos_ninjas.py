from os import rename
from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.model_dojo_ninja import Ninja, Dojo

@app.route("/")
def display_all():
    return render_template('registered_dojo.html', ninjas=Ninja.get_all())
    
    # return redirect("/ninjas")

@app.route('/ninjas')
def display_users():
    return render_template('add_ninja.html', dojos=Dojo.get_all_dojo())

@app.route('/ninjas/add_ninja', methods=["POST"])
def add_ninjas():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')

@app.route('/dojos')
def new():
    return render_template("add_show_dojo.html", dojos=Dojo.get_all_dojo())

@app.route('/dojos/add_dojo', methods=["POST"])
def add_dojos():
    print(request.form)
    # data={
    #     "name": request.form["name"]
    # }
    # Dojo.adding(data)
    Dojo.adding(request.form)
    return redirect('/dojos') 

@app.route('/dojos/<int:id>')
def display_dojo(id):
    data= {
        "id": id
        }
    # ninjas=Dojo.get_one(data)
    # print(ninjas)
    return render_template("registered_dojo.html", ninjas=Dojo.get_one(data)) #ninjas=ninjas )




