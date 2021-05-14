import unittest
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate

rcpt = Receipt("25th December", 2000)
inv = Invoice("25th March", 1500, 0)
hhold = Household("Household 1 custodian", [inv], [rcpt])
ppty = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
tfa = Thoroughfare("London", [ppty])
est = Estate("Estate1", "Philly", "Morocco", [tfa], [ppty], [hhold])

class TestEstate(unittest.TestCase):

    def test_get_number_thoroughfares(self):
        self.assertEqual(est.get_number_thoroughfares(), 1, "Incorrect value returned")

    def test_get_number_properties(self):
        self.assertEqual(est.get_number_properties(), 1, "Incorrect value returned")

    def test_get_object_in_thoroughfares_list(self):
        self.assertEqual(est.get_object_in_thoroughfares_list(0), tfa, "Incorrect value returned")

    def test_get_object_in_properties_list(self):
        self.assertEqual(est.get_object_in_properties_list(0), ppty, "Incorrect value returned")

    def test_get_object_in_households_list(self):
        self.assertEqual(est.get_object_in_households_list(0), hhold, "Incorrect value returned")

    def test_get_name(self):
        self.assertEqual(est.get_name(), "Estate1", "Incorrect value returned")

    def test_get_estate_manager(self):
        self.assertEqual(est.get_estate_manager(), "Philly", "Incorrect value returned")

    def test_get_location(self):
        self.assertEqual(est.get_location(), "Morocco", "Incorrect value returned")

    def test_create_thoroughfare(self):
        esta = Estate("Estate1", "Philly", "Morocco", [tfa], [ppty], [hhold])
        esta.create_thoroughfare("AAA", [])
        self.assertEqual(esta.get_number_thoroughfares(), 2, "Incorrect value returned")

    def test_create_thoroughfare_new(self):
        esta = Estate("Estate1", "Philly", "Morocco", [tfa], [ppty], [hhold])
        esta.create_thoroughfare_new("Tester")
        self.assertEqual(esta.get_number_thoroughfares(), 2, "Incorrect value returned")

    def test_get_thoroughfare(self):
        self.assertEqual(est.get_thoroughfare(0), tfa, "Incorrect value returned")

    def test_delete_thoroughfare(self):
        esta = Estate("Estate1", "Philly", "Morocco", [tfa,tfa], [ppty], [hhold])
        esta.delete_thoroughfare(0)
        self.assertEqual(esta.get_number_thoroughfares(), 1, "Incorrect value returned")

    def test_get_invoice_in_estate(self):
        esta = Estate("Estate1", "Philly", "Morocco", [tfa, tfa], [ppty], [hhold])
        self.assertEqual(esta.get_invoice_in_estate(0,0),inv,"Incorrect value returned")

    def test_get_total_invoice_for_estate_admin(self):
        esta = Estate("Estate1", "Philly", "Morocco", [tfa, tfa], [ppty], [hhold])
        self.assertEqual(esta.get_total_invoice_for_estate_admin(), 3000, "Incorrect value returned")





if __name__ == '__main__':
      unittest.main()