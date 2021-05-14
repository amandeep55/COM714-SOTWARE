from typing import List

class Invoice:

    def __init__(self, payment_date:str, total_value:int, amount_paid:int):
        self.__payment_date = payment_date
        self.__total_value = total_value
        self.__amount_paid = amount_paid
        self.__amount_remaining = self.__total_value - self.__amount_paid

    def get_full_details(self)-> None:
        print("Payment date is :" + self.get_payment_date())
        print("Total value is : £" + str(self.get_total_value()))
        print("Total amount paid is : £" + str(self.get_amount_paid()))

    def get_payment_date(self)->str:
        return self.__payment_date

    def get_total_value(self)->int:
        return self.__total_value

    def get_amount_paid(self)->int:
        return self.__amount_paid

    def get_amount_remaining(self)-> int:
        return self.__amount_remaining

    def set_payment_date(self, new_payment_date)->None:
        self.__payment_date = new_payment_date

    def set_total_value(self, new_total_value)->None:
        self.__total_value = new_total_value

    def add_amount_paid(self, add_amount_paid)->None:
        self.__amount_paid += add_amount_paid

    def set_amount_paid(self, new_amount_paid)->None:
        self.__amount_paid = new_amount_paid

    def set_amount_remaining(self)->None:
        self.__amount_remaining = self.get_total_value() - self.get_amount_paid()
