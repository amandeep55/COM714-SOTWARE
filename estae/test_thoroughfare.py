import unittest
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare

rcpt = Receipt("25th December", 2000)
inv = Invoice("25th March", 1500, 0)
hhold = Household("Household 1 custodian", [inv], [rcpt])
ppty = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
tfa = Thoroughfare("London", [ppty])

class TestThoroughfare(unittest.TestCase):

    def test_get_object_in_properties_list(self):
        self.assertEqual(tfa.get_object_in_properties_list(0), ppty, "Incorrect value returned")

    def test_get_name(self):
        self.assertEqual(tfa.get_name(), "London", "Incorrect value returned")

    def test_get_amount_properties(self):
        self.assertEqual(tfa.get_amount_properties(), 1, "Incorrect value returned")

    def test_set_name(self):
        rcpt = Receipt("25th December", 2000)
        inv = Invoice("25th March", 1500, 0)
        hhold = Household("Household 1 custodian", [inv], [rcpt])
        ppty = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        tfb = Thoroughfare("London", [ppty])
        tfb.set_name("Washington")
        self.assertEqual(tfb.get_name(), "Washington", "Incorrect value returned")

    #def test_create_property(self):
        #tfb = Thoroughfare("London", [ppty])
       # tfb.create_property()
       #self.assertEqual(tfb.get_amount_properties(), 2, "Incorrect value returned")

    #def test_create_property_new(self):
       # tfb = Thoroughfare("London", [ppty])
      #  tfb.create_property_new("1", [], "a", "a", "a", "a")
       # self.assertEqual(tfb.get_amount_properties(), 2, "Incorrect value returned")

    def test_get_property(self):
        self.assertEqual(tfa.get_property(0), ppty, "Incorrect value returned")

    def test_user_change_response(self):
        self.assertEqual(tfa.user_change_response(), 4, "Incorrect value returned")

    def test_delete_property(self):
        rcpt = Receipt("25th December", 2000)
        inv = Invoice("25th March", 1500, 0)
        hhold = Household("Household 1 custodian", [inv], [rcpt])
        ppty2 = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        tfb = Thoroughfare("London", [ppty,ppty2])
        tfb.delete_property(1)
        self.assertEqual(tfb.get_amount_properties(), 1, "Incorrect value returned")

    def test_delete_household(self):
        rcpt = Receipt("25th December", 2000)
        inv = Invoice("25th March", 1500, 0)
        hhold = Household("Household 1 custodian", [inv], [rcpt])
        hhold2 = Household("Household 2 custodian", [inv], [rcpt])
        ppty2 = Property("House", [hhold,hhold2], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
        tfb = Thoroughfare("London", [ppty, ppty2])
        tfb.delete_household(1,1)
        self.assertEqual(tfb.get_property(1).get_number_households(), 1, "Incorrect value returned")

    def test_total_value_invoices(self):
        self.assertEqual(tfa.total_value_invoices(), 1500, "Incorrect value returned")


if __name__ == '__main__':
      unittest.main()