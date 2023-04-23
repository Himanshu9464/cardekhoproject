from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

class brandTypeclass:
    def __init__(self,hp_window):
        self.window=Toplevel(hp_window)
        self.window.title("Cardekho/Brand")
        # ---------- settings ------------------
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = int(self.w / 2)
        h1 = int(self.h / 2)
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50,50))  # (width,height,x,y)
        self.window.minsize(w1, h1)
        from PIL import Image, ImageTk
        self.bkimg1 = Image.open("my_images//carbg1.jpg").resize((w1, h1))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0, y=0)

        #---------------------widgets ----------------
        mycolor1 = "#E7E6FC"
        mycolor2 = "#2C22FE"
        mycolor3 = "white"
        myfont1 = ("Cambria",15)

        self.window.config(background=mycolor1)
        self.headlbl =Label(self.window,text="Add Car Brand",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="Brand Name",background=mycolor1,font=myfont1)

        self.t1 = Entry(self.window,font=myfont1)
        #------------ table ---------------------------

        self.mytable1 = Treeview(self.window,columns=['c1'],height=12)

        self.mytable1.heading("c1",text="Department")

        self.mytable1['show']='headings'
        self.mytable1.column("#1",width=200,anchor="center")

        #----------- buttons -----------------------
        self.b1 = Button(self.window,text="Save",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.saveData)
        self.b2 = Button(self.window,text="Search",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.searchData)

        #----------------- placements ----------------------------

        self.headlbl.place(x=0,y=0,width=w1,height=80)
        x1 = 50
        y1=100
        h_diff=200
        v_diff=50

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+h_diff,y=y1)
        self.mytable1.place(x=x1+h_diff+250,y=y1)
        y1+=v_diff
        self.b1.place(x=x1,y=y1,height=40,width=100)
        self.b2.place(x=x1 + h_diff, y=y1, height=40,width=100)
        self.databaseconnection()
        self.clearPage()
        self.window.mainloop()


    def databaseconnection(self):
        myhost="localhost"
        mydb="cardekho"
        myuser="root"
        mypassword=""
        try:
            self.conn = pymysql.connect(host=myhost,db=mydb,user=myuser,password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error ","Error in Database Connection: \n"+str(e),parent=self.window)

    def saveData(self):
        try:
            qry = "insert into brands values(%s)"
            rowcount = self.curr.execute(qry,(self.t1.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Brand` Added Successfully",parent=self.window)
                self.clearPage()
        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)

    def searchData(self):
        try:
            qry = "select * from brands where brand like %s"
            rowcount = self.curr.execute(qry,(self.t1.get()+"%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                for row in data:
                    self.mytable1.insert("",END,values=row)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)


if __name__ == '__main__':
    dummyHomepage=Tk()
    brandTypeclass(dummyHomepage)
    dummyHomepage.mainloop()



