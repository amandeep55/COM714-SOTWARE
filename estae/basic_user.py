from estate import Estate
from thoroughfare import Thoroughfare
from property import Property
from household import Household
from receipt import Receipt
from invoice import Invoice
from typing import List

class Basic_User:

    def __init__(self, estate:Estate):
        self.__estate = estate

    def get_estate(self) ->Estate:
        return self.__estate

### 1i ####
    def create_thoroughfare(self)->None:
        name = input("What is the name of the thoroughfare?: ")
        self.get_estate().create_thoroughfare(name, [])

    def view_thoroughfare(self, position:int)->Thoroughfare:
        self.get_estate().view_thoroughfare(position)

    def update_thoroughfare(self, position:int)->None:
        new_name = input("Enter updated thoroughfare name: ")
        self.get_estate().get_thoroughfare(position).set_name(new_name)

    def create_full_thoroughfare(self)->None:
        try:
            name_tf = input("What is the name of this thoroughfare?: ")
            TF = self.get_estate().create_thoroughfare_new(name_tf)
            amount_properties = int(input("How much properties would you like to add?: "))
            for x in range (amount_properties):
                print("Entering details for property number " + str(x+1))
                prop_type = input("What is the property type? :")
                address = input("What is the address?: ")
                completion_date = input("What is the completion date?: ")
                mgmt_type = input("What is the management type?: ")
                owner = input("Who is the custodian of the property?: ")

                Prop = TF.create_property_new(prop_type, [], address, owner, completion_date, mgmt_type)

                amount_households = int(input("How many households are in the property?: "))
                for x in range (amount_households):
                    print("Entering details for household: " +str(x+1))
                    Prop.create_household_new()
        except:
            print("Please ensure that the number of properties and households is an integer entry only.")


### 1ii ###

    def create_property(self, position:int)->None:
        self.get_estate().get_thoroughfare(position).create_property()

    def view_property(self, tf_position:int, p_position:int)->None:
        self.get_estate().get_thoroughfare(tf_position).view_property(p_position)

    def update_property(self, tf_position:int, p_position:int)->None:
        self.get_estate().get_thoroughfare(tf_position).update_property_new(p_position)

    def create_full_property(self, tf_position:int)->None:
        try:
            TF = self.get_estate().get_thoroughfare(tf_position)
            amount_properties = int(input("How many properties would you like to add?: "))
            for x in range (amount_properties):
                    print("Entering details for property number " + str(x+1))
                    prop_type = input("What is the property type? :")
                    address = input("What is the address?: ")
                    completion_date = input("What is the completion date?: ")
                    mgmt_type = input("What is the management type?: ")
                    owner = input("Who is the custodian of the property?: ")

                    Prop = TF.create_property_new(prop_type, [], address, owner, completion_date, mgmt_type)

                    amount_households = int(input("How many households are in the property?: "))
                    for x in range (amount_households):
                        print("Entering details for household: " +str(x+1))
                        Prop.create_household_new()
        except:
            print("Please ensure that the number of properties and households is an integer entry only.")

### 1iii ###

    def create_household(self, tf_position:int, p_position:int)->None:
        self.get_estate().get_thoroughfare(tf_position).get_property(p_position).create_household()

    def view_household(self, tf_position:int, p_position:int, h_position:int)->None:
        self.get_estate().get_thoroughfare(tf_position).get_property(p_position).view_household(h_position)

    def update_household(self,tf_position:int, p_position:int, h_position:int)->None:
        new_name = input("What is the name of the custodian?: ")
        self.get_estate().get_thoroughfare(tf_position).get_property(p_position).get_object_in_household_list(h_position).set_custodian(new_name)

    def create_full_household(self, tf_position:int, property_position:int)->None:

        try:
            Prop = self.get_estate().get_thoroughfare(tf_position).get_property(property_position)
            amount_households = int(input("How many households would you like to add?: "))
            for x in range(amount_households):
                print("Entering details for household: " + str(x + 1))
                Prop.create_household_new()
        except:
            print("Please ensure that the number of properties and households is an integer entry only.")

### 1iv ####

    def generate_invoice_specific_household(self,tf_position:int, p_position:int, h_position:int)->None:
        try:
            payment_date = input("What is the payment date?: ")
            total_value = int(input("What is the total value of the invoice?: "))
            amount_paid = int(input("What is the payment being made today?: "))
            self.get_estate().get_thoroughfare(tf_position).get_property(p_position).get_object_in_household_list(
                h_position).create_invoice(payment_date,total_value,amount_paid)
        except:
            print("Please ensure total_value and amount_paid are both integer entries")

### 1v ###

    def take_payment_generate_receipt(self,tf_position:int, p_position:int, h_position:int)->None:
        try:
            invoice_position = int(input("What is the position of the invoice?: "))
            payment_date = input("What is the payment date?: ")
            amount_paid = int(input("What is the payment being made today?: "))
            self.get_estate().get_thoroughfare(tf_position).get_property(p_position).get_object_in_household_list(
                h_position).take_payment_generate_receipt(payment_date, amount_paid,invoice_position)
        except:
            print("Please ensure amount paid is an integer value")

### 1vi ###

    def print_invoices_and_receipts_for_household(self,tf_position:int, p_position:int, h_position:int):
        self.get_estate().get_thoroughfare(tf_position).get_property(p_position).get_object_in_household_list(
            h_position).print_invoices()
        self.get_estate().get_thoroughfare(tf_position).get_property(p_position).get_object_in_household_list(
            h_position).print_receipts()

