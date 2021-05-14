from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate
from basic_user import Basic_User
from manager import Manager_User
from admin import Admin
from typing import List

class DB():

    rcpt = Receipt("25th December", 2000)
    inv = Invoice("25th March", 1500, 0)
    inv2 =  Invoice("1st Jan", 5000, 0)
    inv3 = Invoice("1st December", 200, 0)
    hhold = Household("Household 1 custodian", [inv], [rcpt])
    hhold2 = Household("Household 2 custodian", [inv2], [rcpt])
    hhold3 = Household("Household 3 custodian", [inv3], [rcpt])

    ppty = Property("House", [hhold], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
    ppty2 = Property("House", [hhold2], "Buckingham Palace", "DB CLASS", "1st May", "Owned")
    ppty3 = Property("House", [hhold3], "Buckingham Palace", "DB CLASS", "1st May", "Owned")

    tfa = Thoroughfare("London", [ppty])
    tfc = Thoroughfare("Zimbabewe", [ppty2])
    tfd = Thoroughfare("Piccadilly",[ppty3] )

    est = Estate("Estate1", "Philly", "Morocco", [tfa,tfc,tfd], [ppty], [hhold])

    bau = Basic_User(est)
    mgr = Manager_User(est, est)
    adm = Admin(est, est, [est])



