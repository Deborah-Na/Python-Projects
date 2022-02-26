from os import rename
from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.user import User
from flask_app.models.task import Task
from flask_bcrypt import Bcrypt
from flask import flash

bcrypt = Bcrypt(app)

@app.route('/create')
def create_task():
    return render_template("add_task.html")

@app.route('/new', methods=['POST'])
def add_task():
    if not Task.validate_task(request.form):
        return redirect('/create')
    data = {
        'user_id': request.form['user_id']
    }
    print(request.form)
    Task.save(request.form)
    return redirect('/dashboard')

@app.route('/tasks/<int:id>')
def view_task(id):
    task_id = {
        "id": id
    }
    one_task = Task.get_one_task(task_id)
    return render_template("view.html", one_task=one_task)

@app.route('/tasks/edit/<int:id>')
def edit_task(id):
    data= {
        "id": id
    }
    task = Task.get_one_task(data)
    return render_template("edit_task.html", edit_task=task)

@app.route('/tasks/update', methods=["POST"])
def updates():
    if not Task.validate_task(request.form):
        return redirect(f"/tasks/edit/{request.form['id']}")
    Task.update(request.form)
    return redirect('/dashboard')

@app.route('/tasks/delete/<int:id>')
def deleted(id):
    data={"id": id}
    Task.delete(data)
    return redirect('/dashboard')




    #strftime('%Y-%m-%d')
    # using this depending on how you chang the letters will change the format "february 22, 2022"
