import tkinter as Tk
from tkinter import messagebox 
from tkinter import filedialog
import sqlite3
import os

with sqlite3.connect('student.db') as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Student (name TEXT NOT NULL,Email TEXT NOT NULL,
                Gender TEXT NOT NULL,country TEXT NOT NULL,password TEXT NOT NULL)''')
db.commit()
db.close()

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

        self.name =Tk.StringVar()
        self.password =Tk.StringVar()
        self.Email=Tk.StringVar()
        self.var = Tk.IntVar()
        self.c=Tk.StringVar()

        self.entry_username =Tk.Entry(textvariable=self.name, font=(8))
        self.entry_password =Tk.Entry(textvariable=self.password, font=(8),show="*")
        self.label_username.place(x=45,y=55)
        self.label_password.place(x=45,y=85)
        self.entry_username.place(x=120, y=58)
        self.entry_password.place(x=120, y=88)

        Tk.Label (text ="", bg ="green",fg="brown",width="350",height="1",font=("tahoma",16)).place(x=0, y=185)
        self.makeButton()

    def makeButton (self):
        self.regbutton = Tk.Button(self.frameButton, text="Register",command=self.regis_form ,bg="green").grid(row=0, column=1)
        self.frameButton.place(x=110, y=150)
        self.logbtn = Tk.Button(self.frameButton1, text="Login",command=self.logInBttn,bg="blue").grid(row=0, column=1)
        self.frameButton1.place(x=230, y=150)

    def hide(self):
        """"""
        self.root.withdraw()

    def logInBttn(self, event=None):
        """"""
        with sqlite3.connect('student.db') as db:
            cursor = db.cursor()

        if self.name.get() == "" or self.password.get() == "":
            messagebox.showerror('Oops!','Please fill the form, or register !!')
        else:

            find_user = ('SELECT * FROM Student WHERE name = ? and password = ?')
            cursor.execute(find_user,[(self.name.get()),(self.password.get())])
            result = cursor.fetchall()
            if result:
                self.hide()
                subFrame = MainPage(self)
                self.name.set('')
                self.password.set('')
            else:
                messagebox.showerror('opps!!','Username or Password Invalid')
                self.name.set('')
                self.password.set('')

    def regis_form(self):
        self.hide()
        self.regis_form_s = Tk.Toplevel(root)
        # self.regis_form_s.geometry('350x350')
        width_s = 350
        height_s = 350
        self.regis_form_s.title("Registration Form")
        screen_width = self.regis_form_s.winfo_screenwidth()
        screen_height = self.regis_form_s.winfo_screenheight()
        x = (screen_width/2) - (width_s/2)
        y = (screen_height/2) - (height_s/2)
        self.regis_form_s.geometry('%dx%d+%d+%d' % (width_s, height_s, x, y))
        self.regis_form_s.resizable(0, 0)
        self.regis_form_s.iconbitmap(r'reg.ico')

        def new_user():
            username=self.name.get()
            email=self.Email.get()
            gender=self.var.get()
            country=self.c.get()
            password=self.password.get()
            with sqlite3.connect('student.db') as db:
                cursor = db.cursor()

            #Find Existing username if any take proper action
            if self.name.get() == "" or self.password.get() == "" or self.var.get()=="" or self.Email.get()=="" or self.c.get()=="":
                messagebox.showerror('Error!',"The form can't be empty !!")
                # self.regis_form()
            else :
                find_user = ('SELECT * FROM Student WHERE name = ?')
                cursor.execute(find_user,[(self.name.get())])        
                if cursor.fetchall():
                    messagebox.showerror('Error!','Username Already exis')
                    self.regis_form()
                else:
                    messagebox.showinfo('Success!','Account Created!')
                    self.regis_form_s.destroy()
                    self.root.update()
                    self.root.deiconify()

                cursor.execute('INSERT INTO Student (name,Email,Gender,country,password) VALUES(?,?,?,?,?)',(username,email,gender,country,password,))
                db.commit()
                self.name.set('')
                self.Email.set('')
                self.password.set('')

                                 
        Tk.Label(self.regis_form_s,bg ="green", text="Registration Form",width=30,font=("tahoma", 20)).pack()
        Tk.Label(self.regis_form_s,bg ="green", text="",width=30,font=("tahoma", 20)).place(x=0,y=330)
        Tk.Label(self.regis_form_s, text="Full Name",width=20,font=("bold", 10)).place(x=10,y=70)
        Tk.Entry(self.regis_form_s,textvar=self.name).place(x=170,y=70)
        Tk.Label(self.regis_form_s, text="Email",width=20,font=("bold", 10)).place(x=10,y=110)
        Tk.Entry(self.regis_form_s,textvar=self.Email).place(x=170,y=110)
        Tk.Label(self.regis_form_s, text="Gender",width=20,font=("bold", 10)).place(x=10,y=150)

        Tk.Radiobutton(self.regis_form_s, text="Male",padx = 5, variable=self.var, value=1).place(x=170,y=150)
        Tk.Radiobutton(self.regis_form_s, text="Female",padx = 20, variable=self.var, value=2).place(x=225,y=150)

        Tk.Label(self.regis_form_s, text="country",width=20,font=("bold", 10)).place(x=10,y=200)
        Tk.Entry(self.regis_form_s,textvar=self.password).place(x=175,y=250)
        Tk.Label(self.regis_form_s, text="Password",width=20,font=("bold", 10)).place(x=8,y=250)

        list1 = ['Indonesia','India','Malaysia','Taiwan','Thailand','Vietnam'];

        droplist=Tk.OptionMenu(self.regis_form_s,self.c, *list1)
        droplist.config(width=15)
        self.c.set('select your country') 
        droplist.place(x=170,y=200)

        Tk.Button(self.regis_form_s, text='Submit',width=20,bg='brown',fg='white',command=new_user).place(x=110,y=290)
            

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
        self.iconbitmap(r'11.ico')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 750
        height = 450
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.resizable(0, 0)
        self.configure(background='brown')
        self.title("MainPage")
        Tk.Label (self,text ="VIEW SCORE", bg ="grey",fg="black",width="600",height="1",font=("calibri",20)).pack() 
        # Tk.Label (self,text ="Please Set The Requiretment for make grading automaticly bellow this",fg="red",font=("tahoma",14)).place(x=70,y=55)
        # Tk.Label (self,text ="Result",fg="blue",font=("tahoma",14)).place(x=520,y=55)
        Tk.Label (self,text ="compiled by : Haryanto (M07158031)",bg ="grey",
            fg="red",width="750",height="1",font=("tahoma",9)).place(x=0,y=440)

        self.ButtonInPage()

    def ButtonInPage (self):
        Tk.Button(self, text="Logout",command=self.backLoginPage).place(x=620, y=405)
        Tk.Entry(self, width = 30 ).place(x=225, y=300)
        Tk.Button(self,relief='raised', text="Check", command=self.check_button).place(x=525, y=300)
        Tk.Button(self,relief='raised', text="exit", command=self.quit_t).place(x=685, y=405)
        Tk.Button(self, text = "Send", height = 4, width = 20,bg="blue").place(x=325, y=335)
 
    def backLoginPage(self):
        """"""
        self.destroy()
        self.mainPageFrame.logOut()

    def check_button(self):
        pass
        # try :
        #     tipeFile = (('image files', '*.jpg'), ('png files', '*.png'), ('all files', '*'))
        #     self.path = filedialog.askopenfilename(filetypes=tipeFile)
        # except :
        #     messagebox.showwarning("error","wrong format media, please check again")

         
    def quit_t(self):
        answer = messagebox.askquestion('', "Are you sure want to exit ?" )
        if answer == 'yes':
            self.quit()
        elif answer == 'no':  # 'no'
            pass

def main ():
    global root
    root = Tk.Tk()
    root.bind('<Escape>', lambda e: root.quit())
    root.iconbitmap(r'1234.ico')
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