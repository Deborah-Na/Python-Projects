from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash


class Login:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name=data ['last_name']
        self.email = data['email']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_schema').query_db(query)
        users = []
        if results:
            for user in results:  
                users.append(cls(user))
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) " \
            "VALUES ( %(first_name)s , %(last_name)s, %(email)s, %(password)s, NOW(),NOW());"
        return connectToMySQL('login_schema').query_db( query, data )

    @staticmethod
    def validate_login(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("It needs to be longer unless you have 1 letter last name!")
            is_valid=False

#         isLongEnough = False

#         while not isLongEnough:
#         password = input('Enter password at least 5 characters: ')
#         if len(password) >= 5:
#         isLongEnough = True
#         else:
#         print('Password entered is too short')

# print('Your password entered is: ' + password)

        if len(user['password']) < 8:
            flash("Password needs to be at least 8 characters.")
            is_valid=False
        # if not any(char.isdigit() for char in user):
        #     flash("Password should have at least one number!")
        #     is_valid= False
        
        # if not any(char.isupper() for char in user):
        #     flash("Password should have at least one uppercase letter!")
        #     is_valid= False


        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("login_schema").query_db(query,user)
        print(results)
        if len(results) >= 1:
            flash("Someone else has that email address.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_schema").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query= "SELECT * FROM users WHERE id = %(id)s;"
        results= connectToMySQL('login_schema').query_db(query, data)
        return cls(results[0])


