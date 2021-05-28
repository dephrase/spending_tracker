from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (tag_name) VALUES (%s) RETURNING id"
    values = [tag.tag_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for result in results:
        tag = Tag(result['tag_name'])
        tags.append(tag)
    return tags

def select(id):
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    tag = Tag(results['tag_name'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)