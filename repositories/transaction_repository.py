from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant

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
        transaction = Transaction(row['transaction_name'], row['tag_id'], row['merchant_id'], row['amount_spent'])
        transactions.append(transaction)
    return transactions

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    transaction = Transaction(result['transaction_name'], result['tag_id'], result['merchant_id'], result['amount_spent'])
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
        if 'transaction.merchant_id' in results.keys():
            results['transaction.merchant.name'] += 1
        else:
            results['transaction.merchant.name'] = 1
    
