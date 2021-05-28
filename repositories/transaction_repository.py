from db.run_sql import run_sql
from models.transaction import Transaction

def save(transaction):
    sql = "INSERT INTO transactions (transaction_name, tag_id, merchant_id, amount_spent) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.transaction_name, transaction.tag_id, transaction.merchant_id, transaction.amount_spent]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)
