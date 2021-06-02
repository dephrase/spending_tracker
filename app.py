from models.transaction import Transaction
from models.user import User
from flask import Flask, render_template

from controllers.tag_controller import tags_blueprint
from controllers.user_controller import users_blueprint
from controllers.merchant_controller import merchants_blueprint
from controllers.transaction_controller import transactions_blueprint
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository
import repositories.tag_repository as tag_repository

app = Flask(__name__)

app.register_blueprint(tags_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(merchants_blueprint)
app.register_blueprint(transactions_blueprint)

@app.route('/')
def home():
    transactions = transaction_repository.select_all()
    total_spending = transaction_repository.get_total_spending()
    total_transactions = transaction_repository.get_total_transactions()
    frequent_merchant = transaction_repository.get_frequent_merchant()
    frequent_merchant_name = frequent_merchant[1]
    frequent_merchant_visits = frequent_merchant[0]
    most_expensive_transaction = transaction_repository.get_most_expensive_transaction()
    frequent_tag = transaction_repository.get_frequent_tag()
    frequent_tag_purchases = frequent_tag[0]
    frequent_tag_name = frequent_tag[1]
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()

    tag_percentage = {}
    spent_dict = {}
    for tag in tags:
        listoftrans = tag_repository.transactions(tag)
        amountspent = transaction_repository.get_total_of_list(listoftrans)
        if amountspent > 0:
            spent_dict[tag.tag_name] = amountspent
            tag_percentage[tag.tag_name] = round(((amountspent / total_spending) * 100), 2)

    merchant_percentage = {}
    merch_dict = {}
    for merchant in merchants:
        listoftrans = merchant_repository.transactions(merchant)
        amountspent = transaction_repository.get_total_of_list(listoftrans)
        if amountspent > 0:
            merch_dict[merchant.merchant_name] = amountspent
            merchant_percentage[merchant.merchant_name] = round(((amountspent / total_spending) * 100), 2)

    
    userlist = user_repository.select_all()
    user = userlist[0]
    User.budget_status = staticmethod(User.budget_status)
    budget_status = User.budget_status(user, total_spending)

    return render_template('index.html', total_spending=total_spending, total_transactions=total_transactions, frequent_merchant_name=frequent_merchant_name, frequent_merchant_visits=frequent_merchant_visits, most_expensive_transaction=most_expensive_transaction, frequent_tag_purchases=frequent_tag_purchases, frequent_tag_name=frequent_tag_name, tags=tags, spent_dict=spent_dict, merch_dict=merch_dict, user=user, budget_status=budget_status, tag_percentage=tag_percentage, merchant_percentage=merchant_percentage)

if __name__ == '__main__':
    app.run(debug=True)