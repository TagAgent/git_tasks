class Person:
    def __init__(self, name_pm: str, language_pm: str):
        self.name = name_pm
        self.language = language_pm

    def introduce(self):
        """Это метод для самопредставления объекта Person"""
        if self.language == "ru":
            print(f"Привет меня зовут {self.name}")
        elif self.language == "kg":
            print(f"Салам менин атым {self.name}")
        else:
            print(f"Hello my name's {self.name}")

class BankAccount(Person):
    def __init__(self, name_pm: str, language_pm: str, account_number_pm: str, balance_pm: float):
        self.name = name_pm
        self.language = language_pm
        self.account_number = account_number_pm
        self.__balance = balance_pm

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, new_balance: float) -> None:
        if new_balance >= 0:
            self.__balance = new_balance

    def deposit(self, amount: float) -> None:
        """Это метод для внесения денег на счет"""
        new_balance = self.get_balance()
        if amount > 0.0:
            new_balance += amount
        self.set_balance(new_balance)

    def withdraw(self, amount: float):
        """Это метод для внесения денег на счет"""
        new_balance = self.get_balance()
        if amount < self.get_balance():
            new_balance -= amount
            self.set_balance(new_balance)
            return amount
