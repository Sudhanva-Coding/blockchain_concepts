# # 1. Create a class block

# # 2. In the .generate_hash() method, create the variable block_contents, which combines the Block timestamp, transactions, nonce, and previous hash.
# #Wrap each item in the str() method in order to convert them to a string type to prepare for hashing. Return the result.

# #3. Create a variable block_hash. Create a new hash with sha256() and block_contents and save the value to block_hash. Remember to use the .encode() method to encode the string. Update the method to return block_hash

# #4. Return the text hash value by calling the hexdigest() method on block_hash

# from datetime import datetime
# from hashlib import sha256

# class Block:
#   def __init__(self, transactions, previous_hash, nonce = 0):
#     self.timestamp = datetime.now()
#     self.transactions = transactions
#     self.previous_hash = previous_hash
#     self.nonce = nonce
#     self.hash = self.generate_hash()

#   def print_block(self):
#     # print block contents
#     print("timestamp : ", self.timestamp)
#     print("transactions : ", self.transactions)
#     print("current hash : ", self.generate_hash())

#   def generate_hash(self):
#     # hash the block contents
#     block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
#     print(block_contents)
#     return block_contents

#     block_hash = sha256 (block_contents.encode())
#     print(block_hash.hexdigest())
#     return block_hash.hexdigest()

# use = Block(143123142332981114278961239e123, 1932)
# use.print_block()
# print("\n")
# use.generate_hash()

from block import Block
    

from datetime import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()

  def print_block(self):
    # print block contents
    print("timestamp : ", self.timestamp)
    print("transactions : ", self.transactions)
    print("current hash : ", self.generate_hash())

  def generate_hash(self):
    # hash the block contents
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
    print(block_contents)
    return block_contents

    block_hash = sha256 (block_contents.encode())
    print(block_hash.hexdigest())
    return block_hash.hexdigest()

use = Block(143123142332981114278961239e123, 1932)
use.print_block()
print("\n")
use.generate_hash()