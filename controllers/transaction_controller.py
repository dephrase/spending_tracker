from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions", methods=["GET"])
def transactions():
    transactions = transaction_repository.select_all()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("/transactions/index.html", transactions=transactions, tags=tags, merchants=merchants)

@transactions_blueprint.route("/transactions", methods=['POST'])
def add_transactions():
    transactionname = request.form['transaction_name']
    transactiontag = request.form['transaction_tag']
    tag = tag_repository.select_by_name(transactiontag)

    transactionmerchant = request.form['transaction_merchant']
    merchant = merchant_repository.select_by_name(transactionmerchant)

    transactionamount = request.form['transaction_amount']
    newtransaction = Transaction(transactionname, tag.id, merchant.id, transactionamount)
    transaction_repository.save(newtransaction)
    return redirect("/transactions")