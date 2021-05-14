import unittest
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate
from basic_user import Basic_User
from manager import Manager_User

rcpt = Receipt("25th December", 2000)
inv = Invoice("25th March", 1500, 0)
hhold = Household("Household 1 custodian", [inv], [rcpt])
ppty = Property("House", [hhold,hhold, hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
tfa = Thoroughfare("London", [ppty,ppty,ppty])
tfc = Thoroughfare("London", [ppty])
est = Estate("Estate1", "Philly", "Morocco", [tfa,tfc], [ppty], [hhold])
bau = Basic_User(est)
mgr = Manager_User(est, est)

class TestManager(unittest.TestCase):

    def test_delete_tf(self):
        mgr.delete_tf(1)
        self.assertEqual(mgr.get_estate().get_number_thoroughfares(), 1, "Incorrect value returned")

    def test_delete_prop(self):
        mgr.delete_prop(0,0)
        self.assertEqual(mgr.get_estate().get_thoroughfare(0).get_amount_properties(),2, "Incorrect value returned")

    def test_delete_household(self):
        mgr.delete_household(0,0,0)
        self.assertEqual(mgr.get_estate().get_thoroughfare(0).get_property(0).get_number_households(), 2, "Incorrect value returned")

    def test_create_basic_user(self):
        tester = mgr.create_basic_user()
        self.assertEqual(tester.get_estate().get_name(), "Estate1", "Incorrect value returned")

if __name__ == '__main__':
       unittest.main()