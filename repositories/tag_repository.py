from db.run_sql import run_sql
from models.tag import Tag
from models.transaction import Transaction
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository


def save(tag):
    sql = "INSERT INTO tags (tag_name, tag_description) VALUES (%s, %s) RETURNING id"
    values = [tag.tag_name, tag.tag_description]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for result in results:
        tag = Tag(result['tag_name'], result['tag_description'], result['id'])
        tags.append(tag)
    return tags

def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    tag = Tag(results['tag_name'], results['tag_description'], results['id'])
    return tag

def select_by_name(tagname):
    sql = "SELECT * FROM tags WHERE tag_name = %s"
    values = [tagname]
    results = run_sql(sql, values)[0]
    tag = Tag(results['tag_name'], results['tag_description'], results['id'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def transactions(tag):
    transactions = []
    sql = "SELECT * FROM transactions WHERE transactions.tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)
    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['transaction_name'], tag, merchant, row['amount_spent'], row['id'])
        transactions.append(transaction)
    return transactions

def update(tag):
    sql = "UPDATE tags SET (tag_name, tag_description) = (%s, %s) WHERE id = %s"
    values = [tag.tag_name, tag.tag_description, tag.id]
    run_sql(sql, values)
