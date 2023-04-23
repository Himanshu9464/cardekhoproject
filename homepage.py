from tkinter import *
from tkinter import messagebox

from Report1 import carReport1page
from Report2 import carReport2page
from aboutme import aboutmeclass
from brandType import brandTypeclass
from customerBpage import customerBpage
from customerSpage import customerSpage
from faculty import facultyPageclass
from inventoryc import carInventorypage
from inventorys import carInventorySpage


class HomepageClass:
    def __init__(self,uname,utype):
        self.uname = uname
        self.utype = utype
        self.window = Tk()
        self.window.title("Car Dekho")
        # ---------- settings ------------------
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = int(self.w / 2)
        h1 = int(self.h / 2)
        w_x1 = w1 - w1 / 2
        h_y1 = h1 - h1 / 2
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, w_x1, h_y1))  # (width,height,x,y)
        self.window.minsize(w1, h1)
        self.window.state('zoomed')
        c1="#DF07BB"
        c2="#0033A9"
        # ----------------- background image ----------------------------
        from PIL import Image, ImageTk
        self.bkimg1 = Image.open("my_images//carbg.jpg").resize((self.w, self.h))
        self.bkimg2 = ImageTk.PhotoImage(self.bkimg1)
        self.bkimglbl = Label(self.window, image=self.bkimg2)
        self.bkimglbl.place(x=0, y=0)

        # ------- menus ----------
        self.window.option_add("*TearOff", False)
        self.menubar = Menu()
        self.window.config(menu=self.menubar)
        self.menu1 = Menu(self.menubar)
        self.menu2 = Menu(self.menubar)
        self.menu3 = Menu(self.menubar)
        self.menu4 = Menu(self.menubar)
        self.menu5 = Menu(self.menubar)
        self.menu6 = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu1, label="Customer")

        self.menubar.add_cascade(menu=self.menu2, label="Inventory")
        self.menubar.add_cascade(menu=self.menu3, label="Reports")
        self.menubar.add_cascade(menu=self.menu4, label="Add Faculty")
        self.menubar.add_cascade(menu=self.menu5, label="About Me")
        self.menubar.add_cascade(menu=self.menu6, label="Logout")
        self.menu4.add_command(label="Faculty",foreground=c1, command=lambda: facultyPageclass(self.window))
        self.menu1.add_command(label="Sell Car",foreground=c1, command=lambda: customerSpage(self.window))
        self.menu1.add_command(label="Buy Car",foreground=c1, command=lambda: customerBpage(self.window))
        self.menu2.add_command(label="Add Brand",foreground=c1, command=lambda: brandTypeclass(self.window))
        self.menu2.add_command(label="Instock",foreground=c1, command=lambda: carInventorypage(self.window))
        self.menu2.add_command(label="Sold",foreground=c1, command=lambda: carInventorySpage(self.window))
        self.menu3.add_command(label="All Stock",foreground=c1, command=lambda: carReport1page(self.window))
        self.menu3.add_command(label="Sold Stock",foreground=c1, command=lambda: carReport2page(self.window))
        self.menu5.add_command(label="About Me",foreground=c1, command=lambda: aboutmeclass(self.window))
        self.menu6.add_command(label="Logout",foreground=c1,command=lambda :self.quitter())
        if self.utype == "Employee":
            self.menu4.entryconfig(0, state='disabled')
        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Logout ?", parent=self.window)
        if (ans == "yes"):
            self.window.destroy()
            from loginPage import loginpageClass
            loginpageClass()

        self.window.mainloop()

if __name__ == '__main__':
 HomepageClass()



