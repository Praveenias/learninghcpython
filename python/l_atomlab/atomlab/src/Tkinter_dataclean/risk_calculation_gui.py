import tkinter as tk
from tkinter import *
from help import Helper
import json

class Risk_calculation_gui(tk.Frame):
    def __init__(self,parent,container,null):
        super().__init__(container)
        self.helper = Helper()
        self.db_config = self.get_db_config()
        self.bom_names = sorted(self.get_boms())

        #bom_name
        # select_bom_name_label = tk.Label(self, text="Bom name*",height=2,width=20)
        # select_bom_name_label.grid(row=0,column=0)
        # #bom_names = self.ipns
        # self.bom_name = StringVar()
        # self.bom_name.set(None)  
        # drop = OptionMenu(self,self.bom_name , *self.bom_names )
        # drop.config(width=41,font=('Arial 13'))
        # drop.grid(row=0,column=1,ipadx=20)

        #ipns
        # select_file_type_label = tk.Label(self, text="Bom name*",height=2,width=20)
        # select_file_type_label.grid(row=1,column=0)
        # allowed_filetype = self.ipns
        # self.file_type = StringVar()
        # self.file_type.set(None)  
        # drop = OptionMenu(self,self.file_type , *allowed_filetype )
        # drop.config(width=41,font=('Arial 13'))
        # drop.grid(row=0,column=1,ipadx=20)

        ipn_label = tk.Label(self, text="Search Ipns",height=2,width=20).grid(row=0, column=0, sticky="e")
        self.password_entry = tk.Entry(self, width=50,font=('Arial 13'))
        self.password_entry.grid(row=0, column=1)

        ip_list = tk.Listbox(self,width=50).grid(row=1,column=0)
        
        
    def get_db_config(self):
        with open('config_py.json',encoding='utf-8') as dt:
            data = json.load(dt)
        return data

    def get_ipns(self):
        qry="select distinct(subscriber_part_number),distinct(bom_master_id) from tbl_bom"
        if self.bom_name.get() != None:
            qry +=f" where bom_master_id in ({self.bom_name.get()[0]})"()
        print(qry)
        
        #ipns = self.helper.connectDB(self.db_config,qry)
        #print(ipns,len(ipns))

    def get_boms(self):
        qry = "select id,bom_name from tbl_bom_master"
        ipns = self.helper.connectDB(self.db_config,qry)
        return ipns
        print(ipns,len(ipns))

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=4, relief=RAISED, activebackground="#80B9DC")
        menu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="DATACLEAN",command=lambda: parent.show_frame(parent.Dataclean))
        menubar.add_cascade(label="GetExemption",command=lambda: parent.show_frame(parent.GetExemption))
        menubar.add_cascade(label="Database Config",command=lambda: parent.show_frame(parent.Database_config))
        menubar.add_cascade(label="Risk Calculation",command=lambda: parent.show_frame(parent.Risk_calculation_gui))  
        menubar.add_cascade(label="QUIT",command=parent.quit)
        return menubar


