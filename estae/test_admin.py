import unittest
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate
from basic_user import Basic_User
from manager import Manager_User
from admin import Admin

rcpt = Receipt("25th December", 2000)
inv = Invoice("25th March", 1500, 0)
hhold = Household("Household 1 custodian", [inv], [rcpt])
ppty = Property("House", [hhold,hhold, hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
tfa = Thoroughfare("London", [ppty,ppty,ppty])
tfc = Thoroughfare("London", [ppty])
est = Estate("Estate1", "Philly", "Morocco", [tfa,tfc], [ppty], [hhold])
bau = Basic_User(est)
mgr = Manager_User(est, est)
adm = Admin(est, est, [est,est,est])

class TestAdmin(unittest.TestCase):

    def test_get_object_in_estate_list(self):
        self.assertEqual(adm.get_object_in_estate_list(0), est, "Incorrect value returned")

    def test_create_estate(self):
        adm.create_estate()
        self.assertEqual(len(adm.get_listOfEstate()), 2, "Incorrect value returned")

    def test_update_estate(self):
        adm.update_estate(0)
        self.assertEqual(adm.get_object_in_estate_list(0).get_name(), "Tester", "Incorrect value returned")

    def test_delete_estate(self):
        adm.delete_estate(0)
        self.assertEqual(len(adm.get_listOfEstate()), 2, "Incorrect value returned")

if __name__ == '__main__':
        unittest.main()

