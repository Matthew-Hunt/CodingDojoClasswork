from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninjas').query_db(query)
        dojos = [cls(d) for d in results]
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojo_ninjas').query_db(query, data)

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = """
            SELECT dojos.id AS dojo_id, dojos.name AS dojo_name,
                ninjas.id AS ninja_id, ninjas.first_name, ninjas.last_name, ninjas.age,
                ninjas.created_at AS ninja_created_at, ninjas.updated_at AS ninja_updated_at
            FROM dojos
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('dojo_ninjas').query_db(query, data)
        if not results:
            return None

        dojo = cls(results[0])
        for row in results:
            ninja_data = {
                'id': row['ninja_id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninja_created_at'],
                'updated_at': row['ninja_updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo