from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def get_totpr(pn):
    conn = mysql.connector.connect(host="localhost",user="root",password="mysqlroot",db="shopping")
    cur = conn.cursor()
    sql="SELECT price FROM product WHERE pname = %s"
    cur.execute(sql,(pn,))    
    data = cur.fetchone()[0]    
    conn.close();
    return data;
def User_form(ur):
    root = Tk()
    root.title("User Form")
    root.geometry("500x500")
    global list_data
    list_data = []
    global listbox;
    global lstbox;
    global lsbox;
    global content;
    global content1;
    global  message;
    global calc;
    global calc1;
    global user;
    user=ur;
    calc = tk.StringVar()
    content = tk.StringVar()
    content1=tk.StringVar()
    calc1=tk.StringVar()
    message=tk.StringVar()
    Label(root, text="enter product name ").place(x=20,y=60)
    content = tk.Entry(root, textvariable=content1)
    content.place(x=150,y=60)
    Label(root, text="enter Quantity ").place(x=20,y=90)
    calc = tk.Entry(root, textvariable=calc1)
    calc.place(x=150,y=90)
    button = tk.Button(root, text="Add Item", command=add_item)
    button.place(x=150,y=120) 
    Label(root, text="Preview after save").place(x=280,y=170)    
    button_delete_selected = tk.Button(root,text="Delete Selected", command=delete_selected)
    button_delete_selected.place(x=150,y=170) 
    listbox = tk.Listbox(root)
    listbox.place(x=150,y=200)
    listbox.bind("&lt;Return>", add_item)
    lstbox = tk.Listbox(root,width = 50)
    lstbox.place(x=280,y=200)
    lstbox.bind("&lt;Return>",preview) 
    bquit = tk.Button(root, text="save", command=quit)
    bquit.place(x=170,y=380)    
    Label(root, text="",fg="red", textvariable=message).place(x=95,y=400)
def preview(p,qty,pr,tm):
    ds="name",p,"qty",qty,"price",pr,"tot amt:",tm
    lstbox.insert(tk.END,ds)
             
    
def delete():
    global list_data
    listbox.delete(0, tk.END)
    list_data = []
def delete_selected():
 
    try:
        selected = listbox.get(listbox.curselection())
        listbox.delete(listbox.curselection())
        list_data.pop(list_data.index(selected))
        # reload_data()
        # # listbox.selection_clear(0, END)
        listbox.selection_set(0)
        listbox.activate(0)
        listbox.event_generate("&lt;&lt;ListboxSelect>>")
        print(listbox.curselection())
    except:
        pass
def test_p(s):
    conn = mysql.connector.connect(host="localhost",user="root",password="mysqlroot",db="shopping")
    cur = conn.cursor()    
    sql="SELECT price FROM product where pname=%s"
    cur.execute(sql,(s,))
    records = cur.fetchall()
    tr=cur.rowcount;
    if(tr>0):
        
        return True;
    else:
        return False;        
    
Dict = {}
def add_item():
    #global list_data
    #print("add_item called")
    if content.get() != "" and calc.get() != "":
        if test_p(content.get()):
            listbox.insert(tk.END, content.get())
            list_data.append(content.get())         
            Dict[content.get()]=calc.get()
            content1.set("")
            calc1.set("")
            message.set("")
        else:
            message.set("Not valid product refer available product ")
    else:
        message.set("item or quatity cannot be empty ")
        
def quit():    
    conn = mysql.connector.connect(host="localhost",user="root",password="mysqlroot",db="shopping")
    cur = conn.cursor()
    #with open("save.txt", "w", encoding="utf-8") as file:
    for x in Dict.keys():
        pr=get_totpr(x)
        #tot=Dict[x]*pr        
        query = "insert into tuser(uname,pname,qty,price,totamt)values(%s,%s,%s,%s,%s)"
        s1 = (user,x,Dict[x],pr,int(Dict[x])*(pr))
        preview(x,Dict[x],pr,int(Dict[x])*(pr))
        try: 
          cur.execute(query,s1)      
          conn.commit();
          
        except Exception as e:
          print(e)        
    conn.close()    
    print("Query executed successfully")       

    
#User_form("pooja")

#print(get_totpr('fg',3))
        
