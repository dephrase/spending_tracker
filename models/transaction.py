class Transaction:
    def __init__(self, transaction_name, tag_id, merchant_id, amount_spent, id=None):
        self.transaction_name = transaction_name
        self.tag_id = tag_id
        self.merchant_id = merchant_id
        self.amount_spent = amount_spent
        self.id = id