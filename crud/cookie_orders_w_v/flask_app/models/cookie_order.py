from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class CookieOrder:
    DB = "cookie_orders"

    def __init__(self, cookie_order):
        self.id = cookie_order["id"]
        self.name = cookie_order["name"]
        self.cookie_type = cookie_order["cookie_type"]
        self.num_boxes = cookie_order["num_boxes"]
        self.created_at = cookie_order["created_at"]
        self.updated_at = cookie_order["updated_at"]

    @classmethod
    def is_valid(cls, cookie_order):
        errors = []

        if not cookie_order["name"]:
            errors.append("Name is required.")
        elif len(cookie_order["name"]) < 2:
            errors.append("Name must be at least 2 characters.")

        if not cookie_order["cookie_type"]:
            errors.append("Cookie type is required.")
        elif len(cookie_order["cookie_type"]) < 2:
            errors.append("Cookie type must be at least 2 characters.")

        try:
            num_boxes = int(cookie_order["num_boxes"])
            if num_boxes <= 0:
                errors.append("Please enter a valid number of boxes.")
        except ValueError:
            errors.append("Number of boxes must be a positive integer.")

        if errors:
            flash(" ".join(errors))
            return False

        return True

    @classmethod
    def get_by_id(cls, order_id):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s;"
        data = {
            "id": order_id
        }
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result[0] if result else None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders;"
        orders_data = connectToMySQL(cls.DB).query_db(query)
        orders = [cls(order) for order in orders_data]
        return orders

    @classmethod
    def create(cls, cookie_order):
        query = "INSERT INTO cookie_orders (name, cookie_type, num_boxes) VALUES (%(name)s, %(cookie_type)s, %(num_boxes)s);"
        result = connectToMySQL(cls.DB).query_db(query, cookie_order)
        return result

    @classmethod
    def update(cls, cookie_order):
        query = "UPDATE cookie_orders SET name = %(name)s, cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, cookie_order)
        return result
