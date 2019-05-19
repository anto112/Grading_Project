from main import *

class Database_Ui(Tk.Toplevel):
    """"""
    def __init__(self, page):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.mainPageFrame = page             
        # self.iconbitmap(r'11.ico')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 750
        height = 450
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.resizable(0, 0)

        self.title("MainPage")
        Tk.Label (self,text ="DATABASE INTERFACE", bg ="grey",fg="black",width="600",height="1",font=("calibri",20)).pack() 
        Tk.Label (self,text ="Select table :",fg="black",font=("tahoma",14)).place(x=20,y=55)
        Tk.Label (self,text ="Content table",fg="black",font=("tahoma",14)).place(x=190,y=55)
        Tk.Label (self,text ="Table list:",fg="black",font=("tahoma",14)).place(x=20, y=170)
        Tk.Label (self,text ="compiled by : Haryanto (M07158031)",bg ="grey",
            fg="red",width="750",height="1",font=("tahoma",9)).place(x=0,y=440)

        Tk.Entry(self, width = 20 ).place(x=20, y=90)


        Tk.Button(self, text="Logout").place(x=620, y=405)
        Tk.Button(self,relief='raised', text="exit", command=self.quit_t).place(x=685, y=405)
        
        menubar = Tk.Menu(self)
        Db_menu = Tk.Menu(menubar, tearoff=0)
        Db_menu.add_command(label="Create")
        Db_menu.add_command(label="Delete")
        Db_menu.add_command(label="Show")

        menubar.add_cascade(label="Database", menu=Db_menu)

        Tk.Button(self, text="CHECK").place(x=60, y=125)
        Table_menu = Tk.Menu(menubar, tearoff=0)
        Table_menu.add_command(label="Create")
        Table_menu.add_command(label="Delete")
        Table_menu.add_command(label="Show")
        menubar.add_cascade(label="Table", menu=Table_menu)

        helpmenu=Tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About")
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.config(menu=menubar)

        table_lb =Tk.Listbox(self,width=15, height=9, font=("Helvetica", 12))
       	table_lb.place(x=20, y=210)

       	listNodes = Tk.Listbox(self, width=60, height=15, font=("Helvetica", 12))
       	listNodes.place(x=190, y=100)
       	        
         
    def quit_t(self):
        answer = messagebox.askquestion('', "Are you sure want to exit ?" )
        if answer == 'yes':
            self.quit()
        elif answer == 'no':  # 'no'
            pass

class test:
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Test")
        subwindow = Database_Ui(self)
        self.root.mainloop()


def main():

    page = test()


if __name__ == "__main__":
    main()
