class PaymentProcessor:
    def __init__(self, balance=0):
        self.balance = balance

    def add_funds(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance

    def make_payment(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return f"Payment of ₹{amount} successful. Remaining balance: ₹{self.balance}"


# Example usage
account = PaymentProcessor(balance=1000)
account.add_funds(500)
print(account.make_payment
