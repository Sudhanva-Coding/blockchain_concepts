# 1. Every Block in the blockchain has a timestamp associated with it. In order to dynamically generate a timestamp, we must import a Python module that returns the current date and time.


from datetime import date
today = date.today()

# dd/mm/yy
d1 = today.strftime("%d /%m / %Y")
print("d1 = ", d1)

# textual month , day, year
d2 = today.strftime("%B %d, %Y")
print("d2 = ", d2)

#mm/dd/y
d3 = today.strftime("%m / %d / %y")
print("d3 = ", d3)

# month, m, year, day

d4 = today.strftime("%b - %d - %Y")
print("d4 = ", d4)

# 2. Inside the datetime module there is a .now() method that returns the current date and time.Call the datetime module’s .now() method to print out the current date and time. 

from datetime import datetime
d6 = datetime.now()
print("d6 = ", d6)

# dd/mm/YY H:M:S
dt_string = d6.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


#Part 3 to be done next class


# 3. Now let’s work on creating our Block. We will be passing transactions and previous_hash to the default constructor each time a Block is created. Complete the __init__() method inside the Block class by initializing the following instance variables: transactions, previous_hash, nonce (with a default value of 0)

class Block:
  # defauly constructor for block class
  def __init__(self, transactions, previous_hash, timestamp, nonce = 0):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.timestamp = datetime.now()
    self.nonce = nonce
    pass

# create first object
s1 = Block(4500, 123, 0)

#access instance variable
print ("Object 1")
print("Nonce : ", s1.nonce)

#Inside the __init__() method, create a timestamp instance variable that stores the current date and time

class Time:
    def __init__(self):
        self.timestamp = datetime.now()
        print(self.timestamp)