from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql
class loginpageClass:
    def __init__(self):
        self.window = Tk()
        self.window.title("Car Dekho/Login")
        # ---------- settings ------------------
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = int(self.w / 2)
        h1 = int(self.h / 2)

        w_x1 = w1 - w1 / 2
        h_y1 = h1 - h1 / 2
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, w_x1, h_y1))  # (width,height,x,y)
        self.window.minsize(w1, h1)
        # ----------------- background image ----------------------------
        from PIL import Image, ImageTk
        self.bkimg1 = Image.open("my_images//lbg.jpg").resize((w1, h1))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0, y=0)
        # ---------------------widgets ----------------
        mycolor1 = "#E7E6FC"
        mycolor2 = "#2C22FE"
        mycolor3 = "white"
        myfont1 = ("Cambria", 15)

        self.window.config(background=mycolor1)
        self.headlbl = Label(self.window, text="Welcome to Car Dekho", background=mycolor2,
                             font=("Cambria", 35),
                             foreground=mycolor3, borderwidth=10, relief="groove")

        self.L1 = Label(self.window, text="Username", background=mycolor1, font=myfont1)
        self.L2 = Label(self.window, text="Password", background=mycolor1, font=myfont1)

        self.t1 = Entry(self.window, font=myfont1)
        self.t2 = Entry(self.window, font=myfont1, show="*")
        # ----------- buttons -----------------------
        self.b1 = Button(self.window, text="Login", foreground=mycolor3,
                         background=mycolor2, font=myfont1, command=self.checkData)
        # ----------------- placements ----------------------------

        self.headlbl.place(x=0, y=0, width=w1, height=80)
        x1 = 50
        y1 = 100
        h_diff = 150
        v_diff = 50

        self.L1.place(x=x1, y=y1)
        self.t1.place(x=x1 + h_diff, y=y1)
        y1 += v_diff
        self.L2.place(x=x1, y=y1)
        self.t2.place(x=x1 + h_diff, y=y1)

        y1 += v_diff
        self.b1.place(x=x1, y=y1, height=40, width=100)

        self.databaseconnection()
        self.clearPage()
        self.window.mainloop()

    def databaseconnection(self):
        myhost = "localhost"
        mydb = "cardekho"
        myuser = "root"
        mypassword = ""
        try:
            self.conn = pymysql.connect(host=myhost, db=mydb, user=myuser, password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error ", "Error in Database Connection: \n" + str(e), parent=self.window)

    def checkData(self):
        try:
            qry = "select * from facultytable where username=%s and password=%s"
            rowcount = self.curr.execute(qry, (self.t1.get(), self.t2.get()))
            data = self.curr.fetchone()
            self.conn.commit()
            if data:
                uname=data[5]
                utype=data[7]
                messagebox.showinfo("Success ", "Welcome "+utype, parent=self.window)
                self.window.destroy()
                from homepage import HomepageClass
                HomepageClass(uname,utype)
            else:
                messagebox.showwarning("Failure", "Wrong username or Password", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)


if __name__ == '__main__':
    loginpageClass()


