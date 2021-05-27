from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (merchant_name)  VALUES (%s) RETURNING id"
    values = [merchant.name]
    results = run_sql(sql, values)

    id = results[0]['id']
    merchant.id = id

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['merchant_name'])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    merchant = Merchant(results['merchant_name'])
    return merchant
