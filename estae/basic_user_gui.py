from tkinter import *
from tkinter import messagebox
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate
from basic_user import Basic_User
from db import DB


class Basic_User_Gui(Tk, DB):

    # initialise window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.space = Label()
        self.title("Basic User Gui")
        self.configure(bg="#c68400")

        self.add_go_back_btn()
        self.add_level_Label()

        self.add_enterPositionTF_Label()
        self.add_enterPositionTF_entry_box()
        self.add_createTF_btn()
        self.add_create_full_TF_btn()
        self.add_updateTF_btn()
        self.add_viewTF_btn()

        self.add_createProperty_btn()
        self.create_full_property_btn()
        self.add_updateProperty_btn()
        self.add_viewProperty_btn()

        self.add_createHousehold_btn()
        self.add_create_full_household_btn()
        self.update_Household_btn()
        self.add_view_Household_btn()

        self.add_enterPositionProp_Label()
        self.add_enterPositionProp_entry_box()

        self.add_enterPositionHousehold_Label()
        self.add_enterPositionHousehold_entry_box()

        self.add_createPayment_receipt_btn()
        self.add_createInvoice_btn()
        self.receipts_household_btn()

    def add_go_back_btn(self) -> None:
        self.add_go_back_btn = Button()
        self.add_go_back_btn.grid(row=0, column=3)
        self.add_go_back_btn.configure(font="Arial 12", text="Exit", borderwidth=2, relief="groove", bg="#000a12",
                                       fg="white")
        self.add_go_back_btn.bind("<ButtonRelease-1>", self.add_go_back_btn_clicked)

    def add_go_back_btn_clicked(self, event) -> None:
        self.destroy()

    def add_level_Label(self) -> None:
        self.add_level_label = Label()
        self.add_level_label.grid(row=0, column=1)
        self.add_level_label.configure(font="Arial 22", text="Basic User", borderwidth=2, relief="groove", bg="#000a12",
                                       fg="white")

    #### create, update, view TF ####

    def add_enterPositionTF_Label(self) -> None:
        self.add_enterPositionTF_Label = Label()
        self.add_enterPositionTF_Label.grid(row=1, column=0, pady=(20,0))
        self.add_enterPositionTF_Label.configure(font="Arial 12", text="Enter position of Thoroughfare")

    def add_enterPositionTF_entry_box(self) -> None:
        self.add_enterPositionTF_entry_box = Entry()
        self.add_enterPositionTF_entry_box.grid(row=1, column=1, pady=(20,0))

    def add_createTF_btn(self) -> None:
        self.createTF_btn = Button()

        self.createTF_btn.configure(font="Arial 12",
                                    text="Create empty Thoroughfare")
        self.createTF_btn.grid(row=4, column=0 ,pady=(50,0))
        self.createTF_btn.bind("<ButtonRelease-1>", self.createTF_btn_clicked)

    def add_create_full_TF_btn(self) -> None:
        self.add_create_full_TF_btn = Button()
        self.add_create_full_TF_btn.grid(row=4, column=1, padx=(40,0), pady=(50,0))
        self.add_create_full_TF_btn.configure(font="Arial 12",
                                              text="Create full Thoroughfare")
        self.add_create_full_TF_btn.bind("<ButtonRelease-1>", self.add_create_full_TF_btn_clicked)

    def add_create_full_TF_btn_clicked(self, event) -> None:
        DB.bau.create_full_thoroughfare()
        messagebox.showinfo("Complete", "Thoroughfare Created!")

    def createTF_btn_clicked(self, event) -> None:

        DB.bau.create_thoroughfare()
        messagebox.showinfo("Complete", "Thoroughfare Created!")

    def add_updateTF_btn(self) -> None:
        self.updateTF_btn = Button()
        self.updateTF_btn.grid(row=7, column=0, pady=(50,0))
        self.updateTF_btn.configure(font="Arial 12",
                                    text="Update Thoroughfare")
        self.updateTF_btn.bind("<ButtonRelease-1>", self.updateTF_btn_clicked)

    def updateTF_btn_clicked(self, event) -> None:

        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            DB.bau.update_thoroughfare(tf_position)
            messagebox.showinfo("Complete", "Thoroughfare Updated")
        except:
            print("Thoroughfare position entry is not compatible")

    def add_viewTF_btn(self) -> None:
        self.viewTF_btn = Button()
        self.viewTF_btn.grid(row=7, column=1, pady=(50,0))
        self.viewTF_btn.configure(font="Arial 12",
                                  text="View Thoroughfare")
        self.viewTF_btn.bind("<ButtonRelease-1>", self.viewTF_btn_clicked)

    def viewTF_btn_clicked(self, event) -> None:
        try:
            position = int(self.add_enterPositionTF_entry_box.get())
            DB.bau.view_thoroughfare(position)
        except:
            print("Thoroughfare position entry is not compatible")

    ### create, update, view property

    def add_createProperty_btn(self) -> None:
        self.createProperty_btn = Button()
        self.createProperty_btn.grid(row=5, column=0)
        self.createProperty_btn.configure(font="Arial 12",
                                          text="Create empty Property")
        self.createProperty_btn.bind("<ButtonRelease-1>", self.createProperty_btn_clicked)

    def createProperty_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            DB.bau.create_property(tf_position)
            messagebox.showinfo("Complete", "Property was created")
        except:
            print("Thoroughfare position entry is not compatible")

    def create_full_property_btn(self) -> None:
        self.create_full_property_btn = Button()
        self.create_full_property_btn.grid(row=5, column=1, padx=(40,0))
        self.create_full_property_btn.configure(font="Arial 12", text="Create Full Property")
        self.create_full_property_btn.bind("<ButtonRelease-1>", self.create_full_property_btn_clicked)

    def create_full_property_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            DB.bau.create_full_property(tf_position)
            messagebox.showinfo("Complete", "Property Created!")
        except:
            messagebox.showinfo("Error", "Thorough position is not viable.")

    def add_updateProperty_btn(self) -> None:
        self.updateProperty_btn = Button()
        self.updateProperty_btn.grid(row=8, column=0)
        self.updateProperty_btn.configure(font="Arial 12",
                                          text="Update Property")
        self.updateProperty_btn.bind("<ButtonRelease-1>", self.updateProperty_btn_clicked)

    def updateProperty_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            p_position = int(self.add_enterPositionProp_entry_box.get())
            DB.bau.update_property(tf_position, p_position)
            messagebox.showinfo("Complete", "Property updated ")
        except:
            print("Please check thoroughfare and property position entries are valid.")

    def add_viewProperty_btn(self) -> None:
        # works
        self.viewProperty_btn = Button()
        self.viewProperty_btn.grid(row=8, column=1)
        self.viewProperty_btn.configure(font="Arial 12",
                                        text="View Property")
        self.viewProperty_btn.bind("<ButtonRelease-1>", self.viewProperty_btn_clicked)

    def viewProperty_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            prop_position = int(self.add_enterPositionProp_entry_box.get())
            DB.bau.view_property(tf_position, prop_position)
            messagebox.showinfo("Complete", "Property details found")
        except:
            print("Position entry is not compatible")
            print("Please check thoroughfare and property position entries are valid.")

    ###Create, update, view household ###

    def add_createHousehold_btn(self) -> None:
        self.createHousehold_btn = Button()
        self.createHousehold_btn.grid(row=6, column=0)
        self.createHousehold_btn.configure(font="Arial 12",
                                           text="Create empty Household")
        self.createHousehold_btn.bind("<ButtonRelease-1>", self.createHousehold_btn_clicked)

    def add_create_full_household_btn(self) -> None:
        self.add_create_full_household_btn = Button()
        self.add_create_full_household_btn.grid(row=6, column=1, padx=(40,0))
        self.add_create_full_household_btn.configure(font="Arial 12",
                                                     text="Create Full Household")
        self.add_create_full_household_btn.bind("<ButtonRelease-1>", self.add_create_full_household_btn_clicked)

    def add_create_full_household_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            p_position = int(self.add_enterPositionProp_entry_box.get())
            DB.bau.create_full_household(tf_position, p_position)
            messagebox.showinfo("Complete", "Household created!")
        except:
            messagebox.showinfo("Error", "Please check thoroughfare and property position entries.")

    def createHousehold_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            prop_position = int(self.add_enterPositionProp_entry_box.get())
            DB.bau.create_household(tf_position, prop_position)
            messagebox.showinfo("Complete", "Household created")
        except:
            print("Position entry is not compatible")
            print("Please check thoroughfare and property position entries are valid.")

    def update_Household_btn(self) -> None:
        self.view_Household_btn = Button()
        self.view_Household_btn.grid(row=9, column=0)
        self.view_Household_btn.configure(font="Arial 12", text="Update Household")
        self.view_Household_btn.bind("<ButtonRelease-1>", self.update_Household_btn_clicked)

    def update_Household_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            prop_position = int(self.add_enterPositionProp_entry_box.get())
            h_position = int(self.add_enterPositionHousehold_entry_box.get())
            DB.bau.update_household(tf_position, prop_position, h_position)
            messagebox.showinfo("Complete", "Household updated ")
        except:
            print("Position entry is not compatible")
            print("Please check thoroughfare, property and household position entries are valid.")

    def add_view_Household_btn(self) -> None:
        self.view_Household_btn = Button()
        self.view_Household_btn.grid(row=9, column=1)
        self.view_Household_btn.configure(font="Arial 12", text="View Household")
        self.view_Household_btn.bind("<ButtonRelease-1>", self.view_Household_btn_clicked)

    def view_Household_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            prop_position = int(self.add_enterPositionProp_entry_box.get())
            h_position = int(self.add_enterPositionHousehold_entry_box.get())
            DB.bau.view_household(tf_position, prop_position, h_position)
            messagebox.showinfo("Household", "Household found!")
        except:
            print("Position entry is not compatible")
            print("Please check thoroughfare, property and household position entries are valid.")

    ### enter position of property ###
    def add_enterPositionProp_Label(self) -> None:
        self.add_enterPositionProp_Label = Label()
        self.add_enterPositionProp_Label.grid(row=2, column=0)
        self.add_enterPositionProp_Label.configure(font="Arial 12", text="Enter position of Property")

    def add_enterPositionProp_entry_box(self) -> None:
        self.add_enterPositionProp_entry_box = Entry()
        self.add_enterPositionProp_entry_box.grid(row=2, column=1)

    ### enter position of household ###

    def add_enterPositionHousehold_Label(self) -> None:
        self.add_enterPositionHousehold_Label = Label()
        self.add_enterPositionHousehold_Label.grid(row=3, column=0)
        self.add_enterPositionHousehold_Label.configure(font="Arial 12", text="Enter position of Household")

    def add_enterPositionHousehold_entry_box(self) -> None:
        self.add_enterPositionHousehold_entry_box = Entry()
        self.add_enterPositionHousehold_entry_box.grid(row=3, column=1)

    ### create payment and receipt button ###
    def add_createPayment_receipt_btn(self) -> None:
        self.add_createPayment_receipt_btn = Button()
        self.add_createPayment_receipt_btn.grid(row=8, column=2)
        self.add_createPayment_receipt_btn.configure(font="Arial 12", text="Process payment")
        self.add_createPayment_receipt_btn.bind("<ButtonRelease-1>", self.add_createPayment_receipt_btn_clicked)

    def add_createPayment_receipt_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            prop_position = int(self.add_enterPositionProp_entry_box.get())
            h_position = int(self.add_enterPositionHousehold_entry_box.get())
            DB.bau.take_payment_generate_receipt(tf_position, prop_position, h_position)
            messagebox.showinfo("Complete", "Payment Processed")
        except:
            print("Position entry is not compatible")
            print("Please check thoroughfare, property and household position entries are valid.")

    ### create invoice button ###
    def add_createInvoice_btn(self) -> None:
        self.add_createInvoice_btn = Button()
        self.add_createInvoice_btn.grid(row=8, column=3)
        self.add_createInvoice_btn.configure(font="Arial 12",
                                             text="Create Invoice")
        self.add_createInvoice_btn.bind("<ButtonRelease-1>", self.createInvoice_btn_clicked)

    def createInvoice_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            prop_position = int(self.add_enterPositionProp_entry_box.get())
            h_position = int(self.add_enterPositionHousehold_entry_box.get())
            DB.bau.generate_invoice_specific_household(tf_position, prop_position, h_position)
            messagebox.showinfo("Complete", "Invoice created.")
        except:
            print("Position entry is not compatible")
            print("Please check thoroughfare, property and household position entries are valid.")

    ### rceipts household button ###

    def receipts_household_btn(self) -> None:
        self.receipts_household_btn = Button()
        self.receipts_household_btn.grid(row=7, column=2, columnspan=2,padx=20, pady=(50,0))
        self.receipts_household_btn.configure(font="Arial 12", text="Generate all receipts and invoices for household")
        self.receipts_household_btn.bind("<ButtonRelease-1>", self.add_all_receipts_invoices_btn_clicked)

    def add_all_receipts_invoices_btn_clicked(self, event) -> None:
        try:
            tf_position = int(self.add_enterPositionTF_entry_box.get())
            prop_position = int(self.add_enterPositionProp_entry_box.get())
            h_position = int(self.add_enterPositionHousehold_entry_box.get())
            DB.bau.print_invoices_and_receipts_for_household(tf_position, prop_position, h_position)
        except:
            print("Position entry is not compatible")
            print("Please check thoroughfare, property and household position entries are valid.")
