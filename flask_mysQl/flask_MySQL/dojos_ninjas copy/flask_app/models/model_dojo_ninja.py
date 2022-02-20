from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.dojo_id=data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
# Create an empty list to append our instances of friends
        ninjas = []
# Iterate over the db results and create instances of friends with cls.
        if results:
            for ninja in results:  
                ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age, dojo_id) " \
            "VALUES ( %(first_name)s , %(last_name)s , %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def get_all_dojo(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        if results:
            for dojo in results:  
                dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query ="SELECT * from dojos JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojo_id= %(id)s;"
        results= connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        if results:
            ninjas = []
            for ninja in results:  
                ninjas.append(Ninja(ninja))
        return ninjas
    
    @classmethod
    def adding(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at) " \
            "VALUES ( %(name)s , NOW(),NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )


