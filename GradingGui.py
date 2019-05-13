import tkinter as Tk
from tkinter import messagebox 
from tkinter import filedialog

class Main():

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
        Tk.Button(self, text = "Send", height = 8, width = 20,bg="blue").place(x=75, y=120)
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

if __name__ == "__main__":
    main()
