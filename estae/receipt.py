from typing import List

class Receipt:

    def __init__(self, payment_date:str, payment_amount:int):
        self.__payment_date = payment_date
        self.__payment_amount = payment_amount

    def get_payment_date(self) ->str:
        return self.__payment_date

    def get_payment_amount(self) ->int:
        return self.__payment_amount