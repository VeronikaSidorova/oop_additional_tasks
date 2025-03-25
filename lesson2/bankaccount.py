"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    balance: int

    def __init__(self, balance):
        self._balance = balance
        self._is_closed = False

    @property
    def balance(self):
        if self._is_closed:
            return 0
        return self._balance

    def deposit(self, amount):
        if self._is_closed:
            raise ValueError("Счет закрыт. Невозможно внести деньги.")
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self._balance += amount

    def withdraw(self, amount):
        if self._is_closed:
            raise ValueError("Счет закрыт. Невозможно снять деньги.")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете.")
        self._balance -= amount

    def close(self):
        if self._is_closed:
            raise ValueError("Счет уже закрыт.")
        self._is_closed = True
        return self._balance


# код для проверки 
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
