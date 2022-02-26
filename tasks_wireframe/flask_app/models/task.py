from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash
from flask_app.models import user

class Task:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description= data['description']
        self.due_date = data['due_date']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']
        self.user_id= data['user_id']

    @classmethod
    def get_all_tasks_with_user(cls):
        query= "SELECT * from tasks JOIN users on users.id=tasks.user_id"
        results= connectToMySQL('tasks_schema').query_db(query)
        print(results)
        tasks = []
        if results:
            for row in results:  
                this_task= cls(row)
                user_data= {
                    **row, #destructuring the row
                    "id": row["users.id"],
                    "created_at": row["users.created_at"],
                    "updated_at":   row["users.updated_at"]
                }
                #custom attribute to make it into an object
                this_task.user = user.User(user_data)
                tasks.append(this_task)
        return tasks

        #put it here.. the left JOIN stuff with the  right query
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO tasks (name, description, due_date, created_at, updated_at, user_id) VALUES ( %(name)s , %(description)s, %(due_date)s, NOW(),NOW(), %(user_id)s);" 
        return connectToMySQL('tasks_schema').query_db( query, data )
    
    @staticmethod
    def validate_task(task):
        is_valid= True # we assume this is true
        if len(task['name']) < 2:
            flash("Name must be at least 2 characters.", 'add_task')
            is_valid = False
        if len(task['description']) < 5:
            flash("Give us a proper description!", "add_task")
            is_valid = False
        if task['due_date'] == "":
            flash("Add a date!", "add_task")
            is_valid = False
        return is_valid

    @classmethod
    def get_one_task(cls, data):
        query = "SELECT * from tasks LEFT JOIN users on users.id=tasks.user_id WHERE tasks.id= %(id)s;"
        results= connectToMySQL('tasks_schema').query_db(query, data)
        print(results)
        if results:
            one_task = cls (results[0])
            for row in results:
                user_data = {
                
                    "id":row['users.id'],
                    "created_at": row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                    'first_name': row["first_name"],
                    'last_name': row["last_name"],
                    'email': row['email'],
                    'password': row['password']
                }
                one_task.user = user.User(user_data)
                # one_car_seller.get_car_seller.append(one_car_seller)
            return one_task

    
    # @classmethod
    # def get_id(cls, data):
    #     query= "SELECT * from cars LEFT JOIN users ON users.id= cars.user_id WHERE cars.id = %(id)s;"

    #     results = connectToMySQL('belt_schema').query_db(query,data)
    #     print(results)
    #     cars = []
    #     for row in results:
    #         this_car= cls(row)
    #         data= {
    #             **row,
    #             "id": row["users.id"],
    #             "created_at": row["users.created_at"],
    #             "updated_at": row["updated_at"]
    #         }
    #         this_car.seller.append(user.User(data))
            #     **row,
            #     "id" : row["users.id"],
            #     "first_name" : row["first_name"],
            #     "last_name" : row["last_name"],
            #     "email": row["email"],
            #     "password": row["password"],
            #     "created_at": row["users.created_at"],
            #     "updated_at": row["users.updated_at"]
            # }
            # user_one = user.User(this_car.owner)
            # cars.append(user_one)

        #     cars.append(this_car)
        # return cars
    
    @classmethod
    def update(cls, data):
        query="UPDATE tasks SET name = %(name)s, due_date = %(due_date)s, description = %(description)s WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('tasks_schema').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query= "DELETE from tasks WHERE id =%(id)s;"
        return connectToMySQL('tasks_schema').query_db( query, data )

@classmethod
def delete(cls, data):
    query= "DELETE from tasks WHERE id =%(id)s;"
    return connectToMySQL('tasks_schema').query_db( query, data )

    