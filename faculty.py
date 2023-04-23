from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from tkcalendar import DateEntry

import pymysql as pymysql

class facultyPageclass:

    def __init__(self,hp_window):#
        # self.window = Tk()
        self.window = Toplevel(hp_window)
        self.window.title("Add Faculty")
        #********* settings **********
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = self.w - 250
        h1 = self.h - 220
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50, 50))  # (width,height,x,y)
        self.window.minsize(w1, h1)
        #*********background image*********
        from PIL import Image, ImageTk
        self.bkimg1 = Image.open("my_images//bg1").resize((self.w, self.h))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0, y=0)
        myfont1=("Cambria", 15)
        mycolor1="#0033A9"
        mycolor2 ="#6A14FF"
        mycolor3 ="White"
        self.headlbl = Label(self.window, text="Faculty", background="Light Blue", font=("Cambria", 35),
                             foreground=mycolor1, borderwidth=10, relief="groove")

        self.L1 = Label(self.window, text="Name", foreground=mycolor2, font=myfont1)
        self.L2 = Label(self.window, text="Phone", foreground=mycolor2, font=myfont1)
        self.L3 = Label(self.window, text="Gender",foreground=mycolor2 , font=myfont1)
        self.L4 = Label(self.window, text="DOB", foreground=mycolor2, font=myfont1)
        self.L5 = Label(self.window, text="Address", foreground=mycolor2, font=myfont1)
        self.L6 = Label(self.window, text="Username", foreground=mycolor2, font=myfont1)
        self.L7 = Label(self.window, text="Password", foreground=mycolor2, font=myfont1)
        self.L8 = Label(self.window, text="Usertype", foreground=mycolor2, font=myfont1)

        self.b1 = Button(self.window, text="Save", foreground=mycolor1, background=mycolor3, font=myfont1,
                         command=self.saveData)
        self.b2 = Button(self.window, text="Fetch", foreground=mycolor1,background=mycolor3, font=myfont1,
                         command=self.fetchData)
        self.b3 = Button(self.window, text="update", foreground=mycolor1,background=mycolor3, font=myfont1,
                         command=self.updateData)
        self.b4 = Button(self.window, text="Delete", foreground=mycolor1,background=mycolor3, font=myfont1,
                         command=self.deleteData)
        self.b5 = Button(self.window, text="Search", foreground=mycolor1,background=mycolor3, font=myfont1,
                         command=self.searchData)

        self.t1 =Entry(self.window,font=myfont1)
        self.t2=Entry(self.window,font=myfont1)
        self.v1=StringVar()
        self.r1 = Radiobutton(self.window, text="Male", value="Male", variable=self.v1, font=myfont1,
                              background="Light Blue")
        self.r2 = Radiobutton(self.window, text="Female", value="Female", variable=self.v1, font=myfont1,
                              background="Light Blue")
        self.t4 = DateEntry(self.window, background='darkblue',
                            foreground='white', borderwidth=2, year=2010, date_pattern='yy-mm-dd', font=myfont1)
        self.t5 = Text(self.window,font=myfont1,width=20,height=3)
        self.t6 = Entry(self.window, font=myfont1)
        self.t7=Entry(self.window,font=myfont1)
        self.v2=StringVar()
        self.c1 = Combobox(self.window,values=["Admin","Employee"],textvariable=self.v2,state="readonly",font=myfont1)

        #******Table
        self.mytable1 = Treeview(self.window, columns=['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'], height=10)

        self.mytable1.heading("c1", text="Name")
        self.mytable1.heading("c2", text="Phone")
        self.mytable1.heading("c3", text="Gender")
        self.mytable1.heading("c4", text="DOB")
        self.mytable1.heading("c5", text="Address")
        self.mytable1.heading("c6", text="Username")
        self.mytable1.heading("c7", text="Usertype")

        self.mytable1['show'] = 'headings'
        self.mytable1.column("#1", width=100, anchor="center")
        self.mytable1.column("#2", width=100, anchor="center")
        self.mytable1.column("#3", width=100, anchor="center")
        self.mytable1.column("#4", width=100, anchor="center")
        self.mytable1.column("#5", width=100, anchor="center")
        self.mytable1.column("#6", width=100, anchor="center")
        self.mytable1.column("#7", width=100, anchor="center")

        self.mytable1.bind("<ButtonRelease>", lambda e: self.getpkValue())

        # **********Placements*********
        self.headlbl.place(x=0, y=0, width=w1, height=80)
        x1 = 50
        y1 = 100
        h_diff = 150
        v_diff = 50

        self.L1.place(x=x1, y=y1)
        self.t1.place(x=x1 + h_diff, y=y1)

        self.mytable1.place(x=x1+h_diff+350,y=y1)
        self.b5.place(x=x1+h_diff+250,y=y1,height=30)
        y1 += v_diff
        self.L2.place(x=x1, y=y1)
        self.t2.place(x=x1 + h_diff, y=y1)
        y1 += v_diff
        self.L3.place(x=x1, y=y1)
        self.r1.place(x=x1 + h_diff, y=y1)
        self.r2.place(x=x1 + h_diff + h_diff, y=y1)
        y1 += v_diff
        self.L4.place(x=x1, y=y1)
        self.t4.place(x=x1 + h_diff, y=y1)
        y1 += v_diff
        self.L5.place(x=x1, y=y1)
        self.t5.place(x=x1 + h_diff, y=y1)
        y1 += v_diff
        y1 += v_diff
        self.L6.place(x=x1, y=y1)
        self.t6.place(x=x1 + h_diff, y=y1)
        self.b2.place(x=x1 + h_diff+ h_diff+ h_diff-50 , y=y1,height=35)
        y1 += v_diff
        self.L7.place(x=x1, y=y1)
        self.t7.place(x=x1+h_diff,y=y1)
        y1 += v_diff
        self.L8.place(x=x1, y=y1)
        self.c1.place(x=x1 + h_diff, y=y1)
        y1 += v_diff

        self.b1.place(x=x1,y=y1)
        self.b3.place(x=x1 + h_diff, y=y1)
        self.b4.place(x=x1 + h_diff+ h_diff, y=y1)
        # self.b6.place(x=x1 + h_diff+ h_diff, y=y1)

        self.databaseconnection()
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

    def saveData(self):
        if self.checkValidation()==False:
            return
        try:
            qry = "insert into facultytable values(%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry, (self.t1.get(), self.t2.get(), self.v1.get(),self.t4.get(),
                                                self.t5.get('1.0', END), self.t6.get(), self.t7.get(), self.v2.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success ", "Member Added Successfully", parent=self.window)
                self.clearPage()

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def updateData(self):
        if self.checkValidation()==False:
            return
        try:
            qry = "update facultytable set name=%s, phone=%s , gender=%s , dob=%s, address=%s, " \
                  "password=%s , usertype=%s where username=%s"
            rowcount = self.curr.execute(qry, (self.t1.get(), self.t2.get(), self.v1.get(),self.t4.get(),
                                                self.t5.get('1.0', END), self.t7.get(), self.v2.get(), self.t6.get()))
            self.conn.commit()
            if rowcount == 1:
                messagebox.showinfo("Success ", "Member Updated Successfully", parent=self.window)
                self.clearPage()

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation", "Are you to delete ?", parent=self.window)
        if (ans == "yes"):
            try:
                qry = "delete from facultytable where username=%s"
                rowcount = self.curr.execute(qry, (self.t6.get()))
                self.conn.commit()
                if rowcount == 1:
                    messagebox.showinfo("Success ", "Student deleted Successfully", parent=self.window)
                    self.clearPage()

            except Exception as e:
                messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def getpkValue(self):
        rowID = self.mytable1.focus()
        data = self.mytable1.item(rowID)
        mycontent = data['values']
        pkValue = mycontent[5]
        self.fetchData(pkValue)

    def fetchData(self,pk_value=None):
        if pk_value == None:
            username = self.t6.get()
        else:
            username = pk_value
        try:
            qry = "select * from facultytable where username = %s"
            rowcount = self.curr.execute(qry, (username))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0, data[0])
                self.t2.insert(0, data[1])
                self.v1.set(data[2])
                self.t4.set_date(data[3])
                self.t5.insert('1.0', data[4])
                self.t6.insert(0, data[5])
                self.t7.insert(0, data[6])
                self.v2.set(data[7])

                self.b3['state'] = 'normal'
                self.b4['state'] = 'normal'
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.v1.set(None)
        self.t4.delete(0, END)
        self.t5.delete('1.0', END)
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.c1.set("Choose Usertype")

        self.b3['state']='disable'
        self.b4['state']='disable'

        self.searchData()

    def searchData(self):
        try:
            qry = "select * from facultytable where name like %s"
            rowcount = self.curr.execute(qry, (self.t1.get() + "%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                for row in data:
                    self.mytable1.insert("", END, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[7]))
            else:
                messagebox.showinfo("Failure", "No Record Found", parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e), parent=self.window)

    def checkValidation(self):
        if len(self.t1.get())<1 :
            messagebox.showwarning("Validation Check","Enter Proper Name",parent=self.window)
            return False
        elif len(self.t2.get())<7 or len(self.t2.get())>15 or not self.t2.get().isdigit():
            messagebox.showwarning("Validation Check","Enter Proper Phone no\n[7-15 digits] ",parent=self.window)
            return False
        elif not( self.v1.get()=="Male" or self.v1.get()=="Female"):
            messagebox.showwarning("Validation Check","Select Gender ",parent=self.window)
            return False
        elif self.t4.get()=="":
            messagebox.showwarning("Validation Check","Select DOB ",parent=self.window)
            return False
        elif len(self.t5.get('1.0',END))<2:
            messagebox.showwarning("Validation Check","Enter Address ",parent=self.window)
            return False
        return True

if __name__ == '__main__':
    dummyHomepage=Tk()
    facultyPageclass(dummyHomepage)
    dummyHomepage.mainloop()
    # facultyPageclass()