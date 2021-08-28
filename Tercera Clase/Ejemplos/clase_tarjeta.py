class CreditCard():
    change_rate = 12.5

    def __init__(self, bank, card_holder_name: str, expiration_date: str, card_number: int):
        self._bank = bank
        self._card_holder_name = card_holder_name
        self._expiration_date = expiration_date
        self._card_number = card_number
        self._is_activate = False

    def activate(self):
        self._is_activate = True
        return self._is_activate

    def paid(self):
        pass

    def deactivate(self):
        self._is_activate = False
        return self._is_activate


# creamos un objeto de la clase

creditcard = CreditCard("HSBC", "Pedro Perez", "11/06", 1234567891234567)

# llamamos los tres metodos
print(creditcard.activate())
print(creditcard.deactivate())
print(creditcard.paid())