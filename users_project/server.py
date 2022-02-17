from flask import Flask, render_template, request, redirect
# import the class from friend.py
from users import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    
    return redirect("/users")

@app.route('/users')
def display_users():
    return render_template('create.html', users=User.get_all())

@app.route("/users/new")
def new():
    return render_template("read.html")

@app.route('/users/create', methods=["POST"])
def create_users():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # We pass the data dictionary into the save method from the Friend class.
    User.save(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/user/display/<int:id>')
def display(id):
    data= {"id": id}
    return render_template("display.html", user=User.get_one(data))

@app.route('/users/update/<int:id>', methods=['POST'])
def update(id):
    User.update(request.form)
    return redirect('/users')

@app.route('/users/edit/<int:id>')
def edit_user(id):
    data= {"id": id}
    return render_template("edit.html", user=User.get_one(data))

@app.route('/users/delete/<int:id>')
def deleted(id):
    data={"id": id}
    User.delete(data)
    return redirect('/users')







            
            
if __name__ == "__main__":
    app.run(debug=True)

