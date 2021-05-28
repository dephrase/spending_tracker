import pdb

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

tag_repository.delete_all()
merchant_repository.delete_all()
transaction_repository.delete_all()

tag1 = Tag("Groceries")
tag_repository.save(tag1)

merchant1 = Merchant("Asda", "Big Shop")
merchant_repository.save(merchant1)

transaction1 = Transaction("Weekly Shop", tag1.id, merchant1.id, 40)
transaction_repository.save(transaction1)







pdb.set_trace()