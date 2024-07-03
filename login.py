from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors
import subprocess
win=Tk()
win.config(bg="gray")
win.geometry("500x400")
win.title("Welcome to Login")
win.resizable(False,False)
#function for login
def login():
        #intialise the variable
        user=text.get()
        passwor=text2.get()
        #connect to the datadase
        conn=pymysql.connect(host='localhost',user='root',password='Vegito',db='ayush')
        a=conn.cursor()
        a.execute("select * from fun where Username='"+user+"'and Password='"+passwor+"'")
        result=a.fetchall()
        count=a.rowcount
        if(count>0):
                win.destroy()
                subprocess.run(["python", "login2.py"])

        else:
                messagebox.showerror("message","Not login")

        
    
def forgot():
        win=Tk()
        win.config(bg="orange")
        win.geometry("350x270")
        win.title("Welcome to Forgot Password")
        def reset():
                #intialise the variable
                name=var.get()
                new=var2.get()
                old=var3.get()
                #check both password are same
                if(new==old):
                        #connect to the datadase
                        conn = pymysql.connect(host='localhost',user='root',password='Vegito',db='ayush')
                        mydb=conn.cursor()
                        mydb.execute("select * from fun where Username = '"+name+"'")
                        mydb.execute("update fun set Password='"+new+"' where Username = '"+name+"'")
                        conn.commit()
                        result=mydb.fetchall()
                        count=mydb.rowcount
                        if count>0:
                                messagebox.showinfo("Message","Successful")
                                
                        else:
                                messagebox.showerror("Message","INVALID")
                else:
                        messagebox.showerror("Message","Not match")
                        
        lb=Label(win,text="Username",width=10,bg="orange",font=15).grid(row=1,column=0,padx=10,pady=10)
        lb2=Label(win,text="New Password",width=15,bg="orange",font=15).grid(row=2,column=0,padx=10,pady=10)
        lb3=Label(win,text="Re-enter Password",width=15,bg="orange",font=15).grid(row=3,column=0,padx=10,pady=10)
        var=Entry(win)
        var.grid(row=1,column=1,padx=10,pady=10)
        var2=Entry(win)
        var2.grid(row=2,column=1,padx=10,pady=10)
        var3=Entry(win)
        var3.grid(row=3,column=1,padx=10,pady=10)
        btn=Button(win,text="Change",command=reset,font=10,bd=5,relief="raised").place(x=120,y=150)

def sign():
        sin=Tk()
        sin.config(bg="orange")
        sin.geometry("370x250")
        sin.title("Welcome to Sign up")
        def insert():
                #intialise the variable
                name=tx.get()
                username=tx2.get()
                password=tx3.get()
                #connect to the datadase
                try:
                        conn = pymysql.connect(host='localhost',user='root',password='Vegito',db='ayush')
                        mydb=conn.cursor()
                        mydb.execute("insert into fun(Name,Username,Password) values('"+name+"','"+username+"','"+password+"')")
                        conn.commit()
                        messagebox.showinfo("Message","Successful")
                      
                except:
                        conn.rollback()
                        messagebox.showerror("Message","Failed")
                conn.close()
        lb=Label(sin,text="Name",width=10,bg="orange",font=15).grid(row=1,column=0,padx=10,pady=10)    
        lb=Label(sin,text="Username",width=10,bg="orange",font=15).grid(row=2,column=0,padx=10,pady=10)
        lb2=Label(sin,text="Password",width=15,bg="orange",font=15).grid(row=3,column=0,padx=10,pady=10)
        tx=Entry(sin)
        tx.grid(row=1,column=1,padx=10,pady=10)
        tx2=Entry(sin)
        tx2.grid(row=2,column=1,padx=10,pady=10)
        tx3=Entry(sin)
        tx3.grid(row=3,column=1,padx=10,pady=10)
        btn=Button(sin,text="Submit",command=insert,font=5,bd=5,relief="raised").place(x=120,y=150)

        

#label 
lb=Label(win,text="ARTIFICIAL CAMERA",font=40,bd=10,relief="raised",width=50 ).grid(row=0)
#Frame 
frame2=Frame(win,bd=10,relief="raised",width=400,height=280,bg="orange").place(x=50,y=100)
frame3=Frame(win,bd=9,relief="raised",width=400,height=40).place(x=50,y=100)
lb1=Label(frame3,text="Login ",font=20).place(x=220,y=102)
lb2=Label(frame2,text="Username",font=20,width=10,bg="orange").place(x=100,y=150)
lb3=Label(frame2,text="Password",font=20,width=10,bg="orange").place(x=100,y=190)
#Entry Box
text=Entry(frame2)
text.place(x=270,y=150)
text2=Entry(frame2,show="*")
text2.place(x=270,y=190)
#Button
login=Button(frame2,text="Login",font=10,bd=5,relief="groove",command=login).place(x=100,y=250)
forget=Button(frame2,text="Forgot",font=10,bd=5,relief="groove",command=forgot).place(x=320,y=250)
sign=Button(frame2,text="Sign up",font=10,bd=5,relief="groove",command=sign).place(x=205,y=310)
win.mainloop()
