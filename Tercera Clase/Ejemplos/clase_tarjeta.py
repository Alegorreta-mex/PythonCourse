class CreditCard():
    change_rate = 12.5

    def __init__(self, bank, card_holder_name: str, expiration_date: str, card_number: int, current_balance: float):
        self._bank = bank
        self._card_holder_name = card_holder_name
        self._expiration_date = expiration_date
        self._card_number = card_number
        self._is_activate = False
        self._current_balance = current_balance

    def __str__(self):
        return "".format(self._current_balance)

    def activate(self):
        self._is_activate = True
        return self._is_activate

    def paid(self):
        pass

    def deactivate(self):
        self._is_activate = False
        return self._is_activate

    def balance(self):
        return self._current_balance

    def payment(self, amount):
        self._current_balance = self._current_balance - amount

    def charge(self, amount):
        self._current_balance = self._current_balance + amount


# creamos un objeto de la clase

creditcard = CreditCard("HSBC", "Pedro Perez", "11/06", 1234567891234567,0)

creditcard.payment(100)
creditcard.charge(50)
print(creditcard)