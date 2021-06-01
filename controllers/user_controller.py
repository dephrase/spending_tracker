from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
from models.user import User
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

users_blueprint = Blueprint("myprofile", __name__)

@users_blueprint.route("/myprofile", methods=["GET"])
def users():
    users = user_repository.select_all()
    user = users[0]
    return render_template("/myprofile/index.html", user=user)

@users_blueprint.route("/myprofile/<id>/edit", methods=["GET"])
def edit(id):
    user = user_repository.select(id)
    return render_template('myprofile/edit.html', user=user)

@users_blueprint.route("/myprofile/<id>/<username>", methods=["POST"])
def update_budget(id, username):
    username = username
    budget = request.form['budget']
    user = User(username, budget, id)
    user_repository.update_budget(user)
    return redirect("/myprofile")
