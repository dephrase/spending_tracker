from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (user_name, budget) VALUES (%s, %s) RETURNING *"
    values = [user.user_name, user.budget]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    user = User(results['user_name'], results['budget'], results['id'])
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['user_name'], row['budget'], row['id'])
        users.append(user)
    return users

def update_budget(user):
    sql = "UPDATE users SET budget = %s WHERE id = %s"
    values = [user.budget, user.id]
    run_sql(sql, values)