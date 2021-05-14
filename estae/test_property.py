import unittest
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property

rcpt = Receipt("25th December", 2000)
inv = Invoice("25th March", 1500, 0)
hhold = Household("Household 1 custodian", [inv], [rcpt])
ppty = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")

class TestProperty(unittest.TestCase):

    def test_get_object_in_household_list(self):
        self.assertEqual(ppty.get_object_in_household_list(0), hhold, "Incorrect object returned")

    def test_get_property_type(self):
        self.assertEqual(ppty.get_property_type(), "House", "Incorrect value returned")

    def test_get_number_households(self):
        self.assertEqual(ppty.get_number_households(), 1, "Incorrect value returned")

    def test_get_address(self):
        self.assertEqual(ppty.get_address(), "Buckingham Palace", "Incorrect value returned")

    def test_get_completion_date(self):
        self.assertEqual(ppty.get_completion_date(), "1st May", "Incorrect value returned")

    def test_get_management_type(self):
        self.assertEqual(ppty.get_management_type(), "Owned", "Incorrect value returned")

    def test_set_property_type(self):
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.set_property_type("Flat")
        self.assertEqual(ppty2.get_property_type(), "Flat", "Incorrect value returned")

    def test_set_address(self):
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.set_address("The White House")
        self.assertEqual(ppty2.get_address(), "The White House", "Incorrect value returned")

    def test_set_completion_date(self):
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.set_completion_date("1st March")
        self.assertEqual(ppty2.get_completion_date(), "1st March", "Incorrect value returned")

    def test_set_management_type(self):
        ppty.set_management_type("Rented")
        self.assertEqual(ppty.get_management_type(), "Rented", "Incorrect value returned")

    def test_create_household(self):
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.create_household()
        self.assertEqual(ppty2.get_number_households(), 2, "Incorrect value returned")

    def test_create_household_new(self):
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.create_household_new()
        self.assertEqual(ppty2.get_number_households(), 2, "Incorrect value returned")

    def test_add_household_to_occupied_by(self):
        rcpt = Receipt("25th December", 2000)
        inv = Invoice("25th March", 1500, 0)
        hhold2 = Household("Household 2 custodian", [inv], [rcpt])
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.add_household_to_occupied_by(hhold2)
        self.assertEqual(ppty2.get_number_households(), 2, "Incorrect value returned")

    def test_generate_invoice(self):
        rcpt = Receipt("25th December", 2000)
        inv = Invoice("25th March", 1500, 0)
        hhold2 = Household("Household 2 custodian", [inv], [rcpt])
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.generate_invoice(0, "1st March", 100, 50)
        self.assertEqual((len(ppty2.get_object_in_household_list(0).get_invoices())), 2, "Incorrect value returned")

    def test_delete_household_from_occupiedby_list(self):
        rcpt = Receipt("25th December", 2000)
        inv = Invoice("25th March", 1500, 0)
        hhold2 = Household("Household 2 custodian", [inv], [rcpt])
        ppty2 = Property("House", [hhold, hhold2], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        ppty2.delete_household_from_occupiedby_list(1)
        self.assertEqual(ppty2.get_number_households(), 1, "Incorrect value returned")

    def test_get_total_invoice(self):
        rcpt = Receipt("25th December", 2000)
        inv = Invoice("25th March", 1500, 0)
        hhold2 = Household("Household 2 custodian", [inv], [rcpt])
        ppty2 = Property("House", [hhold2], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        self.assertEqual(ppty2.get_total_invoice(), 1500, "Incorrect value returned")







if __name__ == '__main__':
      unittest.main()