import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):   
    e2.delete(0, END)
    e3.delete(0, END)   
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e2.insert(0,select['pname'])
    e3.insert(0,select['price'])
 
def Add():
    
    pn = e2.get()
    pr = e3.get()
    
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="shopping")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  product (pname,price) VALUES (%s, %s)"
       val = (pn,pr)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "product inserted successfully...")       
       e2.delete(0, END)
       e3.delete(0, END)    
       
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
   
    pn = e2.get()
    pr = e3.get()    
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="shopping")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update product set price=%s where pname=%s"
       val = (pr,pn)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updated successfully...")
 
       e2.delete(0, END)
       e3.delete(0, END)       
       e2.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    #studid = e1.get()
    selected_item = listBox.selection()[0]
    x=listBox.item(selected_item)['values'][0]
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="shopping")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from product where pid = %s"
       val = (x,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def show():
        mysqldb = mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="shopping")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT pid,pname,price FROM product")
        records = mycursor.fetchall()
        print(records)
 
        for i, (pid,pname, price) in enumerate(records, start=1):
            listBox.insert("", "end", values=(pid, pname, price))
            mysqldb.close()
def admin_task():
    root = Tk()
    root.geometry("800x500")
    global e1
    global e2
    global e3
    global e4
    global listBox 
 
    tk.Label(root, text="Product Information", fg="red", font=(None, 30)).place(x=300, y=5) 
    Label(root, text="Product Name").place(x=10, y=40)
    Label(root, text="Price").place(x=10, y=70)
    e2 = Entry(root)
    e2.place(x=140, y=40) 
    e3 = Entry(root)
    e3.place(x=140, y=70) 
    Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
    Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
    Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
 
    cols = ('pid', 'pname', 'price')
    listBox = ttk.Treeview(root, columns=cols, show='headings',height=5)
 
    for col in cols:
        listBox.heading(col, text=col)
        listBox.column("# 1",anchor=CENTER, stretch=NO, width=25)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=200)
 
    show()
    listBox.bind('<Double-Button-1>',GetValue)
 
  
