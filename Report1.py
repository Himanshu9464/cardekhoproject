import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

from printoutpage import my_cust_PDF

class carReport1page:
    def __init__(self,hp_window):

        # self.window = Tk()   #To create independent window
        self.window=Toplevel(hp_window)

        self.window.title("Report")
        # ---------- settings ------------------
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()

        w1 = self.w -100
        h1 = self.h -150

        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50,50))  # (width,height,x,y)
        self.window.minsize(w1, h1)

        #---------------------widgets ----------------
        myfont1 = ("Cambria",15)
        mycolor1 = "#E7E6FC"  #Alternatives
        mycolor2 = "#2C22FE"
        mycolor3 = "White"

        self.window.config(background=mycolor1)
        self.headlbl =Label(self.window,text="In-stock Report",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")
        self.b1 = Button(self.window, text="Print", foreground=mycolor3,
                        background=mycolor2, font=myfont1, command=self.getPrint)

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

        #----------------- placements ----------------------------

        self.headlbl.place(x=0,y=0,width=self.w,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=46

        self.mytable1.place(x=x1,y=y1)
        self.b1.place(x=self.w/2-150,y=y1+450,width=200,height=50)

        self.databaseconnection()
        self.searchData()
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
            qry = "select * from buyc where avail=1"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            self.printData = []
            if data:
                for row in data:
                    self.printData.append(row[:-1])
                    self.mytable1.insert("", END, values=row)
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def getPrint(self):
        pdf = my_cust_PDF()
        headings = ['CName','Phone No','Gender','DOB','Address','Aadhaar ID','Brand','Category','Car Name','Registeration','Manufacturing','Fuel Type','Price']
        pdf.print_chapter(self.printData, headings, 13)
        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')

if __name__ == '__main__':
    dummyHomepage=Tk()
    carReport1page(dummyHomepage)
    dummyHomepage.mainloop()

