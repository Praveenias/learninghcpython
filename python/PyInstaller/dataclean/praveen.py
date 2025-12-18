
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo
from datacheck import Datacheck
from help import logger
from pathlib import Path


class App(tk.Tk):
    def __init__(self):
        logger.info(__file__+" Tinker started")
        super().__init__()
        datacheck = Datacheck()

        ## Setting up Initial Things
        self.title("Atom Helper")
        self.geometry("850x550")
        self.resizable(False, False)

        container = tk.Frame(self, bg="#8AA7A9",relief=tk.RIDGE,borderwidth=3)
        container.pack(side="top", fill="both", expand = True,pady=20,padx=20)
        container.grid_rowconfigure(0,minsize=500, weight=1)
        container.grid_columnconfigure(0, minsize=800,weight=1)
        self.frames = {}
        self.Dataclean = Dataclean
        #self.GetExemption = GetExemption

        ## Defining Frames and Packing it
        for F in {Dataclean}:
            frame = F(self, container,datacheck)
            self.frames[F] = frame
            frame.grid(row=0,column=0, sticky="nsew")    
           
        self.show_frame(Dataclean)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise() 

class Dataclean(tk.Frame):
    def __init__(self, parent, container,datacheck):
        super().__init__(container)
        self.datacheck = datacheck
        self.filename = ''

        #file_type
        select_file_type_label = tk.Label(self, text="File type*",height=2,width=20)
        select_file_type_label.grid(row=0,column=0)
        allowed_filetype = ['bom','contact','master','manufacturer', 'regulation',
                      'substance','fmd','coc','scip','rba','query_statement',
                      'exemption_catagory','exemption_list']
        self.file_type = StringVar()
        self.file_type.set(allowed_filetype[0])  
        drop = OptionMenu(self,self.file_type , *allowed_filetype )
        drop.config(width=41,font=('Arial 13'))
        drop.grid(row=0,column=1,ipadx=20)
        
        #sheet name
        sheet_name_label = tk.Label(self, text="Input Sheet Name",height=2,width=20)
        self.sheet_name_entry = tk.Entry(self, width=50,font=('Arial 13'))
        sheet_name_label.grid(row=2, column=0, sticky="e")
        self.sheet_name_entry.grid(row=2, column=1)

        #header row
        header_row_label = tk.Label(self, text="Header Row",height=2,width=20).grid(row=3, column=0, sticky="e")
        self.header_row_entry = tk.Entry(self, width=50,font=('Arial 13'))
        self.header_row_entry.grid(row=3, column=1)
        self.header_row_entry.insert(0,2)

        #output_file_name
        outfile_name_label = tk.Label(self, text="Output File Name",height=2,width=20)
        self.outfile_name_entry = tk.Entry(self, width=50,font=('Arial 13'))
        outfile_name_label.grid(row=4, column=0, sticky="e")
        self.outfile_name_entry.grid(row=4, column=1)

        #input_file
        input_file_label = tk.Label(self, text="Select Input File*",height=2,width=20)
        input_file_label.grid(row=5,column=0)
        input_file_button = tk.Button(self,text='Select Input File',command=self.select_file,width=50)
        input_file_button.grid(row=5,column=1)

        #output_file_name
        self.selected_file_label = tk.Label(self, text=self.filename)
        self.selected_file_label.grid(row=5, column=3)


        
        btn_submit = tk.Button(self, text="Submit",bg="green",fg="white",command=self.get_values)
        btn_submit.grid(column=1)

        
    
    def select_file(self):
    
        self.filename = filedialog.askopenfilename(
            title='select input file',
            )
        print(self.filename,Path(self.filename).name)
        self.selected_file_label.config(text=Path(self.filename).name)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=4, relief=RAISED, activebackground="#80B9DC")
        menu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="DATACLEAN",command=lambda: parent.show_frame(parent.Dataclean))
        menubar.add_cascade(label="GetExemption",command=lambda: parent.show_frame(parent.GetExemption))  
        menubar.add_cascade(label="QUIT",command=parent.quit)
        return menubar
    
    def get_values(self):
        
        output_file_name = self.outfile_name_entry.get()
        header_row = self.header_row_entry.get()
        sheet_name = self.sheet_name_entry.get()
        file_type = self.file_type.get()
        if(file_type=='' or self.filename == ''):
            msg =''
            if self.filename=='':msg += 'Select Input File'
            if file_type=='': msg+= 'Select File Type'
            showerror('Error',msg)
            return False
        #print(header_row,type(header_row),file_type,self.filename)
        result = self.datacheck.main({'header_row':int(header_row),'file_type':file_type,
                                    'sheet_name':sheet_name,'input_file_path':self.filename,'out_file_name':output_file_name})
        if result['status'] == 'error':
            showerror('Error',result['msg'])
        if result['status'] == 'success':
            showinfo('Success',result['msg'])
        print(result)
        # showinfo('Success',self.outfile_name_entry.get(),self.sheet_name_entry.get())


class GetExemption(tk.Frame):
    def __init__(self, parent, container,datacheck):
        super().__init__(container)

        label = tk.Label(self, text="Get exemption Page", font=('Times', '20'))
        label.pack(pady=0,padx=0)

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=4, relief=RAISED, activebackground="#80B9DC")
        menu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="DATACLEAN",command=lambda: parent.show_frame(parent.Dataclean))
        menubar.add_cascade(label="GetExemption",command=lambda: parent.show_frame(parent.GetExemption))  
        menubar.add_cascade(label="QUIT",command=parent.quit)
        return menubar



if __name__ == "__main__":
    app = App()
    app.mainloop()