import threading
import time

# Transaction Class to log transactions
class Transaction:
    def __init__(self, type, amount, balance_after):
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return f"{self.timestamp} - {self.type} of ${self.amount}, Balance: ${self.balance_after}"

# Customer Class to represent a customer
class Customer:
    def __init__(self, customer_id, name, account_balance, account_type):
        self.customer_id = customer_id
        self.name = name
        self.account_balance = account_balance
        self.account_type = account_type
        self.transactions = []
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.account_balance += amount
            self.transactions.append(Transaction("Deposit", amount, self.account_balance))

    def withdraw(self, amount):
        with self.lock:
            if self.account_balance >= amount:
                self.account_balance -= amount
                self.transactions.append(Transaction("Withdrawal", amount, self.account_balance))
            else:
                raise ValueError("Insufficient funds")

    def apply_interest(self):
        with self.lock:
            if self.account_type == "Savings":
                interest = self.account_balance * 0.02  # 2% interest rate
                self.account_balance += interest
                self.transactions.append(Transaction("Interest", interest, self.account_balance))

    def get_transaction_history(self):
        return [str(transaction) for transaction in self.transactions]

# BankingSystem Class for managing customers and operations
class BankingSystem:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, account_balance, account_type):
        customer = Customer(customer_id, name, account_balance, account_type)
        self.customers[customer_id] = customer

    def get_customer(self, customer_id):
        return self.customers.get(customer_id)

    def deposit(self, customer_id, amount):
        customer = self.get_customer(customer_id)
        if customer:
            customer.deposit(amount)
            
            print(f"Deposited ${amount} to {customer.name}'s account. New balance: ${customer.account_balance}")
        else:
            print("Customer not found.")

    def withdraw(self, customer_id, amount):
        customer = self.get_customer(customer_id)
        if customer:
            try:
                customer.withdraw(amount)
                print(f"Withdrew ${amount} from {customer.name}'s account. New balance: ${customer.account_balance}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Customer not found.")

    def view_transaction_history(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer:
            history = customer.get_transaction_history()
            if history:
                print("\nTransaction History:")
                for transaction in history:
                    print(transaction)
            else:
                print("No transactions found.")
        else:
            print("Customer not found.")

    def apply_interest_periodically(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer:
            while True:
                customer.apply_interest()
                print(f"Interest applied to {customer.name}'s account. New balance: ${customer.account_balance}")
                time.sleep(10)  # Apply interest every 10 seconds

# Main Simulation Function
def main():
    banking_system = BankingSystem()

    # Manually add customers (no CSV file)
    banking_system.add_customer("101", "John Doe", 5000, "Checking")
    banking_system.add_customer("102", "Jane Smith", 3000, "Savings")
    banking_system.add_customer("103", "Alice Johnson", 7000, "Savings")

    # Example of deposit and withdraw operations
    banking_system.deposit("101", 1000)  # John Doe deposits $1000
    banking_system.withdraw("102", 500)  # Jane Smith withdraws $500

    # View transaction history for John Doe
    banking_system.view_transaction_history("101")

    # Simulate interest application in a separate thread for Alice Johnson's savings account
    threading.Thread(target=banking_system.apply_interest_periodically, args=("103",), daemon=True).start()

    # Keeping the main thread alive to let daemon thread run
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

