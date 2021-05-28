from db.run_sql import run_sql
from models.merchant import Merchant
from models.transaction import Transaction

def save(merchant):
    sql = "INSERT INTO merchants (merchant_name, merchant_description) VALUES (%s, %s) RETURNING id"
    values = [merchant.merchant_name, merchant.merchant_description]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['merchant_name'], row['merchant_description'])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    merchant = Merchant(results['merchant_name'], results['merchant_name'])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def transactions(merchant):
    transactions = []

    sql = "SELECT * FROM transactions WHERE transactions.merchant_id = %s"
    values = [merchant.id]
    results = run_sql(sql, values)
    for row in results:
        transaction = Transaction(row['transaction_name'], row['tag_id'], row['merchant_id'], row['amount_spent'], row['id'])
        transactions.append(transaction)
    return transactions