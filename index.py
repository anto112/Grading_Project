# from tkinter import *
# import sqlite3

# root = Tk()
# root.title("Python: Simple Login Application")
# width = 400
# height = 280
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# x = (screen_width/2) - (width/2)
# y = (screen_height/2) - (height/2)
# root.geometry("%dx%d+%d+%d" % (width, height, x, y))
# root.resizable(0, 0)

# #==============================METHODS========================================
# def Database():
#     global conn, cursor
#     conn = sqlite3.connect("database.db")
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
#     cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
#     if cursor.fetchone() is None:
#         cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
#         conn.commit()
    
# def Login(event=None):
#     Database()


#     if USERNAME.get() == "" or PASSWORD.get() == "":
#         lbl_text.config(text="Please complete the required field!", fg="red")
#     else:
#         cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
#         if cursor.fetchone() is not None:
#             HomeWindow()
#             USERNAME.set("")
#             PASSWORD.set("")
#             lbl_text.config(text="")
#         else:
#             lbl_text.config(text="Invalid username or password", fg="red")
#             USERNAME.set("")
#             PASSWORD.set("")   
#     cursor.close()
#     conn.close()

# def HomeWindow():
#     global Home
#     root.withdraw()
#     Home = Toplevel()
#     Home.title("Python: Simple Login Application")
#     width = 600
#     height = 500
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     x = (screen_width/2) - (width/2)
#     y = (screen_height/2) - (height/2)
#     root.resizable(0, 0)
#     Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
#     lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
#     btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

# def Back():
#     Home.destroy()
#     root.deiconify()
    
# #==============================VARIABLES======================================
# USERNAME = StringVar()
# PASSWORD = StringVar()

# #==============================FRAMES=========================================
# Top = Frame(root, bd=2,  relief=RIDGE)
# Top.pack(side=TOP, fill=X)
# Form = Frame(root, height=200)
# Form.pack(side=TOP, pady=20)

# #==============================LABELS=========================================
# lbl_title = Label(Top, text = "Python: Simple Login Application", font=('arial', 15))
# lbl_title.pack(fill=X)
# lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
# lbl_username.grid(row=0, sticky="e")
# lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
# lbl_password.grid(row=1, sticky="e")
# lbl_text = Label(Form)
# lbl_text.grid(row=2, columnspan=2)

# #==============================ENTRY WIDGETS==================================
# username = Entry(Form, textvariable=USERNAME, font=(14))
# username.grid(row=0, column=1)
# password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
# password.grid(row=1, column=1)

# #==============================BUTTON WIDGETS=================================
# btn_login = Button(Form, text="Login", width=45, command=Login)
# btn_login.grid(pady=25, row=3, columnspan=2)
# btn_login.bind('<Return>', Login)





# #==============================INITIALIATION==================================
# if __name__ == '__main__':
#     root.mainloop()
from tkinter import *
from tkinter import messagebox as ms
import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

#main Class
class main:
    def __init__(self,master):
        # Window 
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
        #Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
        #Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methords
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN',font = ('',35),pady = 10)
        self.head.pack()
        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()
        
        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    

#create window and application object
root = Tk()
#root.title("Login Form")
main(root)
root.mainloop()