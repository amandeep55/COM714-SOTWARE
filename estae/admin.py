from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate
from basic_user import Basic_User
from manager import Manager_User
from typing import List

class Admin(Manager_User):
    def __init__(self,estate:Estate, estateInChargeOf:Estate, listOfEstate:List[Estate]):
        Manager_User.__init__(self,estate, estateInChargeOf)
        self.__listOfEstate = listOfEstate

### 3i ####

    def get_listOfEstate(self):
        return self.__listOfEstate

    def get_object_in_estate_list(self, position):
        return self.__listOfEstate[position]

    def create_estate(self)->Estate:
        name = input("What is the name of the estate?: ")
        estate_manager = input("What is the name of the estate manager?: ")
        location = input("What is the location of the estate?: ")
        new_estate = Estate(name, estate_manager, location, [], [], [])
        self.__listOfEstate.append(new_estate)
        return new_estate

    def view_estate(self,position:int)->None:
        self.__listOfEstate[position].view_details_estate()

    def update_estate(self, position:int)->None:
        new_name = input("What is the name of the estate? ")
        new_estate_manager = input("What is the name of the estate manager? ")
        new_location = input("What is the location? ")
        self.__listOfEstate[position].set_name(new_name)
        self.__listOfEstate[position].set_estate_manager(new_estate_manager)
        self.__listOfEstate[position].set_location(new_location)

    def delete_estate(self, position:int)->None:
        self.__listOfEstate.pop(position)

### 3ii ###

    def view_estate_invoice(self, e_position:int, h_position:int, i_position:int)->None:
        self.__listOfEstate[e_position].get_invoice_in_estate(h_position,i_position).get_full_details()

    def update_estate_invoices(self,e_position:int,tf_position:int,property_position:int,h_position:int,i_position:int)->None:
        try:
            new_payment_date = input("What is the payment date?: ")
            new_total_value = int(input("What is the total value?: "))
            new_amount_paid = int(input("What is the amount paid?: "))

            self.__listOfEstate[e_position].get_thoroughfare(tf_position).get_property(property_position).get_object_in_household_list(h_position).get_object_in_invoiceList(i_position).set_payment_date(new_payment_date)
            self.__listOfEstate[e_position].get_thoroughfare(tf_position).get_property(
                property_position).get_object_in_household_list(h_position).get_object_in_invoiceList(i_position).set_total_value(new_total_value)
            self.__listOfEstate[e_position].get_thoroughfare(tf_position).get_property(
                property_position).get_object_in_household_list(h_position).get_object_in_invoiceList(i_position).set_amount_paid(new_amount_paid)
            self.__listOfEstate[e_position].get_thoroughfare(tf_position).get_property(
                property_position).get_object_in_household_list(h_position).get_object_in_invoiceList(i_position).set_amount_remaining()
        except:
            print("Please ensure total value and amount paid are integer entries")

    def delete_estate_invoices(self,e_position:int, h_position:int, i_position:int)->None:
        self.__listOfEstate[e_position].get_object_in_households_list(h_position).remove_invoice(i_position)

### 3iii ###

    def calculate_total_invoice_in_system(self)->None:
        totalValue =0
        for est in self.__listOfEstate:
                    totalValue = totalValue + est.get_total_invoice_for_estate_admin()
        print("The total value of invoices in all estates is £" + str(totalValue))













