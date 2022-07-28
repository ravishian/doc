from tkinter import *
from tkinter import Tk
from tkinter import ttk
import tkinter.messagebox as tmsg
from turtle import goto, width
from PIL import Image, ImageTk
from datetime import date
import random
import cx_Oracle
#from fpdf import FPDF

con=cx_Oracle.connect('scott/tiger')
cur=con.cursor()
print("Connected", con.version)

root = Tk()
root.title("Hello World ")
root.geometry("600x470")
root.resizable(False,False)



def adminadd():
    add=Toplevel()
    add.geometry("1200x800")
    add.title("Home")  
    #------------------adding back frame-------------
    front1=Frame(add,borderwidth=10,bg="#3B3C36")
    front1.place(x=0,y=0,relheight=1,relwidth=1)
    #------------------adding right-side frame------------
    front2 = Frame(add,bg="white")
    front2.place(x=650,y=150,width=450,height=100)
    #------------------adding left-side frame------------
    front3 = Frame(add,bg="white")
    front3.place(x=0,y=0,width=600,height=1080)
    # #-------------------New frame-------------------------
    # front5 = Frame(add,bg="white")
    # front5.place(x=650,y=740,width=200,height=20)

  

    # image = Image.open("C:\\Users\\navis\\Downloads\\frontscreen1.jpg")   
    # image = image.resize((600, 800), Image.Resampling.LANCZOS)
    #test = ImageTk.PhotoImage(image)
    # label1 = tkinter.Label(front3, image=test)
    # label1.image = test
    # label1.place(x=0,y=0)                                                   



    #-------------------adding right-bottom-side frame---------------------
    def tree():
        
        global front4
        front4 = Frame(add,bg="white")
        front4.place( x=600 , y=300 , width=600 , height=450 )
        front4.config(bg='black')

        retlist3 = cur.execute("select * from main")
        global countt2
        countt2 = 0
        for i in retlist3 :        
                
            countt2 += 1
        

        datevar = date.today()
        # print(type(datevar))
        stat2 = "select * from main where record = :1"
        var2 = [datevar]
        retlist2 = cur.execute(stat2,var2)
        countt = 0
        for i in retlist2 :        
                countt += 1





    
        ttl = Label(front4, text = "Today Entries :", fg = "black")
        ttl.place(x=45,y=426)
        # ttlval = countt
        ttl2 = Label(front4, text = countt, fg = "black")
        ttl2.place(x=125,y=426)
            
        ttl3 = Label(front4, text = "Total Entries :", fg = "black")
        ttl3.place(x=200,y=426)
        # ttlval = countt
        ttl4 = Label(front4, text = countt2, fg = "black")
        ttl4.place(x=275,y=426)



        global tv

        tv = ttk.Treeview(front4 , height=20)
        tv['columns']=('id', 'name', 'age' , 'phone' , 'gender' , 'medicine' , 'days' , 'date', 'amount')
        tv.column('#0', width=0, stretch=NO)
        tv.column('id', anchor=CENTER, width=60)
        tv.column('name', anchor=CENTER, width=60)
        tv.column('age', anchor=CENTER, width=30)
        tv.column('phone', anchor=CENTER, width=80)
        tv.column('gender', anchor=CENTER, width=50)
        tv.column('medicine', anchor=CENTER, width=80)
        tv.column('days', anchor=CENTER, width=30)
        tv.column('date', anchor=CENTER, width=50)
        tv.column('amount', anchor=CENTER, width=70)

        tv.heading('#0', text='', anchor=CENTER)
        tv.heading('id', text='Id', anchor=CENTER)
        tv.heading('name', text='Name', anchor=CENTER)
        tv.heading('age', text='Age', anchor=CENTER)
        tv.heading('phone', text='Phone', anchor=CENTER)
        tv.heading('gender', text='Gender', anchor=CENTER)
        tv.heading('medicine', text='Medicine', anchor=CENTER)
        tv.heading('days', text='Days', anchor=CENTER)
        tv.heading('date', text='Date', anchor=CENTER)
        tv.heading('amount', text='Amount', anchor=CENTER)


        # print(radiobtn.get())
        global radiobtnvar
        radiobtnvar = radiobtn.get()
        # print(radioentry.get())
        radiobtnvar2 = radioentry.get()

        if (radiobtnvar == 1 or radiobtnvar == 2) and len(radiobtnvar2) < 2 :
             
            print("HEllo world")
            datevar = date.today()
            # print(type(datevar))
            stat2 = "select * from main where record = :1"
            var2 = [datevar]
            retlist2 = cur.execute(stat2,var2)
                
            countt = 0
            for i in retlist2 :        
                tv.insert(parent='', index=0, iid=countt, text='', values=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[8],i[7]])
                tv.pack()
                countt += 1

        elif radiobtnvar == 1 :
            
            stat ="select * from main where id = :1"
            val = [radiobtnvar2]
            retlist = cur.execute(stat,val)
            con.commit()
            for i in retlist:
                tv.insert(parent='', index=0, iid=0, text='', values=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[8],i[7]])
                tv.pack()

        elif radiobtnvar == 2 :
            stat ="select * from main where phone = :1"
            val = [radiobtnvar2]
            retlist1 = cur.execute(stat,val)
            con.commit()
            for i in retlist1:
                tv.insert(parent='', index=0, iid=0, text='', values=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[8],i[7]])
                tv.pack()
            
        else:
            datevar = date.today()
            # print(type(datevar))
            stat2 = "select * from main where record = :1"
            var2 = [datevar]
            retlist2 = cur.execute(stat2,var2)
            
            countt = 0
            for i in retlist2 :        
                tv.insert(parent='', index=0, iid=countt, text='', values=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[8],i[7]])
                tv.pack()
                countt += 1

        



    
        
    global radiobtn,radioentry 
   
    radiobtn = IntVar()
    
    R1 = Radiobutton(front2, text="Id", variable=radiobtn, value=1)#,command=sel)
    R1.place( x=50 , y=17 )

    R2 = Radiobutton(front2, text="Phone", variable=radiobtn, value=2)#,command=sel)
    R2.place( x=180 , y=17 )

    radioentry = StringVar()
    radioentry = Entry(front2 , textvariable=radioentry , width=18 , bd=2 , font=20 )
    radioentry.place( x=30 , y=50 )

    radbut = Button(front2 , text="Submit" ,command=tree , width=8 , bg= 'skyblue' )
    radbut.place( x=285 , y=50 )

    #------------------------------------------------------------
    def prnt():
        global a1,datevar
        idvar = str(random.randint(1,10000))
        a1 = namevalue.get()
        b1 = int(agevalue.get())
        c1 = phonevalue.get()
        d1 = int(daysvalue.get())
        e1 = int(amountvalue.get())
        f1 = med_inside.get()
        g1 = gen.get()
        datevar = date.today()

        

        
        if a1.isalpha() == True :
            if b1>5 and b1<80 :
                if len(c1) == 10 :
                    if d1 > 0 :
                        if e1 > 0:
                            if f1 != 'Select Option' :
                                if g1 != 'Select Option'  :
                                    print(idvar,a1,b1,c1,d1,e1,f1,g1,datevar)
                                    sql5 = 'insert into main values( :0, :1, :2, :3, :4, :5, :6, :7, :8)'
                                    val5 = [ idvar, a1, b1, c1, g1, f1, d1, e1, datevar]
                                    cur.execute(sql5,val5)
                                    con.commit()
                                    
                                    tree()
                                     
                                    
                                                                                                                                    
            else :
                tmsg.showerror("Error","Enter valid age")
                adminadd()
                add.destroy()
    
    Label(add,text=" Gauanwale" , font="arial 25 ").pack(pady=50)

    a = Label(add,text="Name",font=23)
    a.place(x=100,y=150)
    b = Label(add,text="Age",font=23)
    b.place(x=100,y=200)
    c = Label(add,text="Phone",font=23)
    c.place(x=100,y=250)
    d = Label(add,text="Gender",font=23)
    d.place(x=100,y=300)
    e = Label(add,text="Medicine",font=23)
    e.place(x=100,y=350)
    f = Label(add,text="Days",font=23)
    f.place(x=100,y=400)
    g = Label(add,text="Amount",font=23)
    g.place(x=100,y=450)
    btn = Button(add,text="Submit",width=12,height=3,command=prnt)
    btn.place(x=100,y=500)

    #entery

    global namevalue,agevalue,phonevalue,gendervalue,daysvalue,amountvalue,med_inside,value_inside
  
    namevalue = StringVar()
    agevalue = StringVar()
    phonevalue = StringVar()
    agevalue = StringVar()
    amountvalue = StringVar()
    daysvalue = StringVar()
    #Option Box
    ###########################################################
    options_list = ["Male", "Female"]  #option
    gen = StringVar(add)         #option
    gen.set("Select Option")
    
    Medicine_list = ["Pathri", "Height","Sugar","Bawaseer","Fulherry","Kil","Skin","Sleep","paralysis"]  #option
    med_inside = StringVar(add)         #option
    med_inside.set("Select Option")    #option


    nameEntry=Entry(add,textvariable=namevalue,width=30,bd=2,font=20)
  
    question_menu = OptionMenu(add, gen, *options_list).place(x=200,y=300)  # option Menu
    medlist_menu = OptionMenu(add, med_inside, *Medicine_list).place(x=200,y=350)
    emailEntry=Entry(add,textvariable=phonevalue,width=30,bd=2,font=20)
    ageEntry=Entry(add,textvariable=agevalue,width=30,bd=2,font=20)
    daysEntry=Entry(add,textvariable=daysvalue,width=30,bd=2,font=20)
    amountEntry=Entry(add,textvariable=amountvalue,width=30,bd=2,font=20)

    nameEntry.place(x=200,y=150)
    ageEntry.place(x=200,y=200)
    emailEntry.place(x=200,y=250)
    daysEntry.place(x=200,y=400)
    amountEntry.place(x=200,y=450)

    Button(add,text="Siqn up",font=20,width=11,height=2,command=10).place(x=500,y=780)
    #btn1=Button(root,text="Home",width=12,height=3,command=Home)
    #btn1.place(x=150,y=350)
    btn2=Button(add,text="Login",width=12,height=3,command=10)
    btn2.place(x=300,y=700)

    def delete():
        # Get selected item to Delete
        selected_item = tv.selection()
        delitem = tv.item(selected_item)['values'][0]
        # print(tv.item(selected_item)['values'][0])
        sqll2 = "delete from main where id = :1"
        vall2 = [delitem]
        cur.execute(sqll2,vall2)
        con.commit()
        

        tv.delete(selected_item)

    del_btn =ttk.Button(front2, text="Delete", command=delete)
    del_btn.place(x=360 , y=50 )

    tree()


# my_pdf = FPDF()
# my_pdf.add_page()
# my_pdf.set_font("Arial",size=16)
# my_pdf.cell(200,10,txt=a1,ln=1,align="C")
# my_pdf.output("myPDF.pdf")

btn3=Button(root,text="Login",width=12,height=3,command=adminadd)
btn3.place(x=300,y=400)

root.mainloop()