import tkinter as Tk
from tkinter import messagebox 
from tkinter import filedialog

class LoginPage:
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Python")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        self.frameButton=Tk.Frame(parent)
        self.frameButton1=Tk.Frame(parent)
        self.frameButton2=Tk.Frame(parent)

        Tk.Label (text ="LOGIN PAGE", bg ="green",fg="brown",width="350",height="1",font=("tahoma",16)).pack() 
        self.label_username =Tk.Label(text="Username :")
        self.label_password =Tk.Label(text="Password :")
        self.entry_username =Tk.Entry()
        self.entry_password =Tk.Entry(show="*")
        self.label_username.place(x=80,y=55)
        self.label_password.place(x=80,y=85)
        self.entry_username.place(x=170, y=58)
        self.entry_password.place(x=170, y=88)
        Tk.Label (text ="", bg ="green",fg="brown",width="350",height="1",font=("tahoma",16)).place(x=0, y=185)

        self.hide()
        self.makeButton()
        
        subFrame=MainPage(self)


    def makeButton (self):
        self.checkbox = Tk.Checkbutton(self.frameButton, command=self.keeplogin, text="Keep me logged in").grid(row=0, column=1)
        self.frameButton.place(x=90, y=110)
        self.logbtn = Tk.Button(self.frameButton1, text="Login",command=self.logInBttn).grid(row=0, column=1)
        self.frameButton1.place(x=130, y=145)
        self.Quitbutton = Tk.Button(self.frameButton2, text="exit",command=self.quit).grid(row=0, column=1)
        self.frameButton2.place(x=220, y=145)

    def keeplogin(self):
        self.hide()
        subFrame=MainPage(self)

    def hide(self):
        """"""
        self.root.withdraw()
 
    def logInBttn(self):
        """"""
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "1" and password == "1":
            self.hide()
            subFrame = MainPage(self)
        else:
            messagebox.showerror("Login error", "Incorrect username")

    def quit(self):
        """"""
        answer = messagebox.askquestion('', "Are you sure want to exit ?" )
        if answer == 'yes':
            self.root.destroy()
        elif answer == 'no':  # 'no'
            pass

    def logOut(self):
        """"""
        self.root.update()
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.root.deiconify()

class MainPage(Tk.Toplevel):
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
        #self.configure(background='brown')
        self.title("MainPage")
        Tk.Label (self,text ="AUTOMATIC GRADING SYSTEM", bg ="grey",fg="black",width="600",height="1",font=("calibri",20)).pack() 
        Tk.Label (self,text ="Please Set The Requiretment for make grading automaticly bellow this",fg="red",font=("tahoma",14)).place(x=70,y=55)
        # Tk.Label (self,text ="Result",fg="blue",font=("tahoma",14)).place(x=520,y=55)
        Tk.Label (self,text ="compiled by : Haryanto (M07158031)",bg ="grey",
            fg="red",width="750",height="1",font=("tahoma",9)).place(x=0,y=440)

        self.ButtonInPage()

    def ButtonInPage (self):
        Tk.Button(self, text="Logout",command=self.backLoginPage).place(x=620, y=405)
        Tk.Entry(self, width = 30 ).place(x=225, y=300)
        Tk.Button(self,relief='raised', text="Browse", command=self.browseButton).place(x=525, y=300)
        Tk.Button(self, text = "Send", height = 8, width = 20,bg='#838B8B').place(x=75, y=120)
        Tk.Button(self, text = "Send", height = 8, width = 20,bg="blue").place(x=275, y=120)
        Tk.Button(self, text = "Send", height = 8, width = 20,bg="blue").place(x=475, y=120)
        # Tk.Button(self,relief='raised', text="New Image", command=self.openCAM).place(x=225, y=375)
        Tk.Button(self,relief='raised', text="exit", command=self.quit_1).place(x=685, y=405)
        Tk.Button(self, text = "Send", height = 4, width = 20,bg="blue").place(x=325, y=335)
        # Tk.Button(self,relief='raised', text="Edged Detect", command=self.edgeDetection).place(x=500, y=375)
 
    def backLoginPage(self):
        """"""
        self.destroy()
        self.mainPageFrame.logOut()

    def browseButton(self):
        try :
            tipeFile = (('image files', '*.jpg'), ('png files', '*.png'), ('all files', '*'))
            self.path = filedialog.askopenfilename(filetypes=tipeFile)
        except :
            messagebox.showwarning("error","wrong format media, please check again")

         
    def quit_1(self):
        answer = messagebox.askquestion('', "Are you sure want to exit ?" )
        if answer == 'yes':
            self.quit()
        elif answer == 'no':  # 'no'
            pass

def main ():
    root = Tk.Tk()
    root.bind('<Escape>', lambda e: root.quit())
    # root.iconbitmap(r'1123.ico')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 350
    height = 200
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    app = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
