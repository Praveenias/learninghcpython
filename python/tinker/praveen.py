import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        ## Setting up Initial Things
        self.title("Atom Helper")
        self.geometry("720x550")
        self.resizable(True, True)

        container = tk.Frame(self, bg="#8AA7A9")
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0,minsize=500, weight=1)
        container.grid_columnconfigure(0, minsize=800,weight=1)
        self.frames = {}
        self.Dataclean = Dataclean
        self.GetExemption = GetExemption

        ## Defining Frames and Packing it
        for F in {Dataclean, GetExemption}:
            frame = F(self, container)
            self.frames[F] = frame
            frame.grid(row=0,column=0, sticky="nsew")    
           
        self.show_frame(Dataclean)

    def show_frame(self, cont):
        frame = self.frames[cont]
        menubar = frame.create_menubar(self)
        self.configure(menu=menubar)
        frame.tkraise() 

class Dataclean(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)
        
        labels = [
            "Input Sheet Name",
            "Header Row",
            "Output File name",
        ]
        for idx, text in enumerate(labels,start=2):
            label = tk.Label(self, text=text,height=2,width=20)
            entry = tk.Entry(self, width=50,font=('Arial 13'))
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
        
        # open button
        label = tk.Label(self, text="Select Input File",height=2,width=20)
        label.grid(row=5,column=0)
        open_button = tk.Button(self,text='Select Input File',command=self.select_file,width=50)

        open_button.grid(row=5,column=1)
        select_file_type_label = tk.Label(self, text="File type",height=2,width=20)
        select_file_type_label.grid(row=0,column=0)
        allowed_filetype = ['bom','contact','master','manufacturer', 'regulation',
                      'substance','fmd','coc','scip','rba','query_statement',
                      'exemption_catagory','exemption_list']
        file_type = StringVar()
        file_type.set(allowed_filetype[0])
        
        # Create Dropdown menu
        drop = OptionMenu(self, file_type , *allowed_filetype )
        drop.config(width=44)
        drop.grid(row=0,column=1)
        btn_submit = tk.Button(self, text="Submit")
        btn_submit.grid(column=1)

    def select_file(self):

        filename = filedialog.askopenfilename(
            title='select input file',
            initialdir='/', )

    def create_menubar(self, parent):
        menubar = Menu(parent, bd=4, relief=RAISED, activebackground="#80B9DC")
        menu = Menu(menubar, tearoff=0, relief=RAISED, activebackground="#026AA9")
        menubar.add_cascade(label="DATACLEAN",command=lambda: parent.show_frame(parent.Dataclean))
        menubar.add_cascade(label="GetExemption",command=lambda: parent.show_frame(parent.GetExemption))  
        menubar.add_cascade(label="QUIT",command=parent.quit)
        return menubar

class GetExemption(tk.Frame):
    def __init__(self, parent, container):
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