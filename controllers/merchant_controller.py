from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants", methods=["GET"])
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("/merchants/index.html", merchants = merchants)

@merchants_blueprint.route("/merchants", methods=["POST"])
def show_merchants():
    merchantname = request.form['merchant_name']
    merchantdesc = request.form['merchant_description']
    merchant = Merchant(merchantname, merchantdesc)
    merchant_repository.save(merchant)
    return redirect("/merchants")
