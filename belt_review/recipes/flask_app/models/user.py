from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from flask_app import app
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        return result[0]

    @classmethod
    def get_users(cls):
        query = "SELECT * FROM users ORDER BY first_name DESC"
        results = connectToMySQL('recipes_schema').query_db(query)
        users = [cls(user) for user in results]
        return users

    @staticmethod
    def validate_registration(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        email = connectToMySQL('recipes_schema').query_db(query, data)

        if not data['first_name'].isalpha() or len(data['first_name']) < 2:
            flash("First name must be only letters and at least 2 characters long", "registration")
            is_valid = False
        if not data['last_name'].isalpha() or len(data['last_name']) < 2:
            flash("Last name must be only letters and at least 2 characters long", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is not valid!", "registration")
            is_valid = False
        elif email:
            flash("Email is already registered!", "registration")
            is_valid = False
        if len(data['password']) < 8 or not any(char.isupper() for char in data['password']) or not any(char.islower() for char in data['password']) or not any(char.isdigit() for char in data['password']):
            flash("Password must be at least 8 characters and contain uppercase and lowercase letters and a number", "registration")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords must match", "registration")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)

        if not result:
            flash("No matching email", "login")
            return False

        user = result[0]
        if not bcrypt.check_password_hash(user['password'], data['password']):
            flash("Incorrect password entered", "login")
            return False

        return user
