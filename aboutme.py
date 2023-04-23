from tkinter import *
from tkinter import messagebox

import pymysql as pymysql

class aboutmeclass:

    def __init__(self,hp_window):#
        # self.window = Tk()
        self.window = Toplevel(hp_window)
        self.window.title("About Me")
        #********* settings **********
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = int(self.w / 2)
        h1 = int(self.h / 2)

        w_x1 = w1 - w1 / 2
        h_y1 = h1 - h1 / 2
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, w_x1, h_y1))  # (width,height,x,y)
        self.window.minsize(w1, h1)
        self.window.config(background="#914DF7")
        #*********background image*********
        from PIL import Image, ImageTk
        self.bkimg1 = Image.open("my_images//img.JPG").resize((self.w, self.h))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0, y=0)
        myfont1=("Cambria", 15)
        mycolor1="#0033A9"
        mycolor2 ="#6A14FF"
        mycolor3 ="White"
        self.headlbl = Label(self.window, text="About Me", background="Light Blue", font=("Cambria", 35),
                             foreground=mycolor1, borderwidth=10, relief="groove")

        self.L1 = Label(self.window, text="Project→ Car Showroom Management", foreground=mycolor2, font=myfont1)
        self.L2 = Label(self.window, text="This project is made by Himanshu Sharma", foreground=mycolor2, font=myfont1)
        # **********Placements*********
        self.headlbl.place(x=0, y=0, width=w1, height=80)
        x1 = 50
        y1 = 100
        h_diff = 150
        v_diff = 50

        self.L1.place(x=x1, y=y1)
        self.L2.place(x=x1, y=y1+28)
        self.window.mainloop()

if __name__ == '__main__':
    dummyHomepage=Tk()
    aboutmeclass(dummyHomepage)
    dummyHomepage.mainloop()
    # facultyPageclass()