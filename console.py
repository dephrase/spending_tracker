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

tag1 = Tag("Groceries", "Food shopping, bits and bobs for flat maintenance")
tag_repository.save(tag1)

tag2 = Tag("Travel", "Vehicle maintenance, train tickets, etc")
tag_repository.save(tag2)

merchant1 = Merchant("Asda", "Big shop based in the UK")
merchant_repository.save(merchant1)

transaction1 = Transaction("Weekly Shop", tag1.id, merchant1.id, 40)
transaction_repository.save(transaction1)

transaction2 = Transaction("WD40", tag2.id, merchant1.id, 5)
transaction_repository.save(transaction2)








pdb.set_trace()