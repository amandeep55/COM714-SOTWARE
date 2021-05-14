from household import Household
from typing import List
from invoice import Invoice
from receipt import Receipt

class Property:

    def __init__(self, property_type:str, occupied_by:List[Household], address:str, owner:str, completion_date:str, management_type:str):

        self.__property_type = property_type
        self.__occupied_by = occupied_by
        self.__address = address
        self.__owner = owner
        self.__completion_date = completion_date
        self.__management_type = management_type

    def get_object_in_household_list(self,position:int)->Household:
        return self.__occupied_by[position]

    def get_property_type(self)->str:
        return self.__property_type

    def get_occupied_by(self)->str:
        return self.__occupied_by

    def get_number_households(self)->int:
        return len(self.__occupied_by)

    def get_address(self)->str:
        return self.__address

    def get_owner(self)->str:
        return self.__owner

    def get_completion_date(self)->str:
        return self.__completion_date

    def get_management_type(self)->str:
        return self.__management_type

    def set_property_type(self, new_type:str)->None:
        self.__property_type = new_type

    def set_address(self, new_address:str)->None:
        self.__address = new_address

    def set_owner(self, new_owner:str)->None:
        self.__owner.set_custodian(new_owner)

    def set_completion_date(self, new_completion_date:str)->None:
        self.__completion_date = new_completion_date

    def set_management_type(self, new_management_type:str)->None:
        self.__management_type = new_management_type

    def view_details(self)->None:
        print("Property type: " + self.get_property_type())
        for x in range(len(self.__occupied_by)):
            print("Occupied by: " + self.__occupied_by[x].get_custodian())
        print("Address: " + self.get_address())
        print("Owner: " + str(self.get_owner()))
        print(("Completion date: " + self.get_completion_date()))
        print("Management type: " + self.get_management_type())

################# basic user ################################

    def create_household(self)->None:
        custodian = input("Who is the custodian for the property?: ")
        new_household = Household(custodian, [], [])
        self.add_household_to_occupied_by(new_household)

    def create_household_new(self)->None:
        try:
            custodian = input("Who is the custodian for the household?: ")
            new_household = Household(custodian, [], [])
            self.add_household_to_occupied_by(new_household)

            amount_receipts_invoices = int(input("How many invoices and receipts do you have?: "))
            for x in range(amount_receipts_invoices):
                invoice = new_household.create_invoice_new()
                receipt = new_household.create_receipt_new()
                new_household.add_receipt_and_invoice_new(receipt, invoice)
        except:
            print("Ensure amount of invoices and receipts is an integer value only")

    def add_household_to_occupied_by(self, new_household:Household)->None:
        self.__occupied_by.append(new_household)

    def view_household(self, position:int)->None:
        print("Household custodian is " + self.__occupied_by[position].get_custodian())

    def update_household(self, position:int, new_custodian: str)->None:
        self.__occupied_by[position].set_custodian(new_custodian)

    def generate_invoice(self,position:int, payment_date:str, total_value:int, amount_paid:int)->None:
        self.__occupied_by[position].create_invoice(payment_date, total_value, amount_paid)

    def take_payment(self, payment_date:str, amount_to_pay:int, invoice_to_pay:Invoice)->None:
        self.__owner.take_payment_generate_receipt(payment_date, amount_to_pay, invoice_to_pay)

#### manager user #####

    def delete_household_from_occupiedby_list(self, position:int)->None:
        self.__occupied_by.pop(position)

    def get_total_invoice(self)->int:
        total_value = 0
        for household in self.__occupied_by:
            total_value = total_value + household.get_invoices_value()
        return total_value
