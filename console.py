import pdb

from models.tag import Tag
from models.user import User
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.tag_repository as tag_repository
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()

user1 = User("David", 800)
user_repository.save(user1)

tag1 = Tag("Groceries", "Food shopping, bits and bobs for flat maintenance")
tag_repository.save(tag1)

tag2 = Tag("Travel", "Vehicle maintenance, train tickets, etc")
tag_repository.save(tag2)

tag3 = Tag("Bills", "Mortgage, gas, heating etc")
tag_repository.save(tag3)

tag4 = Tag("Eating out", "Takeaways, restaurants etc")
tag_repository.save(tag4)

merchant1 = Merchant("Asda", "UK based grocery store")
merchant_repository.save(merchant1)

merchant2 = Merchant("Amazon", "Jeffs Shoap")
merchant_repository.save(merchant2)

merchant3 = Merchant("Just Eat", "Online takeaway service")
merchant_repository.save(merchant3)

merchant4 = Merchant("Scotrail", "Thieving bastarts")
merchant_repository.save(merchant4)

merchant5 = Merchant("Virgin", "Mortgage Provider")
merchant_repository.save(merchant5)

merchant6 = Merchant("Uber Eats", "Online takeaway service")
merchant_repository.save(merchant6)

transaction1 = Transaction("Weekly Shop", tag1, merchant1, 40)
transaction_repository.save(transaction1)

transaction2 = Transaction("Monthly train ticket", tag2, merchant4, 32)
transaction_repository.save(transaction2)

transaction3 = Transaction("Mortgage", tag3, merchant5, 380)
transaction_repository.save(transaction3)

transaction4 = Transaction("KFC", tag4, merchant3, 20)
transaction_repository.save(transaction4)

transaction5 = Transaction("McDonalds", tag4, merchant3, 22)
transaction_repository.save(transaction5)

transaction6 = Transaction("Katsu Curry", tag4, merchant6, 25)
transaction_repository.save(transaction6)







pdb.set_trace()