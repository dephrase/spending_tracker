import pdb

from models.tag import Tag
import repositories.tag_repository as tag_repository

tag_repository.delete_all()

tag1 = Tag("Groceries")
tag_repository.save(tag1)





pdb.set_trace()