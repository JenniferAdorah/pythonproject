from abc import ABC, abstractmethod
from symtable import Class


# encapsulation
class Account:
    def __init__(self,account_id,holder_name,balance):
        self.account_id=account_id
        self.holder_name=holder_name
        self.balance=balance


    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited {amount}.New balance: {self.balance}")
    def withdraw(self,amount):
        print(f"Attempting to withdraw {amount} from account with balance"
              f"{self.balance}")
        if amount<=self.balance:
            self.balance -=amount
        else:
            print("insufficient balance")

    def get_balance(self):
        return self.balance

    def get_holder_name(self):
        return self.holder_name

    # inheritance
class Customer(Account):
    def __init__(self,account_id,holder_name,balance,phone_number):
        super().__init__(account_id, holder_name, balance)
        self.phone_number =phone_number





# polymorphism
class Transaction:
    def __init__(self,amount):
        self.amount =amount
    def execute(self,account):
        pass


class DepositTransaction(Transaction):
    def execute(self,account):
        account.deposit(self.amount)

class WithdrawTransaction(Transaction):
    def execute(self,amount):
        amount.withdraw(self.amount)
# Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
class MpesaPaymentSystem(PaymentSystem):
    def process_payment(self,amount):
        print(f"Processing Mpesa payment of {amount}")

# example usage
mpesa = MpesaPaymentSystem
account1=Customer(account_id=1,holder_name="Adorah",balance=2000,
                 phone_number=110517810)
deposit=DepositTransaction(500)
withdraw=WithdrawTransaction(1500)

deposit.execute(account1)
withdraw.execute(account1)
print(f"The balance of {account1.get_holder_name()} is :"
      f" {account1.get_balance()}")
MpesaPaymentSystem
account2=Customer(account_id=2,holder_name="Jennifer",balance=250,
                  phone_number=23456781)
deposit=DepositTransaction(200)
withdraw=WithdrawTransaction(500)
...
deposit.execute(account2)
withdraw.execute(account2)
print(f"The balance of {account2.get_holder_name()} is"
      f" {account2.get_balance()}")
