import unittest
from receipt import Receipt


'''
    def __init__(self, payment_date:str, payment_amount:int):
        self.__payment_date = payment_date
        self.__payment_amount = payment_amount

    def get_payment_date(self) ->str:
        return self.__payment_date

    def get_payment_amount(self) ->int:
        return self.__payment_amount'''


class TestReceipt(unittest.TestCase):

    def test_get_payment_date(self):
        Test = Receipt("25th December 2021", 1000)
        self.assertEqual(Test.get_payment_date(), "25th December 2021", "Correct not date not given")

    def test_get_payment_amount(self):
        Test = Receipt("25th December 2021", 1000)
        self.assertEqual(Test.get_payment_amount(), 1000, "'1000' should return")


if __name__ == '__main__':
    unittest.main()