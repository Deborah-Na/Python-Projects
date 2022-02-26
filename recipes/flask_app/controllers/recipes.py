from os import rename
from unicodedata import name
from flask_app import app
from flask import render_template,redirect,request, session
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/create')
def create_recipes():
    return render_template("add_recipes.html")

@app.route('/recipes/new', methods=['POST'])
def add_recipes():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/create')
    data = {
        'user_id': request.form['user_id']
    }
    print(request.form)
    Recipe.save(request.form)
    return redirect('/success')

@app.route('/recipes/<int:id>')
def display_recipes(id):
    user_data= {
        "id": session['user_id']
        }
    recipe_data ={
        "id": id
    }

    return render_template("show_recipe.html", one_recipe= Recipe.get_one(recipe_data), user= User.get_one(user_data))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    data= {"id": id}
    return render_template("edit_recipes.html", recipe= Recipe.get_one(data))

@app.route('/recipes/update', methods=['POST'])
def updates():
    Recipe.update(request.form)
    return redirect('/success')

@app.route('/recipes/delete/<int:id>')
def deleted(id):
    data={"id": id}
    Recipe.delete(data)
    return redirect('/success')