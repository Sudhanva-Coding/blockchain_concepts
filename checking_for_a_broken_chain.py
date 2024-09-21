# 1. In the .validate_chain() method, create a for loop with the loop variable i and traverse through the entire length of self.chain. Be sure to start at index 1 instead of index 0. Inside the for loop, create a variable current and assign it to the current block being indexed with i. Create another variable previous and assign it to the previous block using index i-1.

# 2. Verify that the hash of the current block is NOT equal to the value the current block generates via the generate_hash() method. If this condition is true, then the blockchain is not valid, therefore we should return False

# 3. Verify that the hash of the previous hash of the current block is NOT equal to the value generated over the previous block using the generate_hash() method. If this condition is true, then the blockchain is not valid, therefore we should return False

# 4. If the above conditions are not satisfied, then the blockchain is valid! Return True outside the for loop.


# importing the block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  def print_block(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]

      print("Block {} {}".format(i, current_block))
      current_block.print_contents()

# add block to blockchain `chain`
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    print(new_block)
    self.chain.append(new_block)

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      print("Current Hash : ", current.hash)
      print("Generate Hash :", current.generate_hash())

      if(current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True
uac = Block(5579e876832, 1952)
uac.print_block()
print("\n")
uac.generate_hash()

abc = Blockchain()
abc.validate_chain()

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

