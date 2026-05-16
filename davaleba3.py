class BankAccount:
    bank_name = "TBC Bank"
    __total_accounts = 0 

    def __init__(self, owner, balance):
        BankAccount.__total_accounts += 1
        
        
        self._owner = owner 
        
        self.__account_number = f"AN{BankAccount.__total_accounts:04d}"
        
        if BankAccount.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0.0
            print(f"Warning: Invalid initial balance for {owner}. Set to 0.0")

  
    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.__balance += amount
            print(f"Successfully deposited {amount} to {self.__account_number}.")
        else:
            print("Transaction failed: Amount must be positive.")

    def withdraw(self, amount):
        if not BankAccount.validate_amount(amount):
            print("Transaction failed: Amount must be positive.")
            return
        
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew {amount} from {self.__account_number}.")
        else:
            print("Transaction failed: Insufficient funds.")

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner
        print(f"Account owner changed to: {new_owner}")

  
    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"





acc1 = BankAccount("Lasha Kakabadze", 1000)
acc2 = BankAccount("Nino Beridze", 500)
acc3 = BankAccount("Giorgi Mgeladze", -50)  

print("--- ობიექტების ბეჭდვა ---")
print(acc1)
print(acc2)
print(acc3)

print("\n--- ტრანზაქციების შემოწმება ---")
acc1.deposit(500)
acc1.withdraw(300)
print(f"Lasha's Balance: {acc1.check_balance()}")


acc2.withdraw(1000)

acc2.deposit(-100)

print("\n--- მფლობელის შეცვლა და ანგარიშის ნომრის წაკითხვა ---")
acc2.change_owner("Nino Beridze-Kapanadze")
print(f"Account number: {acc2.get_account_number()}")
print(acc2)

print("\n--- კლასის საერთო სტატისტიკა ---")
print(f"Bank Name: {BankAccount.bank_name}")
print(f"Total Accounts Created: {BankAccount.get_total_accounts()}")