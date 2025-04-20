from tkinter import *
import math, random,os
from tkinter import messagebox,filedialog
import webbrowser
pro = Tk()
pro.resizable(False, False)
pro.title("Restaurant")
pro.iconbitmap('res.ico')
pro.geometry('650x450')
pro.config(bg='#EFE0BB') 

title = Label(pro, text='Restaurant System', fg='#002B5B', bg="#ECB390", font=("Quicksand", 18, 'bold'))
title.pack(fill=X)
def open_url(url):
    webbrowser.open(url, new=2)
def menu_window():#(nadeen)
    menu_window = Toplevel(pro)
    menu_window.resizable(TRUE, False)
    menu_window.geometry('800x700+30+10')
    menu_window.iconbitmap('menu.ico')
    menu_window.title("Menu")
    # adding frame for menu window (nadeen)
    frame = Frame(menu_window, bg='#FFFAF1', bd=-20, relief=RIDGE)
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    # adding title for frame (nadeen)
    label = Label(frame, text="Menu", font=('Lucida Calligraphy', 25, 'bold'), fg='#002B5B', bg='#ECB390')
    label.pack(pady=5)
    # adding main dishes (nadeen)
    main_dishes_label = Label(frame, text="Main Dishes", font=('Lucida Calligraphy', 20, 'bold'), fg='#ECB390', bg="#002B5B")
    main_dishes_label.place(relx=0.01,rely=0.07,anchor='nw')
    main_dishes = [
        ("SUPREME PIZZA", "$12.00"), ("MARGHARITA PIZZA", "$10.00"), ("SMOKE PIZZA", "$11.00"), 
        ("SEE RANCH PIZZA", "$13.00"), ("CLASSIC CHEESE BURGER", "$8.00"), ("MUSHROOM BURGER", "$9.00"), 
        ("SPICY BURGER", "$8.50"), ("TERIYAKI CHICKEN BOWL", "$12.50"), ("FETTUCCINE ALFREDO", "$11.50"), ("LASAGNA", "$13.50")
    ]
    y_position = 0.17 
    for dish, price in main_dishes:
         dish_label = Label(frame, text=f"{dish} - {price}", font=('Quicksand', 12), bg='#FFFAF1')
         dish_label.place(relx=0.01, rely=y_position, anchor='nw') 
         y_position += 0.05
    # adding appetizers (nadeen)
    appetizers_label = Label(frame, text="Appetizers", font=('Lucida Calligraphy', 20, 'bold'), fg='#ECB390', bg="#002B5B")
    appetizers_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    appetizers = [
        ("Chicken Tenders", "$5.00"), ("Crunchy", "$4.00"), ("Buffalo Wings", "$6.00"), ("French Fries", "$3.00"),
        ("Onion Rings", "$4.50"), ("Spring Rolls", "$5.00"), ("Dumplings", "$5.50"), ("Vegan Nachos", "$6.50")
    ]
    y_position = 0.2
    for appetizer, price in appetizers:
        appetizer_label = Label(frame, text=f"{appetizer} - {price}", font=('Quicksand', 12),bg='#FFFAF1')
        appetizer_label.place(relx=0.5, rely=y_position, anchor=CENTER)
        y_position += 0.05

    # adding sides
    sides_label = Label(frame, text="Sides", font=('Lucida Calligraphy', 20, 'bold'), fg='#ECB390', bg="#002B5B", padx=40)
    sides_label.place(rely=0.07, relx=0.99, anchor='ne')
    sides = [
        ("Pepsi", "$3.00"), ("Coleslaw", "$2.50"), ("Caesar Salad", "$4.00"), ("Sweet Potato", "$3.50")]
    y_position = 0.2
    for side, price in sides:
        side_label = Label(frame, text=f"{side} - {price}", font=('Quicksand', 12),padx=30,bg='#FFFAF1')
        side_label.place(relx=0.93, rely=y_position, anchor=CENTER)
        y_position += 0.05

    # adding desserts  
    desserts_label = Label(frame, text="Desserts", font=('Lucida Calligraphy', 20, 'bold'), fg='#ECB390', bg="#002B5B", padx=25)
    desserts_label.place(relx=0.5, rely=0.64, anchor=CENTER)
    desserts = [
        ("Apple Pie", "$4.00"), ("Milkshakes (Vanilla, Chocolate, Strawberry)", "$5.00"), ("Tiramisu", "$4.50"),
        ("Green Tea Ice Cream", "$3.50"), ("Cinnamon Rolls", "$4.00"), ("Coconut Cream Pie", "$4.50")
    ]
    y_position = 0.7
    for dessert, price in desserts:
        dessert_label = Label(frame, text=f"{dessert} - {price}", font=('Quicksand', 12),bg='#FFFAF1')
        dessert_label.place(relx=0.5, rely=y_position, anchor=CENTER)
        y_position += 0.05

