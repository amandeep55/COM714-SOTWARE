from tkinter import *
from tkinter import messagebox
from basic_user_gui import Basic_User_Gui
from manager_user_gui import Manager_User_Gui
from admin_gui import Admin_Gui

class Main_Gui(Tk):

  # initialise window
  def __init__(self):
    super().__init__()

    # set window attributes
    self.title("Gui")
    self.configure(bg="#eee",
                   height= 500,
                   width = 500)
    self.add_admin_btn()
    self.add_mngr_button()
    self.add_basic_user_button()


  def add_admin_btn(self)->None:
      #creation
      self.admin_btn = Button()
      self.admin_btn.grid(row=0, column=0)

      #style
      self.admin_btn.configure(font = "Arial 20",
                             text = "Admin",bg = "#000a12", fg = "white", width = 4)

      #events
      self.admin_btn.bind("<ButtonRelease-1>", self.admin_btn_clicked)

  def add_mngr_button(self)->None:
      self.mgr_btn = Button()
      self.mgr_btn.grid(row=5, column=0)

      # style
      self.mgr_btn.configure(font="Arial 20",
                             text="Manager", bg = "#000a12", fg = "white")
      # events
      self.mgr_btn.bind("<ButtonRelease-1>", self.mngr_button_clicked)


  def add_basic_user_button(self)->None:
      self.basic_user_btn = Button()
      self.basic_user_btn.grid(row=10, column=0)

      # style
      self.basic_user_btn.configure(font="Arial 20",
                             text="Basic User", bg = "#000a12", fg = "white")
      # events
      self.basic_user_btn.bind("<ButtonRelease-1>", self.basic_user_btn_clicked)


  def admin_btn_clicked(self,event)->None:
      self.destroy()
      ag = Admin_Gui()
      ag.mainloop()

  def mngr_button_clicked(self,event)->None:
      self.destroy()
      mug = Manager_User_Gui()
      mug.mainloop()

  def basic_user_btn_clicked(self,event)->None:
      self.destroy()
      bug = Basic_User_Gui()
      bug.mainloop()





