from property import Property
from typing import List
from household import Household

class Thoroughfare:

    def __init__(self, name: str, properties: List[Property]):
        self.__name = name
        self.__properties = properties

    def get_object_in_properties_list(self,position:int)->Property:
        return self.__properties[position]

    def get_name(self) ->str:
        return self.__name

    def get_properties(self)-> Property:
        return self.__properties

    def get_amount_properties(self)->int:
        return len(self.__properties)

    def set_name(self, new_name:str)->None:
        self.__name = new_name

############### basic system user methods ###################

    def view_details(self)->None:
       print(self.get_name() + " contains " + str(self.get_amount_properties()) + " properties")
       print("\n")
       for address in self.__properties:
           address.view_details()

    def create_property(self)->None:
        property_type = input("What is the property type?: ")
        occupied_by = []
        address = input("What is the address?: ")
        owner = []
        completion_date = input("What is the completion date?: ")
        management_type = input("What is the management type?: ")
        new_property = Property(property_type, occupied_by, address, owner, completion_date, management_type)
        self.add_property(new_property)

    def create_property_new(self, property_type:str, occupied_by:List[Household], address:str, owner:str, completion_date:str, management_type:str)->Property:
        new_property = Property(property_type, occupied_by, address, owner, completion_date, management_type)
        self.add_property(new_property)
        return new_property

    def get_property(self,position:int)->Property:
        return self.__properties[position]

    def add_property(self, property:Property)->None:
        self.__properties.append(property)

    def view_property(self, position: int)->None:
        self.__properties[position].view_details()

    def update_property_new(self, p_position:int)->None:
        try:
            choicePair = {1:self.get_property(p_position).set_property_type,
                          3:self.get_property(p_position).set_address,
                          4:self.get_property(p_position).set_owner,
                          5:self.get_property(p_position).set_completion_date,
                          6:self.get_property(p_position).set_management_type}
            value = self.user_change_response()
            amended_value = input("What value should this be changed to?: ")
            choicePair[value](amended_value)
        except:
            print("Value could not be changed")

    def user_change_response(self)->int:
        try:
            choice = int(input
                             ("Enter 1 to change property type \n "
                              "Enter 3 to change address \n "
                              "Enter 4 to change owner / custodian \n "
                              "Enter 5 to change completion date \n "
                              "Enter 6 to change management type \n "
                              "Enter here : "
                              ))
            return choice
        except:
            print("Value entered was not valid")

###################Manager methods#############################

    def delete_property(self, position:int):
        self.__properties.pop(position)

    def delete_household(self, property_pos:int, household_position:int):
        self.__properties[property_pos].delete_household_from_occupiedby_list(household_position)

    def total_value_invoices(self)->int:
        total_value = 0
        for x in self.__properties:
            total_value = total_value + x.get_total_invoice()
        return total_value




