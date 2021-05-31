import pdb

from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()


tag1 = Tag("Groceries", "Food shopping, bits and bobs for flat maintenance")
tag_repository.save(tag1)

tag2 = Tag("Travel", "Vehicle maintenance, train tickets, etc")
tag_repository.save(tag2)

merchant1 = Merchant("Asda", "Big shop based in the UK")
merchant_repository.save(merchant1)

merchant2 = Merchant("Amazon", "Jeffs Shoap")
merchant_repository.save(merchant2)

transaction1 = Transaction("Weekly Shop", tag1, merchant1, 40)
transaction_repository.save(transaction1)

transaction2 = Transaction("WD40", tag2, merchant1, 5)
transaction_repository.save(transaction2)

transaction3 = Transaction("Torch", tag2, merchant2, 15)
transaction_repository.save(transaction3)








pdb.set_trace()