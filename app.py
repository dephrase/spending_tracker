from models.transaction import Transaction
from flask import Flask, render_template

from controllers.tag_controller import tags_blueprint
from controllers.merchant_controller import merchants_blueprint
from controllers.transaction_controller import transactions_blueprint
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository


app = Flask(__name__)

app.register_blueprint(tags_blueprint)
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
    return render_template('index.html', total_spending=total_spending, total_transactions=total_transactions, frequent_merchant_name=frequent_merchant_name, frequent_merchant_visits=frequent_merchant_visits, most_expensive_transaction=most_expensive_transaction)

if __name__ == '__main__':
    app.run(debug=True)