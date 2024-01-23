from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.cookie_order import CookieOrder

@app.route("/")
@app.route("/cookies")
def index():
    orders = CookieOrder.get_all()
    return render_template("cookies.html", orders=orders)

@app.route("/cookies/new", methods=["GET"])
def new_page():
    return render_template("new_order.html")

@app.route("/cookies/edit/<int:cookie_id>", methods=["GET"])
def edit_page(cookie_id):
    order = CookieOrder.get_by_id(cookie_id)
    return render_template("edit_order.html", order=order)

@app.route("/cookies", methods=["POST"])
def create_cookie():
    cookie_order = request.form

    if not CookieOrder.is_valid(cookie_order):
        return redirect("/cookies/new")

    CookieOrder.create(cookie_order)

    return redirect("/cookies")

@app.route("/cookies/edit/<int:cookie_id>", methods=["POST"])
def update_cookie(cookie_id):
    cookie_order = request.form

    if not CookieOrder.is_valid(cookie_order):
        return redirect(f"/cookies/edit/{cookie_id}")

    CookieOrder.update(cookie_order)

    return redirect("/cookies")
