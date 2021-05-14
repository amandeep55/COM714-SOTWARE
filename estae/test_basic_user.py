import unittest
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate
from basic_user import Basic_User

rcpt = Receipt("25th December", 2000)
inv = Invoice("25th March", 1500, 0)
hhold = Household("Household 1 custodian", [inv], [rcpt])
ppty = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
tfa = Thoroughfare("London", [ppty])
est = Estate("Estate1", "Philly", "Morocco", [tfa], [ppty], [hhold])
bau = Basic_User(est)

class TestBasicUser(unittest.TestCase):

    def test_create_thoroughfare(self):
        bau.create_thoroughfare()
        self.assertEqual(bau.get_estate().get_number_thoroughfares(),2,"Incorrect value returned")

    def test_update_thoroughfare(self):
        bau.update_thoroughfare(0)
        self.assertEqual(bau.get_estate().get_thoroughfare(0).get_name(), "Sandwich", "Incorrect value returned")

    def test_create_property(self):
       bau.create_property(0)
       self.assertEqual(bau.get_estate().get_thoroughfare(0).get_amount_properties(), 2, "Incorrect value returned")

    def test_update_property(self):
        bau.update_property(0,0)
        self.assertEqual(bau.get_estate().get_thoroughfare(0).get_property(0).get_property_type(), "tester", "Incorrect value returned")

    def test_generate_invoice_specific_household(self):
       bau.generate_invoice_specific_household(0,0,0)
       self.assertEqual(bau.get_estate().get_thoroughfare(0).get_property(0).get_object_in_household_list(0).get_object_in_invoiceList(1).get_payment_date(), "lll", "Incorrect value returned")

    def test_take_payment_generate_receipt(self):
        bau.take_payment_generate_receipt(0,0,0)
        self.assertEqual(bau.get_estate().get_thoroughfare(0).get_property(0).get_object_in_household_list(0).get_object_in_receiptsList(1).get_payment_date(), "lll")


if __name__ == '__main__':
        unittest.main()