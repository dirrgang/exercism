import threading


class BankAccount:
    balance: int = 0
    status: bool = False
    lock: threading.Lock = threading.Lock()

    def __init__(self) -> None:
        pass

    def get_balance(self) -> int:
        if self.status:
            return self.balance
        else:
            raise ValueError(self)

    def open(self) -> None:
        with self.lock:
            if not self.status:
                self.status = True
            else:
                raise ValueError(self)

    def deposit(self, amount: int) -> None:
        with self.lock:
            if self.status and amount > 0:
                self.balance += amount
            else:
                raise ValueError(amount)

    def withdraw(self, amount: int) -> None:
        with self.lock:
            if self.status and amount > 0 and amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError(amount)

    def close(self) -> None:
        with self.lock:
            if self.status:
                self.status = False
                self.balance = 0
            else:
                raise ValueError(self)
