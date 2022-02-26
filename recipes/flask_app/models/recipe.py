from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.under30= data['30mins_under']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']
        self.user_id= data['user_id']

    @classmethod
    def get_all_recipes(cls):
        query= "SELECT * from recipes JOIN users ON users.id=recipes.user_id"
        results= connectToMySQL('recipes_schema').query_db(query)
        print(results)
        if results:
            recipes = []
            for recipe in results:  
                recipes.append(Recipe(recipe))
        return recipes
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes ( name, description, instruction, date_made, 30mins_under, created_at, updated_at, user_id) " \
            "VALUES ( %(name)s , %(description)s, %(instruction)s, %(date_made)s, %(30mins_under)s, NOW(),NOW(), %(user_id)s);" 
        return connectToMySQL('recipes_schema').query_db( query, data )
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid= True # we assume this is true
        if len(recipe['name']) < 2:
            flash("Recipe name must be at least 3 characters.", 'add_recipe')
            is_valid = False
        if len(recipe['description']) < 5:
            flash("Give us a proper description!", "add_recipe")
            is_valid = False
        if len(recipe['instruction']) < 2:
            flash("More please")
        if recipe['date_made']== "":
            flash("choose a date", 'add_recipe') 
            is_valid = False
        if 'under30' not in recipe:
            flash("choose yes or no", 'add_recipe')
            is_valid = False
        return is_valid

    @classmethod
    def get_one(cls, data):
        query = "SELECT * from recipes " \
                "WHERE recipes.id= %(id)s;"
        results= connectToMySQL('recipes_schema').query_db(query, data)
        print(results)
        if len(results)< 1:
            return False
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query= "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, " \
            "30mins_under = %(30mins_under)s, updated_at = NOW() WHERE id = %(id)s;"
        print(query)
        return connectToMySQL('recipes_schema').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query= "DELETE from recipes WHERE id =%(id)s;"
        return connectToMySQL('recipes_schema').query_db( query, data )


    