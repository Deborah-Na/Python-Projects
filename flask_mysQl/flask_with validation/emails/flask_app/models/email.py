from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash


class Email:

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']
        # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('email_schema').query_db(query)
# Create an empty list to append our instances of friends
        emails = []
# Iterate over the db results and create instances of friends with cls.
        if results:
            for email in results:  
                emails.append(cls(email))
        return emails

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO emails ( email , created_at , updated_at) VALUES ( %(email)s , NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('email_schema').query_db( query, data )
    
    # @classmethod
    # def get_one(cls, data):
    #     query ="SELECT * FROM user WHERE id = %(id)s;"
    #     results= connectToMySQL('users_schema').query_db(query, data)
    #     print(results)
    #     if results:
    #         return cls(results[0])

    # @classmethod
    # def update(cls, data):
    #     query= "UPDATE user SET first_name = %(first_name)s, last_name= %(last_name)s, email= %(email)s, updated_at=NOW() " \
    #         "WHERE id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query= "DELETE from emails WHERE id =%(id)s;"
        return connectToMySQL('email_schema').query_db( query, data )

    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL("email_schema").query_db(query,email)
        if len(results) >= 1:
            flash("Someone else has that email address.")
            is_valid=False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!!!")
            is_valid=False
        return is_valid
