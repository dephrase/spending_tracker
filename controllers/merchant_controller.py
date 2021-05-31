from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants", methods=["GET"])
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("/merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants/<id>", methods=["GET"])
def show_merchants(id):
    merchant = merchant_repository.select(id)
    return render_template("/merchants/show.html", merchant=merchant)

@merchants_blueprint.route("/merchants", methods=['POST'])
def add_merchants():
    merchant_name = request.form['merchant_name']
    merchant_description = request.form['merchant_description']
    merchant = Merchant(merchant_name, merchant_description)
    merchant_repository.save(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)

@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    merchant_name = request.form['name']
    merchant_description = request.form['desc']
    merchant = Merchant(merchant_name, merchant_description, id)
    merchant_repository.update(merchant)
    return redirect("/merchants/"+id)