label1 = Label(pro, text="For Menu click here ⬇", fg='#002B5B', bg='#ECB390', font=('Quicksand', 10), padx=50)
label1.pack(pady=20, anchor=CENTER)

menu_window_button = Button(pro, text="Menu", fg='#153E7E', command=menu_window, font=("Quicksand", 14, 'bold'),
                            bg='#FCF8E8', activeforeground="#ffffff", activebackground="#153E7E", bd=1, relief=SOLID, padx=100)
menu_window_button.pack(anchor=CENTER)


contact_label = Label(pro, text="To Contact Us ⬇", fg='#002B5B', bg='#ECB390', font=('Quicksand', 12), padx=100)
contact_label.pack(anchor=CENTER,pady=100,padx=20)

# Adding buttons for social media(nadeen)
facebook_button = Button(pro, text="Facebook", fg='white', command=lambda: open_url('https://www.facebook.com/karamelshaam?mibextid=ZbWKwL'), font=("Quicksand", 12, 'bold'),
                         bg='#1877F2', activeforeground="blue", activebackground="lightblue", bd=1, relief=SOLID)
facebook_button.place(relx=0.52,rely=0.65,anchor=CENTER)

twitter_button = Button(pro, text="Twitter", fg='white', command=lambda: open_url('https://www.twitter.com'), font=("Quicksand", 12, 'bold'),
                        bg='#1DA1F2', activeforeground="blue", activebackground="lightblue", bd=1, relief=SOLID)
twitter_button.place(relx=0.65,rely=0.65,anchor=CENTER)

instagram_button = Button(pro, text="Instagram", fg='white', command=lambda: open_url('https://www.instagram.com/karamelshamfoods?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=='), font=("Quicksand", 12, 'bold'),
                          bg='#CF9FFF', activeforeground="blue", activebackground="lightblue", bd=1, relief=SOLID)
instagram_button.place(relx=0.37,rely=0.65,anchor=CENTER)

def order_window():
    order_window = Toplevel(pro)
    order_window.geometry('1400x700+30+10')
    order_window.title("Order")
    order_window.iconbitmap('order.ico')
    #adding frame to order
    frame1 = Frame(order_window, bg='#EFE0BB', bd=-20, relief=RIDGE)
    frame1.pack(fill='both', expand=True, padx=10, pady=10)
    # adding title for frame
    label1 = Label(frame1, text="ORDER", font=('Lucida Calligraphy', 18, 'bold'),bg="#ECB390" , fg='white')
    label1.place(x=580,y=0)

