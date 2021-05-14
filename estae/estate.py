from typing import List
from invoice import Invoice
from thoroughfare import Thoroughfare
from property import Property
from household import Household

class Estate:

    def __init__(self, name: str, estate_manager: str, location:str, thoroughfares:List[Thoroughfare],
                 properties:List[Property], households:List[Household]):
        self.__name = name
        self.__estate_manager = estate_manager
        self.__location = location
        self.__throughfares = thoroughfares
        self.__properties = properties
        self.__households = households

    def get_households(self)->Household:
        return self.__households

    def get_number_thoroughfares(self)->int:
        return len(self.__throughfares)

    def get_number_properties(self)->int:
        return len(self.__properties)

    def get_number_households(self)->int:
        return len(self.__households)

    def get_object_in_thoroughfares_list(self, position:int)->Thoroughfare:
        return self.__throughfares[position]

    def get_object_in_properties_list(self, position:int)->Property:
        return self.__properties[position]

    def get_object_in_households_list(self, position:int)->Household:
        return self.__households[position]

    def get_name(self) ->str:
        return self.__name

    def get_estate_manager(self) ->str:
        return self.__estate_manager

    def get_location(self) ->str:
        return self.__location

    def get_thoroughfares(self)->Thoroughfare:
        return self.__thoroughfares

    def get_properties(self)->Property:
        return self.__properties

    def set_name(self, new_name:str)->None:
        self.__name = new_name

    def set_estate_manager(self, new_manager:str)->None:
        self.__estate_manager = new_manager

    def set_location(self, new_location:str)->None:
        self.__location = new_location

    def add_property(self, new_property:Property)->None:
        self.__properties.append(new_property)

    #################### basic system user methods ###################################
    def create_thoroughfare(self, name, property:List[Property])->None:
        TF = Thoroughfare(name, property)
        self.add_thoroughfare(TF)

    def create_thoroughfare_new(self, name:str)->Thoroughfare:
        TF = Thoroughfare(name, [])
        self.add_thoroughfare(TF)
        return TF

    def add_thoroughfare(self, new_thoroughfare:Thoroughfare)->None:
        self.__throughfares.append(new_thoroughfare)

    def view_thoroughfare(self, position:int)->None:
        self.__throughfares[position].view_details()

    def get_thoroughfare(self, position:int)->Thoroughfare:
        return self.__throughfares[position]

    def view_all_thoroughfares(self)->None:
        for thoroughfare in self.__throughfares:
            print("Thoroughname is :" + thoroughfare.get_name())
            print()

    #################### Manager user methods #########################################

    def delete_thoroughfare(self, position:int)->None:
        self.__throughfares.pop(position)

    def get_total_invoice_for_estate_manager(self)->None:
        total_value = 0
        for x in self.__throughfares:
            total_value = total_value + x.total_value_invoices()
        print("The total value of invoices in this estate is £" + str(total_value))

    ##### admin methods #####

    def view_details_estate(self)->None:
        print("Estate name is " + self.get_name())
        print("Estate is managed by " + self.get_estate_manager())
        print("Estate location is " + self.get_location())
        print("There are " + str(self.get_number_thoroughfares()) + " thoroughfares within this estate")
        print("There are " + str(self.get_number_properties()) + " properties within this estate")
        print("There are " + str(self.get_number_households()) + " households within this estate")

    def get_invoice_in_estate(self,h_position:int, i_position:int)->Invoice:
        return self.__households[h_position].get_object_in_invoiceList(i_position)

    def get_total_invoice_for_estate_admin(self)->int:
        total_value = 0
        for x in self.__throughfares:
            total_value = total_value + x.total_value_invoices()
        return total_value
