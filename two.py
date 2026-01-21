class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # ❌ local variable only
        self.balance = balance    # ❌ local variable only

    def deposit(self, amount):
        self.balance += amount    # ❌ tries to change a local variable, not the object
        print(f"{self.owner}'s new balance: {self.balance}")  # ❌ self.owner not stored in object

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:   # ❌ self.balance doesn’t exist on the object
            print(f"{self.owner} cannot withdraw {amount}, not enough money!")
        else:
            self.balance -= amount
            print(f"{self.owner}'s new self.balance: {self.balance}")
    
    def dd(self):
        print(f"{self.owner} cannot withdraw {self.amount}, not enough money!")



alice = BankAccount("Alice", 100)
bob = BankAccount("Bob", 200)

alice.deposit(50)    # Alice’s balance changes, Bob’s does not
bob.withdraw(30)     # Bob’s balance changes, Alice’s does not
bob.dd()     # Bob’s balance changes, Alice’s does not
