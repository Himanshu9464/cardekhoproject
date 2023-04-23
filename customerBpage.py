from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox, Treeview
import pymysql
from tkcalendar import DateEntry
from PIL import Image,ImageTk

class customerBpage:                    #BUY FROM CUSTOMER
    default_img_name = "images.png"
    avail=1
    def __init__(self,hp_window):

        # self.window = Tk()   #To create independent window
        self.window=Toplevel(hp_window)

        self.window.title("Buy From Customer")
        # ---------- settings ------------------
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()

        w1 = self.w -100
        h1 = self.h -150

        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 50,50))  # (width,height,x,y)
        self.window.minsize(self.w, self.h)
        self.window.state('zoomed')

        #----------------- background image ----------------------------
        from PIL import Image,ImageTk
        self.bkimg1 = Image.open("my_images//buybg").resize((self.w,self.h))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0,y=0)

        # ---------------------------------------------------------------
        #---------------------widgets ----------------
        # mycolor1 = "#0033A9"
        # mycolor2 = "#6A14FF"
        # mycolor3 = "white"
        myfont1 = ("Cambria",15)
        mycolor1 = "#E7E6FC"  #Alternatives
        mycolor2 = "#2C22FE"
        mycolor3 = "White"

        self.window.config(background=mycolor1)
        self.headlbl =Label(self.window,text="Buy From Customer",background=mycolor2,font=("Cambria",35),
                            foreground=mycolor3,borderwidth=10,relief="groove")


        self.L1 =Label(self.window,text="Cust. Name",background=mycolor1,font=myfont1)
        self.L2 =Label(self.window,text="Phone",background=mycolor1,font=myfont1)
        self.L3 =Label(self.window,text="Gender",background=mycolor1,font=myfont1)
        self.L4 =Label(self.window,text="DOB",background=mycolor1,font=myfont1)
        self.L5 =Label(self.window,text="Address",background=mycolor1,font=myfont1)
        self.L6 =Label(self.window,text="Aadhaar ID",background=mycolor1,font=myfont1)
        self.L7 =Label(self.window,text="Car Brand",background=mycolor1,font=myfont1)
        self.L8 =Label(self.window,text="Category",background=mycolor1,font=myfont1)
        self.L9 =Label(self.window,text="Car Name",background=mycolor1,font=myfont1)
        self.L10=Label(self.window,text="Registration No.",background=mycolor1,font=myfont1)
        self.L11=Label(self.window,text="Manufact. Date",background=mycolor1,font=myfont1)
        self.L12=Label(self.window,text="Fuel Type",background=mycolor1,font=myfont1)
        self.L13=Label(self.window,text="Price Ask",background=mycolor1,font=myfont1)#After ml automatic price

        self.t1 = Entry(self.window,font=myfont1)
        self.t2 = Entry(self.window,font=myfont1)
        self.v1=StringVar()
        self.r1 = Radiobutton(self.window,text="Male",value="Male",variable=self.v1,font=myfont1,background=mycolor1)
        self.r2 = Radiobutton(self.window,text="Female",value="Female",variable=self.v1,font=myfont1,background=mycolor1)
        self.t4 = DateEntry(self.window,  background='darkblue',
                    foreground='white', borderwidth=2, year=2010,date_pattern='dd-mm-yy',font=myfont1)
        self.t5 = Text(self.window,font=myfont1,width=20,height=3)
        self.t6 = Entry(self.window, font=myfont1)
        self.v2=StringVar()
        self.c1 = Combobox(self.window,textvariable=self.v2,state="readonly",font=myfont1)
        self.v3=StringVar()
        self.c2 = Combobox(self.window,values=["Hatchback","Sedan","SUV","MUV"],textvariable=self.v3,state="readonly",font=myfont1)
        self.t9 = Entry(self.window, font=myfont1)
        self.t10 = Entry(self.window, font=myfont1)
        self.t11 = DateEntry(self.window,  background='darkblue',
                    foreground='white', borderwidth=2, year=2010,date_pattern='dd-mm-yy',font=myfont1)
        self.v4 = StringVar()
        self.c3 = Combobox(self.window, values=["Petrol", "Diesel", "Electric"], textvariable=self.v4,
                           state="readonly", font=myfont1)
        self.t13 = Entry(self.window, font=myfont1)

        #------------ table ---------------------------

        self.mytable1 = Treeview(self.window,columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11'],height=12)

        self.mytable1.heading("c1",text="Cust. Name")
        self.mytable1.heading("c2",text="Phone")
        self.mytable1.heading("c3",text="Gender")
        self.mytable1.heading("c4",text="Aadhaar Id")
        self.mytable1.heading("c5",text="Car Brand")
        self.mytable1.heading("c6",text="Category")
        self.mytable1.heading("c7",text="Car Name")
        self.mytable1.heading("c8",text="Registration")
        self.mytable1.heading("c9",text="Manufacturing")
        self.mytable1.heading("c10",text="Fuel Type")
        self.mytable1.heading("c11",text="Price")

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

        self.mytable1.bind("<ButtonRelease>",lambda e: self.getpkValue())

        #----------- buttons -----------------------

        self.b1 = Button(self.window,text="Save",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.saveData)
        self.b5 = Button(self.window,text="Fetch",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.fetchData)
        self.b3 = Button(self.window,text="update",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.updateData)
        self.b4 = Button(self.window,text="Delete",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.deleteData)
        self.b2 = Button(self.window,text="Search",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.searchData)
        self.b6 = Button(self.window,text="Upload",foreground=mycolor3,
                         background=mycolor2,font=myfont1,command=self.getImage)#

        self.imglbl = Label(self.window,relief="groove",borderwidth=1)

        #----------------- placements ----------------------------

        self.headlbl.place(x=0,y=0,width=self.w,height=80)
        x1 = 50
        y1=100
        h_diff=150
        v_diff=46

        self.L1.place(x=x1,y=y1)
        self.t1.place(x=x1+h_diff,y=y1)
        self.b2.place(x=x1+h_diff+250,y=y1,height=30)
        self.mytable1.place(x=x1+h_diff+350,y=y1)
        y1+=v_diff
        self.L2.place(x=x1,y=y1)
        self.t2.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L3.place(x=x1,y=y1)
        self.r1.place(x=x1+h_diff,y=y1)
        self.r2.place(x=x1+h_diff+h_diff,y=y1)
        y1+=v_diff
        self.L4.place(x=x1,y=y1)
        self.t4.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L5.place(x=x1,y=y1)
        self.t5.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        y1+=v_diff
        self.L6.place(x=x1,y=y1)
        self.t6.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L7.place(x=x1,y=y1)
        self.c1.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L8.place(x=x1,y=y1)
        self.c2.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L9.place(x=x1,y=y1)
        self.t9.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L10.place(x=x1,y=y1)
        self.t10.place(x=x1+h_diff,y=y1)
        self.b5.place(x=x1+h_diff+250,y=y1,height=30)
        y1+=v_diff
        self.L11.place(x=x1,y=y1)
        self.t11.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L12.place(x=x1,y=y1)
        self.c3.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.L13.place(x=x1,y=y1)
        self.t13.place(x=x1+h_diff,y=y1)
        y1+=v_diff
        self.b1.place(x=x1,y=y1,height=40,width=100)
        self.b3.place(x=x1+110,y=y1,height=40,width=100)
        self.b4.place(x=x1+220,y=y1,height=40,width=100)

        self.imglbl.place(x=x1+520,y=y1-310,height=300,width=300)
        self.b6.place(x=x1+520,y=y1,height=40,width=300)

        self.databaseconnection()
        self.clearPage()
        self.getAllBrand()
        self.window.mainloop()

    def getImage(self):
        self.filename = askopenfilename(file=[("All Pictures","*.png;*.jpg;*.jpeg"),
                                              ("PNG Images","*.png"),("JPG Images","*.jpg")],parent=self.window)
        if self.filename!="":
            self.img1 = Image.open(self.filename).resize((300,300))
            self.img2 = ImageTk.PhotoImage(self.img1)
            self.imglbl.config(image=self.img2)

            # make image name
            path = self.filename.split("/")
            name = path[-1]
            import time
            uniqness = str(int(time.time()))
            self.actualname = uniqness+name

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
        if self.checkValidation()==False:
            return

        if self.actualname==self.default_img_name:
            pass
        else:
            self.img1.save("customerimages//"+self.actualname)

        self.avail==1

        try:
            qry = "insert into buyc values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.v1.get(),self.t4.get_date(),self.t5.get('1.0',END),
                                              self.t6.get(), self.v2.get(),self.v3.get(),self.t9.get(),self.t10.get(),
                                              self.t11.get_date(),self.v4.get(),self.t13.get(),self.actualname,self.avail))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Customer's Car Added Successfully",parent=self.window)
                self.clearPage()

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def updateData(self):
        if self.checkValidation()==False:
            return # end function now

        if self.actualname==self.oldname: # no new image is selected
            # nothing to save or delete in folder
            pass
        else:
            self.img1.save("customerimages//"+self.actualname)
            if self.oldname==self.default_img_name: # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("customerimages//"+self.oldname)
        try:
            qry = "update buyc set name=%s, phone=%s , gender=%s , dob=%s, address=%s, " \
                  "aadhaar=%s, brand=%s, category=%s, cname=%s , md =%s ,ft =%s , price =%s , pic =%s where rn=%s "
            rowcount = self.curr.execute(qry,(self.t1.get(),self.t2.get(),self.v1.get(),self.t4.get_date(),self.t5.get('1.0',END),
                                              self.t6.get(), self.v2.get(),self.v3.get(),self.t9.get(),
                                              self.t11.get_date(),self.v4.get(),self.t13.get(),self.actualname,self.t10.get()))
            self.conn.commit()
            if rowcount==1:
                messagebox.showinfo("Success ","Customer Updated Successfully",parent=self.window)
                self.clearPage()

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def deleteData(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to delete ?",parent=self.window)
        if (ans=="yes"):

            if self.oldname==self.default_img_name: # no image was given in past
                # nothing to delete
                pass
            else:
                import os
                os.remove("customerimages//"+self.oldname)
            try:
                qry = "delete from buyc where rn=%s"
                rowcount = self.curr.execute(qry,(self.t10.get()))
                self.conn.commit()
                if rowcount==1:
                    messagebox.showinfo("Success ","Customer deleted Successfully",parent=self.window)
                    self.clearPage()

            except Exception as e:
                messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def getpkValue(self):
        rowID = self.mytable1.focus()
        data = self.mytable1.item(rowID)
        mycontent = data['values']
        pkValue = mycontent[7]
        self.fetchData(pkValue)

    def fetchData(self,pk_value=None):
        if pk_value==None:
            Rn=self.t10.get()
        else:
            Rn=pk_value
        try:
            qry = "select * from buyc where rn = %s"
            rowcount = self.curr.execute(qry,(Rn))
            data = self.curr.fetchone()
            self.clearPage()
            if data:
                self.t1.insert(0,data[0])
                self.t2.insert(0,data[1])
                self.v1.set(data[2])
                self.t4.set_date(data[3])
                self.t5.insert('1.0',data[4])
                self.t6.insert(0,data[5])
                self.v2.set(data[6])
                self.v3.set(data[7])
                self.t9.insert(0,data[8])
                self.t10.insert(0,data[9])
                self.t11.set_date(data[10])
                self.v4.set(data[11])
                self.t13.insert(0,data[12])
                self.actualname=data[13]
                self.oldname = data[13]

                self.img1 = Image.open("customerimages//" + self.oldname).resize((300, 300))
                self.img2 = ImageTk.PhotoImage(self.img1)
                self.imglbl.config(image=self.img2)

                self.b3['state'] = 'normal'
                self.b4['state'] = 'normal'
            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def clearPage(self):
        self.t1.delete(0,END)
        self.t2.delete(0,END)
        self.v1.set(None)
        self.t4.delete(0,END)
        self.t5.delete('1.0',END)
        self.t6.delete(0,END)
        self.c1.set("Choose Brand")
        self.c2.set("Choose Category")
        self.t9.delete(0,END)
        self.t10.delete(0,END)
        self.t11.delete(0,END)
        self.c3.set("Choose F Type")
        self.t13.delete(0,END)
        self.b3['state']='disable'
        self.b4['state']='disable'
        self.actualname=self.default_img_name
        self.img1 = Image.open("customerimages//"+self.default_img_name).resize((300, 300))
        self.img2 = ImageTk.PhotoImage(self.img1)
        self.imglbl.config(image=self.img2)

    def searchData(self):
        try:
            qry = "select * from buyc where name like %s and avail=1"
            rowcount = self.curr.execute(qry,(self.t1.get()+"%"))
            data = self.curr.fetchall()
            self.mytable1.delete(*self.mytable1.get_children())
            if data:
                for row in data:
                    self.mytable1.insert("",END,values=(row[0],row[1],row[2],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))

            else:
                messagebox.showinfo("Failure","No Record Found",parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error ","Error in Query: \n"+str(e),parent=self.window)

    def checkValidation(self):
        if len(self.t1.get()) < 1:
            messagebox.showwarning("Validation Check", "Enter Proper Name ", parent=self.window)
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
        elif len(self.t6.get())>12 or not self.t6.get().isdigit():
            messagebox.showwarning("Validation Check","Enter Proper Aadhaar ID\n[12 digits] ",parent=self.window)
            return False
        elif self.v2.get()=="Choose Brand" or self.v2.get()=="No Brand":
            messagebox.showwarning("Validation Check","Select Brand ",parent=self.window)
            return False
        elif self.v3.get()=="Choose Category" or self.v2.get()=="No Category":
            messagebox.showwarning("Validation Check","Select Category ",parent=self.window)
            return False
        if len(self.t9.get()) < 1:
            messagebox.showwarning("Validation Check", "Enter Proper Car Name ", parent=self.window)
            return False
        if len(self.t10.get()) < 1:
            messagebox.showwarning("Validation Check", "Enter Registeration No. Properly ", parent=self.window)
            return False
        elif self.t11.get()=="":
            messagebox.showwarning("Validation Check","Select Manufacturing Date ",parent=self.window)
            return False
        elif self.v4.get()=="Choose F Type" or self.v4.get()=="No F Type":
            messagebox.showwarning("Validation Check","Select F Type ",parent=self.window)
            return False
        if len(self.t13.get()) < 4:
            messagebox.showwarning("Validation Check", "Enter Price ", parent=self.window)
            return False
        return True

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
    customerBpage(dummyHomepage)
    dummyHomepage.mainloop()

