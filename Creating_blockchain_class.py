from datetime import datetime
from hashlib import sha256

class Block :
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()

  def print_block(self):
    print("timestamp : ", self.timestamp)
    print("transactions : ", self.transactions)
    print("current hash : ", self.generate_hash())

  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
    print(block_contents)
    return block_contents


    block_hash = sha256(block_contents.encode())
    print(block_hash.hexdigest())
    return block_hash.hexdigest()

uac = Block(5579e876832, 1952)
uac.print_block()
print("\n")
uac.generate_hash()

