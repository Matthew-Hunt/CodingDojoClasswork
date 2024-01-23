from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.creator_id = data['creator_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_recipe(cls, data):
        query = """INSERT INTO recipes (creator_id, name, description, instructions, date_made, under_30, created_at, updated_at) 
        VALUES (%(creator_id)s, %(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, NOW(), NOW());"""
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = [cls(recipe) for recipe in results]
        return recipes

    @classmethod
    def get_recipe_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        if results:
            recipe = cls(results[0])
            return recipe
        return None

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes
        SET name = %(name)s,
        description = %(description)s,
        instructions = %(instructions)s,
        date_made = %(date_made)s,
        under_30 = %(under_30)s,
        updated_at = NOW()
        WHERE id = %(id)s;"""
        connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def delete_recipe(cls, data):
        deleted = False
        recipe = cls.get_recipe_by_id(data)
        if session.get('user_id') and recipe and recipe.creator_id == session['user_id']:
            query = "DELETE FROM recipes WHERE id = %(id)s;"
            connectToMySQL('recipes_schema').query_db(query, data)
            deleted = True
        return deleted

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe name must be at least 3 characters long", "recipe")
            is_valid = False
        if len(data['description']) < 3:
            flash("Recipe description must be at least 3 characters long", "recipe")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Recipe instructions must be at least 3 characters long", "recipe")
            is_valid = False
        if not data['date_made']:
            flash("Date made must be entered", "recipe")
            is_valid = False
        return is_valid