#=================================================
    #variables (       main dish           )
    maindi1=IntVar()
    maindi2=IntVar()
    maindi3=IntVar()
    maindi4=IntVar()
    maindi5=IntVar()
    maindi6=IntVar()
    maindi7=IntVar()
    maindi8=IntVar()
    maindi9=IntVar()
    maindi10=IntVar()
  #====================================================

    #adding the main dishes
    ff1=Frame(frame1,bd=2 , width=320 , height= 550 , bg= "#EFE0BB")
    ff1.place(x=1,y=45)
    a=Label(ff1, text="MAIN DISHES",font=("Lucida Calligraphy",15,"bold"),bg="#ECB390",fg="black")
    a.place(x=100,y=0)
    bp1=Label(ff1,text="SUPREME PIZZA",font=("tajawal",10,"bold"),bg="#ECB390" , fg='#002B5B')
    bp1.place(x=10,y=40)
    bp2=Label(ff1,text="MARGHARITA PIZZA",font=("tajawal",10,"bold"),bg="#ECB390" , fg='#002B5B')
    bp2.place(x=10,y=80)
    bp3=Label(ff1,text="SMOKE PIZZA",font=("tajawal",10,"bold"),bg="#ECB390" ,fg='#002B5B')
    bp3.place(x=10,y=120)
    bp4=Label(ff1,text="SEE RANCH PIZZA",font=("tajawal",10,"bold"),bg="#ECB390" , fg='#002B5B')
    bp4.place(x=10,y=160)
    bp5=Label(ff1,text="CLASSIC CHEESE BURGER",font=("tajawal",10,"bold"),bg="#ECB390" , fg='#002B5B')
    bp5.place(x=10,y=200)
    bp6=Label(ff1,text="MUSHROOM BURGER",font=("tajawal",10,"bold"),bg="#ECB390" , fg='#002B5B')
    bp6.place(x=10,y=240)
    bp7=Label(ff1,text="SPICY BURGER",font=("tajawal",10,"bold"),bg="#ECB390" , fg='#002B5B')
    bp7.place(x=10,y=280)
    bp8=Label(ff1,text="TERIYAKI CHICKEN BOWL",font=("tajawal",10,"bold"),bg="#ECB390" , fg='#002B5B')
    bp8.place(x=10,y=320)
    bp9=Label(ff1,text="FETTUCCINE ALFREDO",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    bp9.place(x=10,y=360)
    bp10=Label(ff1,text="LASAGNA",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    bp10.place(x=10,y=400)
    bpent1=Entry(ff1, width=16,textvariable=maindi1)
    bpent1.place(x=185,y=40)
    bpent2=Entry(ff1, width=16,textvariable=maindi2)
    bpent2.place(x=185,y=80)
    bpent3=Entry(ff1, width=16,textvariable=maindi3)
    bpent3.place(x=185,y=120)
    bpent4=Entry(ff1, width=16,textvariable=maindi4)
    bpent4.place(x=185,y=160)
    bpent5=Entry(ff1, width=16,textvariable=maindi5)
    bpent5.place(x=185,y=200)
    bpent6=Entry(ff1, width=16,textvariable=maindi6)
    bpent6.place(x=185,y=240)
    bpent7=Entry(ff1, width=16,textvariable=maindi7)
    bpent7.place(x=185,y=280)
    bpent8=Entry(ff1, width=16,textvariable=maindi8)
    bpent8.place(x=185,y=320)
    bpent9=Entry(ff1, width=16,textvariable=maindi9)
    bpent9.place(x=185,y=360)
    bpent10=Entry(ff1, width=16,textvariable=maindi10)
    bpent10.place(x=185,y=400)
  #=============================================================

#Variables (appetizers)
    appe1=IntVar()
    appe2=IntVar()
    appe3=IntVar()
    appe4=IntVar()
    appe5=IntVar()
    appe6=IntVar()
    appe7=IntVar()
    appe8=IntVar()

    #adding appetizers
    ff2=Frame(frame1,bd=2 , width=300 , height= 550 , bg= "#EFE0BB")
    ff2.place(x=323,y=45)
    b=Label(ff2, text="APPETIZERS",font=("Lucida Calligraphy",15,"bold"),bg= "#ECB390",fg="black")
    b.place(x=90,y=0)
    b1=Label(ff2,text="Chicken Tenders",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b1.place(x=10,y=40)
    b2=Label(ff2,text="Crunchy",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b2.place(x=10,y=80)
    b3=Label(ff2,text="Buffalo Wings",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b3.place(x=10,y=120)
    b4=Label(ff2,text="French Fries",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b4.place(x=10,y=160)
    b5=Label(ff2,text="Onion Rings",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b5.place(x=10,y=200)
    b6=Label(ff2,text="Spring Rolls",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b6.place(x=10,y=240)
    b7=Label(ff2,text="Dumplings",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b7.place(x=10,y=280)
    b8=Label(ff2,text="Vegan Nachos",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    b8.place(x=10,y=320)
    bent1=Entry(ff2, width=16,textvariable=appe1)
    bent1.place(x=150,y=40)
    bent2=Entry(ff2, width=16,textvariable=appe2)
    bent2.place(x=150,y=80)
    bent3=Entry(ff2, width=16,textvariable=appe3)
    bent3.place(x=150,y=120)
    bent4=Entry(ff2, width=16,textvariable=appe4)
    bent4.place(x=150,y=160)
    bent5=Entry(ff2, width=16,textvariable=appe5)
    bent5.place(x=150,y=200)
    bent6=Entry(ff2, width=16,textvariable=appe6)
    bent6.place(x=150,y=240)
    bent7=Entry(ff2, width=16,textvariable=appe7)
    bent7.place(x=150,y=280)
    bent8=Entry(ff2, width=16,textvariable=appe8)
    bent8.place(x=150,y=320)

#=================================================
    #variables ( sides )
    side1=IntVar()
    side2=IntVar()
    side3=IntVar()
    side4=IntVar()
#====================================================================================
#adding sides 
    c=Label(ff2, text="SIDES",font=("Lucida Calligraphy",15,"bold"),bg="#ECB390", fg='black')
    c.place(x=110,y=360)
    c1=Label(ff2,text="Pepsi",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    c1.place(x=10,y=400)
    c2=Label(ff2,text="Coleslaw",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    c2.place(x=10,y=440)
    c3=Label(ff2,text="Caesar Salad",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    c3.place(x=10,y=480)
    c4=Label(ff2,text="Sweet Potato Wedges",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    c4.place(x=10,y=520)
    cent1=Entry(ff2, width=16,textvariable=side1)
    cent1.place(x=160,y=400)
    cent2=Entry(ff2, width=16,textvariable=side2)
    cent2.place(x=160,y=440)
    cent3=Entry(ff2, width=16,textvariable=side3)
    cent3.place(x=160,y=480)
    cent4=Entry(ff2, width=16,textvariable=side4)
    cent4.place(x=160,y=520)

#=====================================================
#variables (Desserts)
    dessert1=IntVar()
    dessert2=IntVar()
    dessert3=IntVar()
    dessert4=IntVar()
    dessert5=IntVar()
    dessert6=IntVar()
    dessert7=IntVar()
    dessert8=IntVar()
#==============================================
#adding desserts
    ff3=Frame(frame1,bd=2 , width=300 , height= 550 , bg= "#EFE0BB")
    ff3.place(x=625,y=45)
    d=Label(ff3, text="DESSERTS",font=("Lucida Calligraphy",15,"bold"),bg= "#ECB390",fg="black")
    d.place(x=110,y=0)
    d1=Label(ff3,text="Apple Pie",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d1.place(x=10,y=40)
    d2=Label(ff3,text="Chocolate Milkshake",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d2.place(x=10,y=80)
    d3=Label(ff3,text="Vanilla Milkshake",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d3.place(x=10,y=120)
    d4=Label(ff3,text="Strawberry Milkshake",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d4.place(x=10,y=160)
    d5=Label(ff3,text="Tiramisu",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d5.place(x=10,y=200)
    d6=Label(ff3,text="Green Tea Ice Cream",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d6.place(x=10,y=240)
    d7=Label(ff3,text="Cinnamon Rolls",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d7.place(x=10,y=280)
    d8=Label(ff3,text="Coconut Cream Pie",font=("tajawal",10,"bold"),bg="#ECB390", fg='#002B5B')
    d8.place(x=10,y=320)
    dent1=Entry(ff3, width=16,textvariable=dessert1)
    dent1.place(x=170,y=40)
    dent2=Entry(ff3, width=16,textvariable=dessert2)
    dent2.place(x=170,y=80)
    dent3=Entry(ff3, width=16,textvariable=dessert3)
    dent3.place(x=170,y=120)
    dent4=Entry(ff3, width=16,textvariable=dessert4)
    dent4.place(x=170,y=160)
    dent5=Entry(ff3, width=16,textvariable=dessert5)
    dent5.place(x=170,y=200)
    dent6=Entry(ff3, width=16,textvariable=dessert6)
    dent6.place(x=170,y=240)
    dent7=Entry(ff3, width=16,textvariable=dessert7)
    dent7.place(x=170,y=280)
    dent8=Entry(ff3, width=16,textvariable=dessert8)
    dent8.place(x=170,y=320)

#==========================================================
#variables for customers
    b_number=StringVar()
    X=random.randint(100,9999)
    b_number.set(str(X))
    c_name=StringVar()
#=========================================================
    #customer data
    F4=Frame(order_window,bd=2,width=338,height=130,bg="#ECB390")
    F4.place(x=928,y=55)
    title=Label(F4,text="Customer order:",font=("tajawal", 13, 'bold'),fg='black',bg='#EFE0BB')
    title.place(x=100,y=0)
    customer_name=Label(F4,text="Customer name:",font=("tajawal", 11, 'bold'),fg='#002B5B')
    customer_name.place(x=5,y=40)
    bill_number=Label(F4,text="Bill number:",font=("tajawal", 11, 'bold'),fg='#002B5B')
    bill_number.place(x=5,y=70)
    Ent_name=Entry(F4,textvariable=c_name)
    Ent_name.place(x=160,y=40)
    Ent_bill=Entry(F4,textvariable=b_number,justify='center')
    Ent_bill.place(x=160,y=70)

    #=========================================
    #Bill
    titleb=Label(F4,text="{BILL}",font=("Lucida Calligraphy", 13, 'bold'),fg='#002B5B',bg="#ECB390")
    titleb.place(x=145,y=100)
    F5=Frame(order_window,width=10,height=130,bg='white')
    F5.place(x=928,y=188)
    Scrol_y=Scrollbar(F5,orient=VERTICAL)
    ttextarea=Text(F5,yscrollcommand=Scrol_y.set)
    Scrol_y.pack(side=LEFT,fill=Y)
    Scrol_y.config(command=ttextarea.yview)
    ttextarea.pack(fill=BOTH,expand=1)
    def welcome(Ent_name,Ent_bill):
        ttextarea.delete('1.0', END)
        ttextarea.insert(END, "       Welcome to Pizza Restaurant")
        ttextarea.insert(END, "\n=======================================")
        ttextarea.insert(END, f"\n Customer Name: {Ent_name.get()}")
        ttextarea.insert(END, f"\n Bill Number  : {Ent_bill.get()}")
        ttextarea.insert(END, "\n=======================================")
        ttextarea.insert(END, f"\n Items\t\t  Qty\t\t Price")
        ttextarea.insert(END, "\n=======================================")

    welcome(Ent_name,Ent_bill)

    #=====================================================
    #function of clear 
    def clear():
        maindi1.set(0)
        maindi2.set(0)
        maindi3.set(0)
        maindi4.set(0)
        maindi5.set(0)
        maindi6.set(0)
        maindi7.set(0)
        maindi8.set(0)
        maindi9.set(0)
        maindi10.set(0)
        appe1.set(0)
        appe2.set(0)
        appe3.set(0)
        appe4.set(0)
        appe5.set(0)
        appe6.set(0)
        appe7.set(0)
        appe8.set(0)
        side1.set(0)
        side2.set(0)
        side3.set(0)
        side4.set(0)
        dessert1.set(0)
        dessert2.set(0)
        dessert3.set(0)
        dessert4.set(0)
        dessert5.set(0)
        dessert6.set(0)
        dessert7.set(0)
        dessert8.set(0)
        c_name.set('')
        welcome(Ent_name,Ent_bill)
    #==================================================================  
    #function save 
    def save():
       m1 = messagebox.askyesno("Save", "Do you want to save the bill?")
       if m1 > 0:
          file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], title="Save your bill")
          if file_path:
            bill_content = ttextarea.get("1.0", END)
            with open(file_path, 'w') as file:
                file.write(bill_content)
            messagebox.showinfo("Saved", f"Bill saved as {file_path}")
    #========================================================================
    #function of total cost
    def totall_cost():
        global totala, mmaindi1, mmaindi2, mmaindi3, mmaindi4, mmaindi5, mmaindi6, mmaindi7, mmaindi8, mmaindi9, mmaindi10,aappe1,aappe2,aappe3,aappe4,aappe5,aappe6,aappe7,aappe8,sside1,sside2,sside3,sside4,ddessert1,ddessert2,ddessert3,ddessert4,ddessert5,ddessert6,ddessert7,ddessert8
        # ================= total cost of main dishes ======
        mmaindi1=maindi1.get()*12
        mmaindi2=maindi2.get()*10
        mmaindi3=maindi3.get()*11
        mmaindi4=maindi4.get()*13
        mmaindi5=maindi5.get()*8
        mmaindi6=maindi6.get()*9
        mmaindi7=maindi7.get()*8.50
        mmaindi8=maindi8.get()*12.50
        mmaindi9=maindi9.get()*11.50
        mmaindi10=maindi10.get()*13.50
        totalmain=float(mmaindi1+mmaindi2+mmaindi3+mmaindi4+mmaindi5+mmaindi6+mmaindi7+mmaindi8+mmaindi9+mmaindi10)
        # ================= total cost of appetizers ======
        aappe1=appe1.get()*3
        aappe2=appe2.get()*4
        aappe3=appe3.get()*6
        aappe4=appe4.get()*3
        aappe5=appe5.get()*4.50
        aappe6=appe6.get()*5
        aappe7=appe7.get()*5.50
        aappe8=appe8.get()*6.50
        totalappe=float(aappe1+aappe2+aappe3+aappe4+aappe5+aappe6+aappe7+aappe8)
        # ================= total cost of sides ======
        sside1=side1.get()*3
        sside2=side2.get()*2.50
        sside3=side3.get()*4
        sside4=side4.get()*3.50
        totalside=float(sside1+sside2+sside3+sside4)
        # ================= total cost of desserts ======
        ddessert1=dessert1.get()*4
        ddessert2=dessert2.get()*3
        ddessert3=dessert3.get()*3
        ddessert4=dessert4.get()*3
        ddessert5=dessert5.get()*4.50
        ddessert6=dessert6.get()*3.50
        ddessert7=dessert7.get()*4
        ddessert8=dessert8.get()*4.30
        totaldessert=float(ddessert1+ddessert2+ddessert3+ddessert4+ddessert5+ddessert6+ddessert7+ddessert8)
        totala=totalmain+totalappe+totaldessert+totalside
        bb=(
        "Total cost of Main dish = " + str(totalmain) + " $ \n" +
        "Total cost of appetizers = " + str(totalappe) + " $ \n" +
        "Total cost of sides = " + str(totalside) + " $ \n" +
        "Total cost of Desserts = " + str(totaldessert) + " $ \n"+
        "Total = "+str(totala)+"$")
        messagebox.showinfo("Total cost",bb)
#=======================================================
     #function bill
    def bill():
        if Ent_name.get() == "":
          messagebox.showerror("Error", "Please enter your name")
        elif totala == 0.00:
          messagebox.showerror("Error", "Please choose items")
        else:
           welcome(Ent_name, Ent_bill)
           if maindi1.get()!= 0:
              ttextarea.insert(END, f"\n Supreme pizza \t \t {maindi1.get()} \t \t {mmaindi1}")
           if maindi2.get()!= 0:
              ttextarea.insert(END, f"\n Marghrita pizza \t\t{maindi2.get()} \t \t {mmaindi2}")
           if maindi3.get()!= 0:
              ttextarea.insert(END, f"\n Smoke pizza \t \t   {maindi3.get()} \t \t {mmaindi3}")
           if maindi4.get()!= 0:
              ttextarea.insert(END, f"\n See ranch pizza \t {maindi4.get()} \t \t         {mmaindi4}")
           if maindi5.get()!= 0:
              ttextarea.insert(END, f"\n C.Cheese Burger \t {maindi5.get()} \t\t\t {mmaindi5}")
           if maindi6.get()!= 0:
              ttextarea.insert(END, f"\n Mushroom Burger\t\t {maindi6.get()} \t \t {mmaindi6}")
           if maindi7.get()!= 0:
              ttextarea.insert(END, f"\n Spicy Burger  \t \t {maindi7.get()} \t \t {mmaindi7}")
           if maindi8.get()!= 0:
              ttextarea.insert(END, f"\n Teri.chic.bowl\t \t {maindi8.get()}\t    \t {mmaindi8}")
           if maindi9.get()!= 0:
              ttextarea.insert(END, f"\n Fettuccine.A\t   \t {maindi9.get()}\t    \t {mmaindi9}")
           if maindi10.get()!= 0:
              ttextarea.insert(END, f"\n Lasagna \t \t   {maindi10.get()} \t \t {mmaindi10}")
           if appe1.get()!=0:
              ttextarea.insert(END, f"\n Chic.Tender \t \t   {appe1.get()} \t \t {aappe1}")
           if appe2.get()!=0:
              ttextarea.insert(END, f"\n Crunchy \t \t   {appe2.get()} \t \t {aappe2}")
           if appe3.get()!=0:
              ttextarea.insert(END, f"\n B.wings \t \t   {appe3.get()} \t \t {aappe3}")
           if appe4.get()!=0:
              ttextarea.insert(END, f"\n French.F \t \t   {appe4.get()} \t \t {aappe4}")
           if appe5.get()!=0:
              ttextarea.insert(END, f"\n Onion Rings \t \t   {appe5.get()} \t \t {aappe5}")
           if appe6.get()!=0:
              ttextarea.insert(END, f"\n Spring Rolls \t \t  {appe6.get()} \t \t {aappe6}")
           if appe7.get()!=0:
              ttextarea.insert(END, f"\n Dumplings\t \t   {appe7.get()} \t \t {aappe7}")
           if appe8.get()!=0:
              ttextarea.insert(END, f"\n Vegan Nachos \t \t  {appe8.get()} \t \t {aappe8}")
           if side1.get()!=0:
              ttextarea.insert(END, f"\n Pepsi \t \t   {side1.get()} \t \t {sside1}")
           if side2.get()!=0:
              ttextarea.insert(END, f"\n Colesalw \t \t   {side2.get()} \t \t {sside2}")
           if side3.get()!=0:
              ttextarea.insert(END, f"\n Caesar Salad \t \t  {side3.get()} \t \t {sside3}")
           if side4.get()!=0:
              ttextarea.insert(END, f"\n S.P.Wedges\t \t   {side4.get()} \t \t {sside4}")
           if dessert1.get()!=0:
              ttextarea.insert(END, f"\n Apple Pie\t \t   {dessert1.get()} \t \t {ddessert1}")
           if dessert2.get()!=0:
              ttextarea.insert(END, f"\n Choc.MS\t \t   {dessert2.get()} \t \t {ddessert2}")
           if dessert3.get()!=0:
              ttextarea.insert(END, f"\n Vanilla.MS\t \t   {dessert3.get()} \t \t {ddessert3}")
           if dessert4.get()!=0:
              ttextarea.insert(END, f"\n Straw.MS\t \t   {dessert4.get()} \t \t {ddessert4}")
           if dessert5.get()!=0:
              ttextarea.insert(END, f"\n Tiramisu\t \t   {dessert5.get()} \t \t {ddessert5}")
           if dessert6.get()!=0:
              ttextarea.insert(END, f"\n Green Tea I.C\t \t  {dessert6.get()} \t \t {ddessert6}")
           if dessert7.get()!=0:
              ttextarea.insert(END, f"\n Cinnamon Rolls\t \t {dessert7.get()} \t \t {ddessert7}")
           if dessert8.get()!=0:
              ttextarea.insert(END, f"\n Coc.Cream pie\t \t  {dessert8.get()} \t \t {ddessert8}")

              

              
              

        ttextarea.insert(END, "\n===========================================")
        ttextarea.insert(END, f"\n\t   Total cost = \t \t {totala} $ ")
        save()



    #total cost
    F6=Frame(order_window,bd=2,width=338,height=100,bg='#ECB390')
    F6.place(x=930,y=566)
    costbu=Button(F6,text='Total Cost',width=12,font=('arial',12,'bold'),bg='white',fg='#002B5B',relief=GROOVE,command=totall_cost)
    costbu.place(x=25,y=8)
    clearbu=Button(F6,text='Clear',width=12,font=('arial',12,'bold'),bg='white',fg='#002B5B',relief=GROOVE,command=clear)
    clearbu.place(x=185,y=8)
    createbu=Button(F6,text='Create Bill',width=12,font=('arial',12,'bold'),bg='white',fg='#002B5B',relief=GROOVE,command=bill)
    createbu.place(x=105,y=45)
#=======================================================

   
# order button(nadeen)       
order_label = Button(pro, text="Order here",font=("Quicksand", 14, 'bold'),command=order_window,bg='#FCF8E8', activeforeground="#ffffff", 
activebackground="#153E7E", bd=0.5, relief=SOLID,fg='#153E7E',padx=75)
order_label.place(x=190,y=175)



pro.mainloop()

