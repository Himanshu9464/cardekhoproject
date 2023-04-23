from tkinter import *
from tkinter import messagebox
import pymysql
class MainClass:
    def __init__(self):

        self.databaseconnection()
        try:
            qry = "select * from facultytable"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchone()
            self.conn.commit()
            if data:
                from loginPage import loginpageClass
                loginpageClass()
            else:
                from faculty import facultyPageclass
                facultyPageclass()
        except Exception as e:
            messagebox.showerror("Query Error ", "Error in Query: \n" + str(e))

    def databaseconnection(self):
        myhost = "localhost"
        mydb = "cardekho"
        myuser = "root"
        mypassword = ""
        try:
            self.conn = pymysql.connect(host=myhost, db=mydb, user=myuser, password=mypassword)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error ", "Error in Database Connection: \n" + str(e))


if __name__ == '__main__':
    MainClass()


