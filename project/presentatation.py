from tkinter import *
import mysql.connector
from tkinter import messagebox as m

con = mysql.connector.connect(host="localhost", user="root", passwd="tiger", database='db')
cur = con.cursor()

def show_tc():
    a = m.askyesno('HELP!!', 'Do you have Symptoms of COVID?')
    if a:
        m.showinfo('Positive', 'Please contact Our Helping Services ON TOLL FREE NUMBER 8780-8780')
    else:
        m.showinfo('Negative', 'Please Take Necessary Precautions')

def clear():
    a = t1.get()
    print(a)
    q="DELETE FROM covid WHERE fname=%s"
    cur.execute(q,(a,))
    con.commit()
    cur.execute('SELECT * FROM covid')
    for i in cur:
        print(i)

def insert():
    try:
        a = t1.get()
        b = t2.get()
        c = t3.get()
        d = t4.get()
        e = f1.get()
        f = t5.get()
        g = t6.get()

        query = "INSERT INTO covid VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (a, b, c, d, e, f, g))
        con.commit()
        m.showinfo('Success', 'Data Inserted Successfully!')
        print('Done')
    except Exception as e:
        m.showerror('Error', 'Error: {}'.format(e))

window = Tk()
window.title("SR COVID-19 SURVEY")
window.geometry('600x600')
window.configure(background="orange")

a = Label(window ,text = "First Name",background="white",foreground="black",font=("times new roman", 13))
a.grid(row = 0,column = 0,padx=10,pady=10)
b = Label(window ,text = "Last Name",background="white",foreground="black",font=("times new roman", 13))
b.grid(row = 1,column = 0,padx=5,pady=10)
c = Label(window ,text = "Email Id",background="white",foreground="black",font=("times new roman", 13))
c.grid(row = 2,column = 0,padx=5,pady=10)
d = Label(window ,text = "Aadhaar Number",background="white",foreground="black",font=("times new roman", 13))
d.grid(row = 3,column = 0,padx=5,pady=10)
e = Label(window ,text = "Gender",background="white",foreground="black",font=("times new roman", 13))
e.grid(row = 4,column = 0,padx=5,pady=10)
g = Label(window ,text = "1st dose date",background="black",foreground="white",font=("times new roman", 13))
g.grid(row = 5,column = 0,padx=5,pady=10)
h = Label(window ,text = "2nd dose date",background="black",foreground="white",font=("times new roman", 13))
h.grid(row = 6,column = 0,padx=5,pady=10)

f1=StringVar()
f1.set(" ")
r1=Radiobutton(window, text="Male",value="Male",background="white",foreground="blue",variable=f1)
r1.grid(row = 4,column = 1,padx=5,pady=10)
Radiobutton(window, text="Female",value="Female",background="white",foreground="blue",variable=f1).grid(row =4,column = 2,padx=5,pady=10)
Radiobutton(window, text="Others",value="Others",background="white",foreground="blue",variable=f1).grid(row =4,column = 5,padx=5,pady=10)
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
 
a1 = Entry(window,textvariable=t1,foreground="red",font=("times new roman",13))
a1.grid(row = 0,column = 1)
b1 = Entry(window,textvariable=t2,font=("times new roman",13))
b1.grid(row = 1,column = 1)
c1 = Entry(window,textvariable=t3,foreground="blue",font=("times new roman",13))
c1.grid(row = 2,column = 1)
d1 = Entry(window,textvariable=t4,font=("times new roman",13))
d1.grid(row = 3,column = 1)
g1 = Entry(window,textvariable=t5,font=("times new roman",13))
g1.grid(row = 5,column = 1)
h1 = Entry(window,textvariable=t6,font=("times new roman",13)).grid(row = 6,column = 1)

btn1 = Button(window ,text="SUBMIT",command=insert).place(x=80,y=318)
btn2 = Button(window ,text="EXIT",command=window.destroy).grid(row=14,column=1)
btn3 = Button(window ,text="HELP",command=show_tc).grid(row=14,column=2)
btn4 = Button(window ,text="DELETE",command=clear).grid(row=14,column=4)
window.mainloop()

