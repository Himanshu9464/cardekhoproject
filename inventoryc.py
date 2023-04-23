from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
import pymysql
from tkcalendar import DateEntry
from PIL import Image,ImageTk

class carInventorypage:                    #BUY FROM CUSTOMER
    default_img_name = "images.png"
    def __init__(self,hp_window):

        # self.window = Tk()   #To create independent window
        self.window=Toplevel(hp_window)

        self.window.title("Inventory")
        # ---------- settings ------------------
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()

        w1 = self.w -100
        h1 = self.h -150

        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50,50))  # (width,height,x,y)
        self.window.minsize(w1, h1)

        #----------------- background image ----------------------------
        from PIL import Image,ImageTk
        self.bkimg1 = Image.open("my_images//ic.jpg").resize((self.w,self.h))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0,y=0)

        #---------------------widgets ----------------
        myfont1 = ("Cambria",15)
        mycolor1 = "#E7E6FC"  #Alternatives
        mycolor2 = "#2C22FE"
        mycolor3 = "White"

        self.window.config(background=mycolor1)
        self.headlbl =Label(self.window,text="Car's Inventory",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")

        self.L1 =Label(self.window,text="Car Brand",background=mycolor1,font=myfont1)
        self.v1=StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v1,state="readonly",font=myfont1)

        self.imglbl = Label(self.window, relief="groove", borderwidth=1)

        #------------ table ---------------------------

        self.mytable1 = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13'],height=12)

        self.mytable1.heading("c1",text="Cust. Name")
        self.mytable1.heading("c2",text="Phone")
        self.mytable1.heading("c3",text="Gender")
        self.mytable1.heading("c4",text="Dob")
        self.mytable1.heading("c5",text="Address")
        self.mytable1.heading("c6",text="Aadhaar Id")
        self.mytable1.heading("c7",text="Car Brand")
        self.mytable1.heading("c8",text="Category")
        self.mytable1.heading("c9",text="Car Name")
        self.mytable1.heading("c10",text="Registration")
        self.mytable1.heading("c11",text="Manufacturing")
        self.mytable1.heading("c12",text="Fuel Type")
        self.mytable1.heading("c13",text="Price")

        self.mytable1['show']='headings'
        self.mytable1.column("#1",width=85,anchor="center")
        self.mytable1.column("#2",width=85,anchor="center")
        self.mytable1.column("#3",width=85,anchor="center")
        self.mytable1.column("#4",width=85,anchor="center")
        self.mytable1.column("#5",width=85,anchor="center")
        self.mytable1.column("#6",width=85,anchor="center")
        self.mytable1.column("#7",width=85,anchor="center")
        self.mytable1.column("#8",width=85,anchor="center")
        self.mytable1.column("#9",width=85,anchor="center")
        self.mytable1.column("#10",width=85,anchor="center")
        self.mytable1.column("#11",width=85,anchor="center")
        self.mytable1.column("#12",width=85,anchor="center")
        self.mytable1.column("#13",width=85,anchor="center")

        self.mytable1.bind("<ButtonRelease>",lambda e: self.getpkValue())
        #----------- buttons -----------------------
        self.b2 = Button(self.window,text="Search",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.searchData)

        #----------------- placements ----------------------------

        self.headlbl.place(x=0,y=0,width=self.w,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=46

        self.L1.place(x=x1,y=y1)
        self.c1.place(x=x1+h_diff,y=y1)
        self.b2.place(x=x1+h_diff+250,y=y1,height=30)
        y1+=v_diff
        self.mytable1.place(x=x1,y=y1)
        y1+=v_diff
        self.imglbl.place(x=x1 +50, y=y1 +240, height=300, width=300)

        self.databaseconnection()
        self.getAllBrand()

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

    def searchData(self):
        try:
            qry = "select * from buyc where brand like %s and avail=1"
            rowcount = self.curr.execute(qry,(self.v1.get()+"%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                for row in data:
                    self.mytable1.insert("", END, values=row)

            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def getpkValue(self):
        rowID = self.mytable1.focus()
        data = self.mytable1.item(rowID)
        mycontent = data['values']
        pkValue = mycontent[6]
        self.fetchData(pkValue)

    def fetchData(self,pk_value=None):
        if pk_value==None:
            brand=self.v1.get()
        else:
            brand=pk_value
        try:
            qry = "select * from buyc where brand = %s"
            rowcount = self.curr.execute(qry,(brand))
            data = self.curr.fetchone()
            if data:
                self.v1.set(data[6])
                self.actualname=data[13]
                self.oldname = data[13]

                self.img1 = Image.open("customerimages//" + self.oldname).resize((300, 300))
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def getAllBrand(self):
        try:
            qry = "select * from brands"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            self.brandList=[]
            if data:
                self.c1.set("Choose Brand")
                for row in data:
                    self.brandList.append(row[0])
            else:
                self.c1.set("No Brand")
            self.c1.config(values=self.brandList)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)


if __name__ == '__main__':
    dummyHomepage=Tk()
    carInventorypage(dummyHomepage)
    dummyHomepage.mainloop()

