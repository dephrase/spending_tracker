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
    newtransaction = Transaction(transactionname, tag, merchant, transactionamount)
    transaction_repository.save(newtransaction)
    return redirect("/transactions")


@transactions_blueprint.route("/transactions/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", transaction=transaction)

@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template('transactions/edit.html', transaction=transaction, merchants=merchants, tags=tags)

@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    transaction_name = request.form['name']
    tag_id = request.form['transaction_tag']
    tag = tag_repository.select(tag_id)
    merchant_id = request.form['transaction_merchant']
    merchant = merchant_repository.select(merchant_id)
    transaction_amount = request.form['transaction_amount']
    transaction = Transaction(transaction_name, tag, merchant, transaction_amount, id)
    transaction_repository.update(transaction)
    return redirect("/transactions/"+id)
