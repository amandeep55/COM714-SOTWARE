import basic_user
from estate import Estate
from basic_user import Basic_User
from thoroughfare import Thoroughfare
from property import Property
from household import Household
from receipt import Receipt
from invoice import Invoice
from typing import List

class Manager_User(Basic_User):
    def __init__(self,estate:Estate, estateInChargeOf:Estate):
        Basic_User.__init__(self,estate)
        self.__estateInChargeOf = estateInChargeOf

    def get_estateInChargeOf(self):
        return self.__estateInChargeOf

#### 2i ####

    def delete_tf(self, tf_position:int)->None:
        self.get_estate().delete_thoroughfare(tf_position)

    def delete_prop(self, tf_position:int, p_position:int)->None:
        self.get_estate().get_thoroughfare(tf_position).delete_property(p_position)

    def delete_household(self,tf_position:int, p_position:int, h_position:int)->None:
        self.get_estate().get_thoroughfare(tf_position).get_property(p_position).delete_household_from_occupiedby_list(h_position)

### 2ii ###

    def create_basic_user(self)->Basic_User:
        new_basic_user = Basic_User(self.get_estateInChargeOf())
        print("New user created, in charge of estate " + self.get_estateInChargeOf().get_name())
        return new_basic_user

### 2iii ###

    def get_total_invoice_estate(self):
        self.get_estate().get_total_invoice_for_estate_manager()

























