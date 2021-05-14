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
from admin import Admin
from basic_user_gui import Basic_User_Gui
from manager_user_gui import Manager_User_Gui
from db import DB

class Admin_Gui(Manager_User_Gui):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Admin Gui")
    self.configure(bg="#c68400",
                   height= 1000,
                   width = 1000)

    self.add_createEstateBtn()
    self.add_label_position_estate()
    self.add_position_estate_entry_box()
    self.add_view_estate_btn()
    self.add_update_estate_btn()
    self.add_delete_estate_btn()

    self.add_label_position_invoice()
    self.add_entry_box_position_invoice()

    self.add_updateEstateInvoiceBtn()
    self.add_deleteEstateInvoiceBtn()
    self.add_viewPaymentsForEntireSystemBtn()

  def add_level_Label(self)->None:
     self.add_level_label = Label()
     self.add_level_label.grid(row=0, column=1)
     self.add_level_label.configure(font="Arial 22", text="Admin", borderwidth=2, relief="groove", bg="#000a12", fg="white")

# create, view, delete estate

  def add_createEstateBtn(self)->None:
      self.add_createEstateBtn = Button()
      self.add_createEstateBtn.grid(row=12, column=0, pady=(30,5))
      self.add_createEstateBtn.configure(font="Arial 12", text="Create Estate")
      self.add_createEstateBtn.bind("<ButtonRelease-1>", self.add_createEstateBtn_clicked)

  def add_createEstateBtn_clicked(self, event)->None:
      DB.adm.create_estate()
      messagebox.showinfo("Complete", "Estate was created.")

  def add_label_position_estate(self)->None:
      self.add_label_position_estate = Label()
      self.add_label_position_estate.grid(row=13, column=0)
      self.add_label_position_estate.configure(font="Arial 12", text="Enter position of Estate")

  def add_position_estate_entry_box(self)->None:
      self.add_position_estate_entry_box = Entry()
      self.add_position_estate_entry_box.grid(row=13, column=1)

  def add_view_estate_btn(self)->None:
      self.add_view_estate_btn = Button()
      self.add_view_estate_btn.grid(row=12, column=1, pady=(30,5))
      self.add_view_estate_btn.configure(font="Arial 12", text="View Estate")
      self.add_view_estate_btn.bind("<ButtonRelease-1>", self.add_view_estate_btn_clicked)

  def add_view_estate_btn_clicked(self, event)->None:
      try:
          e_position = int(self.add_position_estate_entry_box.get())
          DB.adm.view_estate(e_position)
      except:
          print("Estate position is not compatible")

  def add_label_position_invoice(self)->None:
      self.add_label_position_invoice = Label()
      self.add_label_position_invoice.grid(row=15, column=0)
      self.add_label_position_invoice.configure(font="Arial 12", text="Enter position of Invoice")

  def add_entry_box_position_invoice(self)->None:
      self.add_entry_box_position_invoice = Entry()
      self.add_entry_box_position_invoice.grid(row=15, column=1)

    # update estate

  def add_update_estate_btn(self)->None:
      self.add_update_estate_btn = Button()
      self.add_update_estate_btn.grid(row=14, column=0)
      self.add_update_estate_btn.configure(font="Arial 12", text="Update Estate")
      self.add_update_estate_btn.bind("<ButtonRelease-1>", self.add_update_estate_btn_clicked)

  def add_update_estate_btn_clicked(self, event)->None:
      try:
           e_position = int(self.add_position_estate_entry_box.get())
           DB.adm.update_estate(e_position)
           messagebox.showinfo("Complete", "Estate updated")
      except:
          print("Estate position is not compatible")

    # delete estate

  def add_delete_estate_btn(self)->None:
      self.add_delete_estate_btn = Button()
      self.add_delete_estate_btn.grid(row=14, column=1)
      self.add_delete_estate_btn.configure(font="Arial 12", text="Delete Estate")
      self.add_delete_estate_btn.bind("<ButtonRelease-1>",self.add_delete_estate_btn_clicked)

  def add_delete_estate_btn_clicked(self, event)->None:
      try:
          e_position = int(self.add_position_estate_entry_box.get())
          DB.adm.delete_estate(e_position)
          messagebox.showinfo("Complete", "Estate deleted")
      except:
          print("Estate position is not compatible")

