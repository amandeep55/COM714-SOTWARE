import unittest
from invoice import Invoice

class TestInvoice(unittest.TestCase):


    def test_get_payment_date(self):
        Tester = Invoice("1st March 2020", 0, 0)
        self.assertEqual(Tester.get_payment_date(), "1st March 2020", "Incorrect date returned")

    def test_get_total_value(self):
        Tester = Invoice("1st March 2020", 1000, 0)
        self.assertEqual(Tester.get_total_value(), 1000, "Incorrect value returned")

    def test_get_amount_paid(self):
        Tester = Invoice("1st March 2020", 1000, 500)
        self.assertEqual(Tester.get_amount_paid(), 500, "Incorrect value returned")

    def test_get_amount_remaining(self):
        Tester = Invoice("1st March 2020", 1000, 250)
        self.assertEqual(Tester.get_amount_remaining(), 750, "Incorrect value returned")

    def test_set_payment_date(self):
        Tester = Invoice("1st March 2020", 1000, 250)
        Tester.set_payment_date("1st December 2021")
        self.assertEqual(Tester.get_payment_date(), "1st December 2021", "Incorrect date returned")

    def test_set_total_value(self):
        Tester = Invoice("1st March 2020", 1000, 250)
        Tester.set_total_value(2000)
        self.assertEqual(Tester.get_total_value(), 2000, "Incorrect value returned")

    def test_add_amount_paid(self):
        Tester = Invoice("1st March 2020", 1000, 250)
        Tester.add_amount_paid(100)
        self.assertEqual(Tester.get_amount_paid(), 350, "Incorrect value returned")

    def test_set_amount_paid(self):
        Tester = Invoice("1st March 2020", 1000, 250)
        Tester.set_amount_paid(100)
        self.assertEqual(Tester.get_amount_paid(), 100, "Incorrect value returned")

    def set_amount_remaining(self):
        Tester = Invoice("1st March 2020", 1000, 250)
        Tester.set_amount_paid(100)
        Tester.set_amount_remaining()
        self.assertEqual(Tester.get_amount_remaining(), 900, "Incorrect value returned")

if __name__ == '__main__':
    unittest.main()