from tkinter import *
from tkinter import messagebox
from invoice import Invoice
from receipt import Receipt
from household import Household
from property import Property
from thoroughfare import Thoroughfare
from estate import Estate
from basic_user import Basic_User
from manager import Manager_User
from basic_user_gui import Basic_User_Gui
from db import DB

class Manager_User_Gui(Basic_User_Gui):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Manager User Gui")
    self.configure(bg="#c68400",
                   height= 1000,
                   width = 1000)

    self.add_level_Label()
    self.add_deleteTF_btn()
    self.add_deleteProperty_btn()
    self.add_deleteHousehold_btn()
    self.add_BasicUserBtn()
    self.add_viewInvoicesEntireEstateBtn()

  def add_level_Label(self)->None:
     self.add_level_label = Label()
     self.add_level_label.grid(row=0, column=1)
     self.add_level_label.configure(font="Arial 22", text="Manager", borderwidth=2, relief="groove", bg="#000a12", fg="white")

  ### delete thoroughfare ###

  def add_deleteTF_btn(self)->None:
      self.add_deleteTF_btn = Button()
      self.add_deleteTF_btn.grid(row=4, column=2 , pady=(50,0))
      self.add_deleteTF_btn.configure(font="Arial 12",
                                  text="Delete Thoroughfare")
      self.add_deleteTF_btn.bind("<ButtonRelease-1>", self.delete_TF_btn_clicked)

  def delete_TF_btn_clicked(self, event)->None:
      try:
          tf_position = int(self.add_enterPositionTF_entry_box.get())
          DB.mgr.delete_tf(tf_position)
          messagebox.showinfo("Complete", "Thoroughfare deleted")
      except:
          print("Thoroughfare position entry is not compatible")

## delete property ###

  def add_deleteProperty_btn(self)->None:
      self.add_deleteProperty_btn = Button()
      self.add_deleteProperty_btn.grid(row=5, column=2)
      self.add_deleteProperty_btn.configure(font="Arial 12",
                                  text="Delete Property")
      self.add_deleteProperty_btn.bind("<ButtonRelease-1>", self.deleteProperty_btn_clicked)

  def deleteProperty_btn_clicked(self, event)->None:
      try:
          tf_position = int(self.add_enterPositionTF_entry_box.get())
          prop_position = int(self.add_enterPositionProp_entry_box.get())
          DB.mgr.delete_prop(tf_position, prop_position)
          messagebox.showinfo("Complete", "Property deleted")
      except:
          print("Position entry is not compatible")
          print("Please check thoroughfare and property position entries are valid.")

### delete household ###

  def add_deleteHousehold_btn(self)->None:
      self.add_deleteHousehold_btn = Button()
      self.add_deleteHousehold_btn.grid(row=6, column=2)
      self.add_deleteHousehold_btn.configure(font="Arial 12",
                                  text="Delete Household")
      self.add_deleteHousehold_btn.bind("<ButtonRelease-1>", self.deleteHousehold_btn_clicked)

  def deleteHousehold_btn_clicked(self, event)->None:
      try:
          tf_position = int(self.add_enterPositionTF_entry_box.get())
          prop_position = int(self.add_enterPositionProp_entry_box.get())
          h_position = int(self.add_enterPositionHousehold_entry_box.get())
          DB.mgr.delete_household(tf_position, prop_position, h_position)
          messagebox.showinfo("Complete", "Household deleted")
      except:
          print("Position entry is not compatible")
          print("Please check thoroughfare, property and household position entries are valid.")

### create basic user section ###

  def add_BasicUserBtn(self)->None:
      self.add_BasicUserBtn = Button()
      self.add_BasicUserBtn.grid(row=1, column=4)
      self.add_BasicUserBtn.configure(font="Arial 12", text="Create Basic User")
      self.add_BasicUserBtn.bind("<ButtonRelease-1>", self.add_BasicUserBtn_clicked)

  def add_BasicUserBtn_clicked(self, event)->None:
      new_basic_user = DB.mgr.create_basic_user()
      messagebox.showinfo("Created", "New Basic User created")
      return new_basic_user

### view total invoice for all households on estate button ####

  def add_viewInvoicesEntireEstateBtn(self)->None:
      self.add_viewInvoicesEntireEstateBtn = Button()
      self.add_viewInvoicesEntireEstateBtn.grid(row=2, column=4)
      self.add_viewInvoicesEntireEstateBtn.configure(font="Arial 12", text="View invoices for entire estate")
      self.add_viewInvoicesEntireEstateBtn.bind("<ButtonRelease-1>", self.add_viewInvoicesEntireEstateBtn_clicked)

  def add_viewInvoicesEntireEstateBtn_clicked(self, event)->None:
      DB.mgr.get_total_invoice_estate()





