from re import T
from models.tag import Tag
from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import pdb

def save(transaction):
    sql = "INSERT INTO transactions (transaction_name, tag_id, merchant_id, amount_spent) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [transaction.transaction_name, transaction.tag.id, transaction.merchant.id, transaction.amount_spent]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['transaction_name'], tag, merchant, row['amount_spent'])
        transactions.append(transaction)
    return transactions

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    tag = tag_repository.select(result['tag_id'])
    merchant = merchant_repository.select(result['merchant_id'])
    transaction = Transaction(result['transaction_name'], tag, merchant, result['amount_spent'])
    return transaction

def update(transaction):
    sql = "UPDATE transactions SET (transaction_name, tag_id, merchant_id, amount_spent) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.transaction_name, transaction.tag.id, transaction.merchant.id, transaction.amount_spent]
    run_sql(sql, values)

def get_total_spending():
    transactions = select_all()
    total_spending = 0
    for transaction in transactions:
        total_spending += transaction.amount_spent
    return total_spending

def get_total_transactions():
    transactions = select_all()
    count = 0
    for transaction in transactions:
        count += 1
    return count

def get_frequent_merchant():
    transactions = select_all()
    results = {}
    for transaction in transactions:
        if transaction.merchant.merchant_name in results.keys():
            results[transaction.merchant.merchant_name] += 1
        else:
            results[transaction.merchant.merchant_name] = 1
    visits = 0
    location = ""
    for key in results:
        if results[key] > visits:
            visits = results[key]
            location = key
    listresult = [visits, location]
    return listresult

        

    
