import pdb

from models.tag import Tag
from models.merchant import Merchant
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

tag_repository.delete_all()
merchant_repository.delete_all()

tag1 = Tag("Groceries")
tag_repository.save(tag1)

merchant1 = Merchant("Asda", "Big Shop")
merchant_repository.save(merchant1)







pdb.set_trace()