import threading


class BankAccount:
    balance: int = 0
    status: bool = False
    threadLock = threading.Lock()

    def __init__(self):
        pass

    def get_balance(self):
        if self.status:
            return self.balance
        else:
            raise ValueError(self)

    def open(self):
        if not self.status:
            self.status = True
        else:
            raise ValueError(self)

    def deposit(self, amount):
        if self.status and amount > 0:
            self.threadLock.acquire()
            self.balance += amount
            self.threadLock.release()
        else:
            raise ValueError(amount)

    def withdraw(self, amount):
        if self.status and amount > 0 and amount <= self.balance:
            self.threadLock.acquire()
            self.balance -= amount
            self.threadLock.release()
        else:
            raise ValueError(amount)

    def close(self):
        if self.status:
            self.status = False
            self.balance = 0
        else:
            raise ValueError(self)
