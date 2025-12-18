'''Databse Configuration GUI Page

'''

import tkinter as tk
from tkinter import *
import json
from help import Helper
from tkinter.messagebox import showerror, showinfo
from pathlib import Path

class Database_config(tk.Frame):
    def __init__(self,parent,container,null):
        '''GUI Initilization for database configuration UI'''

        super().__init__(container)
        self.helper = Helper()

        #Host
        host_name_label = tk.Label(self, text="Host name",height=2,width=20).grid(row=0, column=0, sticky="e")
        self.host_name_entry = tk.Entry(self, width=50,font=('Arial 13'))
        self.host_name_entry.grid(row=0, column=1)

        #Port
        port_name_label = tk.Label(self, text="Port Number",height=2,width=20).grid(row=2, column=0, sticky="e")
        self.port_name_entry = tk.Entry(self, width=50,font=('Arial 13'))
        self.port_name_entry.grid(row=2, column=1)

        #Username
        username_label = tk.Label(self, text="User Name",height=2,width=20).grid(row=3, column=0, sticky="e")
        self.username_entry = tk.Entry(self, width=50,font=('Arial 13'))
        self.username_entry.grid(row=3, column=1)

        #Password
        password_label = tk.Label(self, text="Password",height=2,width=20).grid(row=4, column=0, sticky="e")
        self.password_entry = tk.Entry(self, width=50,font=('Arial 13'))
        self.password_entry.grid(row=4, column=1)

        #Database
        database_name_label = tk.Label(self, text="Database Name",height=2,width=20).grid(row=5, column=0, sticky="e")
        self.database_name_entry = tk.Entry(self, width=50,font=('Arial 13'))
        self.database_name_entry.grid(row=5, column=1)

        btn_submit = tk.Button(self, text="Save changes",bg="green",fg="white",command=self.save_to_json)
        btn_submit.grid(column=1)

        btn_submit = tk.Button(self, text="Check Connection",bg="green",fg="white",command=self.check_db_connection)
        btn_submit.grid(column=1)
        self.load_config_data()

    def create_menubar(self, parent):
        '''Menubar for Database Configuration Menubar'''

        menubar = Menu(parent, bd=4, relief=RAISED, activebackground="#80B9DC")
        menu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="DATACLEAN",command=lambda: parent.show_frame(parent.Dataclean))
        menubar.add_cascade(label="GetExemption",command=lambda: parent.show_frame(parent.GetExemption))
        menubar.add_cascade(label="Database Config",command=lambda: parent.show_frame(parent.Database_config))  
        menubar.add_cascade(label="QUIT",command=parent.quit)
        return menubar

    def load_config_data(self):
        ''' Load config data from json file to GUI'''

        with open(Path('config_py.json'),encoding='utf-8') as dt:
            data = json.load(dt)
        self.host_name_entry.insert(0,data['host'])
        self.port_name_entry.insert(0,data['port'])
        self.username_entry.insert(0,data['username'])
        self.password_entry.insert(0,data['password'])
        self.database_name_entry.insert(0,data['database'])

    def save_to_json(self):
        ''' On Click save button to save details in json file'''

        ip_data = self.get_data()
        json_data = json.dumps(ip_data)
        with open(Path("config_py.json"), "w") as outfile:
            outfile.write(json_data)
        print(ip_data)

    def get_data(self):
        ''' Returns the data that entered in Input for Database settings'''

        data={
            "host" : self.host_name_entry.get(),
            "port" : self.port_name_entry.get(),
            "username" : self.username_entry.get(),
            "password" : self.password_entry.get(),
            "database" : self.database_name_entry.get(),
        }
        return data

    def check_db_connection(self):
        ''' Check DB Connection based on the given Input Parameters'''

        ip_data = self.get_data()
        db_con = self.helper.check_db_connection(ip_data)
        if db_con:
            showinfo("Info","connection successfull")
            return 
        showerror("Error","Connection Failed")

        
