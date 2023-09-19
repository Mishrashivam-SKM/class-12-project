from tkinter import *
import mysql.connector
from admintask import admin_task
from UserTask import User_form

def display_selected(choice):  

  ch = options.get()
  #print(ch)
def dbadd():
  tus=txtus.get();
  tnm=txtname.get();
  tp=txtpass.get();
  te=txtemail.get();
  print(te);
  conn = mysql.connector.connect(host="localhost",user="root",password="mysqlroot",db="shopping")
  cur = conn.cursor()        
  query = "insert into newuser(cname,uname,password,email)values(%s,%s,%s,%s)"
  s1 = (tnm,tus,tp,te)        
  try: 
      cur.execute(query,s1)      
      conn.commit();
  except Exception as e:
      conn.rollback()
  finally:
      conn.close()
  print("Query executed successfully")    
def open_win():
   new= Toplevel(login_screen)
   new.geometry("750x250")
   new.title("New Registration")
   #chd=Tk();
   global txtus;
   global txtname;
   global txtemail;
   global txtpass;
   txtus=StringVar()
   txtname=StringVar()
   txtemail=StringVar()
   txtpass=StringVar()
   #Create a Label in New window
   Label(new, text="Name").place(x=50,y=20)
   Entry(new,textvariable=txtname).place(x=130,y=20)
   Label(new, text="user Name").place(x=50,y=50)
   Entry(new,textvariable=txtus).place(x=130,y=50)
   Label(new, text="password").place(x=30,y=80)
   Entry(new,textvariable=txtpass).place(x=130,y=80)
   Label(new, text="Email").place(x=50,y=110)
   Entry(new,textvariable=txtemail).place(x=130,y=110)   
   Button(new,text="Register", width=10, height=1, bg="orange",command=dbadd).place(x=105,y=200)

#defining login function
def login():
    uname=username.get()
    print(uname)
    pwd=password.get()
    #getting form data
    ch=options.get()
    print(ch)

    mysqldb = mysql.connector.connect(host="localhost",user="root",password="mysqlroot",database="shopping")
    mycursor = mysqldb.cursor()
    myrecords=[]
    mycursor.execute("SELECT uname,password FROM newuser where uname=%s and password =%s",(username.get(),password.get()))
    records = mycursor.fetchone()
    
    if ch=="Select":
      message.set("select admin or user")    
    #applying empty validation
    elif uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      if uname=="raman" and pwd=="abc123" and ch=="Admin":
         #message.set("Admin Login success")
         admin_task()
      elif records!=None and ch=="User":
         message.set("User Login success")
         User_form(uname)
      else:
         message.set("Wrong username or password!!!")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login Form")
    #setting height and width of screen
    login_screen.geometry("300x250")
    #declaring variable
    global  message;
    global username;
    global password;
    global options;
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #Username Label
    my_list = ["Admin","User"];
    options = StringVar();
    options.set("Select")
    dropdown = OptionMenu(login_screen,options,*my_list,command=display_selected).place(x=60,y=20)
    Label(login_screen, text="Username * ").place(x=20,y=60)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=90,y=62)
    #Password Label
    Label(login_screen, text="Password * ").place(x=20,y=100)
    #Password textbox
    Entry(login_screen, textvariable=password,show="*").place(x=90,y=102)    
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=95,y=180)
    #Login button
   
    #options.set(my_list[1]);
    
    Button(login_screen, text="Submit", width=10, height=1, bg="orange",command=login).place(x=40,y=150)
    Button(login_screen, text="New user", width=10, height=1, bg="orange",command=open_win).place(x=160,y=150)
    login_screen.mainloop()

#calling function Loginform
Loginform()