#view, update and delete estate invoices and payments#

  def add_viewEstateInvoicesandPaymentsBtn(self)->None:
      self.add_viewEstateInvoicesandPaymentsBtn = Button()
      self.add_viewEstateInvoicesandPaymentsBtn.grid(row=14, column=4)
      self.add_viewEstateInvoicesandPaymentsBtn.configure(font="Arial 12", text="View Estate Invoices")
      self.add_viewEstateInvoicesandPaymentsBtn.bind("<ButtonRelease-1>", self.add_viewEstateInvoicesandPaymentsBtn_clicked)

  def add_viewEstateInvoicesandPaymentsBtn_clicked(self, event)->None:
      DB.adm.get_total_invoice_estate()

#update invoices and payments

  def add_updateEstateInvoiceBtn(self)->None:
      self.add_updateEstateInvoiceBtn = Button()
      self.add_updateEstateInvoiceBtn.grid(row=9, column=4)
      self.add_updateEstateInvoiceBtn.configure(font="Arial 12", text="Update Estate Invoice")
      self.add_updateEstateInvoiceBtn.bind("<ButtonRelease-1>",
                                                     self.add_updateEstateInvoiceBtn_clicked)

  def add_updateEstateInvoiceBtn_clicked(self, event)->None:
      try:
          e_position = int(self.add_position_estate_entry_box.get())
          tf_position = int(self.add_enterPositionTF_entry_box.get())
          prop_position = int(self.add_enterPositionProp_entry_box.get())
          h_position = int(self.add_enterPositionHousehold_entry_box.get())
          i_position = int(self.add_entry_box_position_invoice.get())
          DB.adm.update_estate_invoices(e_position,tf_position, prop_position, h_position, i_position)
          messagebox.showinfo("Complete", "Invoice updated")
      except:
          print("Position entry is not compatible")
          print("Please ensure estate, household and invoice position are correct")


  def add_deleteEstateInvoiceBtn(self)->None:
      self.add_deleteEstateInvoiceBtn = Button()
      self.add_deleteEstateInvoiceBtn.grid(row=10, column=4)
      self.add_deleteEstateInvoiceBtn.configure(font="Arial 12", text="Delete invoice")
      self.add_deleteEstateInvoiceBtn.bind("<ButtonRelease-1>",
                                           self.add_deleteEstateInvoiceBtn_clicked)

  def add_deleteEstateInvoiceBtn_clicked(self, event)->None:
      try:
          e_position = int(self.add_position_estate_entry_box.get())
          tf_position = int(self.add_enterPositionTF_entry_box.get())
          prop_position = int(self.add_enterPositionProp_entry_box.get())
          h_position = int(self.add_enterPositionHousehold_entry_box.get())
          i_position = int(self.add_entry_box_position_invoice.get())
          DB.adm.delete_estate_invoices(e_position,h_position,i_position)
          messagebox.showinfo("Complete", "Invoice deleted")
      except:
          print("Position entry is not compatible")
          print("Please ensure estate, household and invoice position are correct")

# view payments for entire estate button #

  def add_viewPaymentsForEntireSystemBtn(self)->None:
      self.add_viewPaymentsForEstateBtn = Button()
      self.add_viewPaymentsForEstateBtn.grid(row=11, column=4)
      self.add_viewPaymentsForEstateBtn.configure(font="Arial 12", text="View payments for entire system")
      self.add_viewPaymentsForEstateBtn.bind("<ButtonRelease-1>", self.add_viewPaymentsForEstateBtn_clicked)

  def add_viewPaymentsForEstateBtn_clicked(self, event)->None:
      DB.adm.calculate_total_invoice_in_system()


