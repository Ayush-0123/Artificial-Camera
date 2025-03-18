from tkinter import *
from tkinter import messagebox
import pymysql
import pymysql.cursors
import subprocess

win = Tk()
win.config(bg="gray")
win.geometry("500x400")
win.title("Welcome to Login")
win.resizable(False, False)

# Function for login
def login():
    user = text.get()
    passwor = text2.get()
    conn = pymysql.connect(host='localhost', user='', password='', db='')
    a = conn.cursor()
    a.execute("SELECT * FROM fun WHERE Username=%s AND Password=%s", (user, passwor))
    result = a.fetchall()
    count = a.rowcount
    if count > 0:
        win.destroy()
        subprocess.run(["python", "login2.py"])
    else:
        messagebox.showerror("message", "Incorrect detail,plz try again")
    conn.close()

# Function for forgot password (DOB added)
def forgot():
    win_forgot = Tk()
    win_forgot.config(bg="orange")
    win_forgot.geometry("350x320")  # increased height to accommodate new DOB field
    win_forgot.title("Forgot Password")
    
    # Added label with helpful message at the top
    Label(win_forgot, text="Forgot Password? Reset below", bg="orange", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)
    
    def reset():
        name = var.get()
        dob = var_dob.get()  # New entry for DOB
        new = var2.get()
        old = var3.get()
        if new == old:
            conn = pymysql.connect(host='localhost', user='', password='', db='')
            mydb = conn.cursor()
            # First, check if the DOB matches for the given username
            mydb.execute("SELECT dob FROM fun WHERE Username=%s", (name,))
            result = mydb.fetchone()
            if result:
                stored_dob = result[0]
                if stored_dob == dob:
                    mydb.execute("UPDATE fun SET Password=%s WHERE Username=%s", (new, name))
                    conn.commit()
                    messagebox.showinfo("Message", "Successful")
                else:
                    messagebox.showerror("Message", "DOB does not match")
            else:
                messagebox.showerror("Message", "Username not found")
            conn.close()
        else:
            messagebox.showerror("Message", "Not match")

    Label(win_forgot, text="Username", width=10, bg="orange", font=15).grid(row=1, column=0, padx=10, pady=10)
    Label(win_forgot, text="DOB(Y-M-D)", width=15, bg="orange", font=15).grid(row=2, column=0, padx=10, pady=10)
    Label(win_forgot, text="New Password", width=15, bg="orange", font=15).grid(row=3, column=0, padx=10, pady=10)
    Label(win_forgot, text="Re-enter Password", width=15, bg="orange", font=15).grid(row=4, column=0, padx=10, pady=10)
    
    var = Entry(win_forgot)
    var.grid(row=1, column=1, padx=10, pady=10)
    var_dob = Entry(win_forgot)  # New entry field for DOB
    var_dob.grid(row=2, column=1, padx=10, pady=10)
    var2 = Entry(win_forgot)
    var2.grid(row=3, column=1, padx=10, pady=10)
    var3 = Entry(win_forgot)
    var3.grid(row=4, column=1, padx=10, pady=10)
    
    Button(win_forgot, text="Change", command=reset, font=10, bd=5, relief="raised").place(x=120, y=260)

# Function for sign-up (DOB added)
def sign():
    sin = Tk()
    sin.config(bg="orange")
    sin.geometry("370x300")  # increased height to accommodate new DOB field
    sin.title("Sign up")
    
    # Added label with helpful message at the top
    Label(sin, text="Welcome User, let's get started!", bg="orange", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)
    
    def insert():
        name = tx.get()
        username = tx2.get()
        password = tx3.get()
        dob = tx4.get()  # New: DOB value from the entry
        try:
            conn = pymysql.connect(host='localhost', user='', password='', db='')
            mydb = conn.cursor()
            mydb.execute("SELECT * FROM fun WHERE Username=%s", (username,))
            if mydb.fetchone():
                messagebox.showerror("Message", "Username already exists. Choose a different one.")
                return
            # Insert the new record along with DOB
            mydb.execute("INSERT INTO fun (Name, Username, Password, dob) VALUES (%s, %s, %s, %s)", (name, username, password, dob))
            conn.commit()
            messagebox.showinfo("Message", "Successful")
        except:
            conn.rollback()
            messagebox.showerror("Message", "Failed")
        conn.close()

    Label(sin, text="Name", width=10, bg="orange", font=15).grid(row=1, column=0, padx=10, pady=10)    
    Label(sin, text="Username", width=10, bg="orange", font=15).grid(row=2, column=0, padx=10, pady=10)
    Label(sin, text="Password", width=15, bg="orange", font=15).grid(row=3, column=0, padx=10, pady=10)
    Label(sin, text="DOB(Y-M-D)", width=15, bg="orange", font=15).grid(row=4, column=0, padx=10, pady=10)
    
    tx = Entry(sin)
    tx.grid(row=1, column=1, padx=10, pady=10)
    tx2 = Entry(sin)
    tx2.grid(row=2, column=1, padx=10, pady=10)
    tx3 = Entry(sin)
    tx3.grid(row=3, column=1, padx=10, pady=10)
    tx4 = Entry(sin)  # New entry field for DOB
    tx4.grid(row=4, column=1, padx=10, pady=10)
    
    Button(sin, text="Submit", command=insert, font=5, bd=5, relief="raised").place(x=120, y=240)

# Function for remove details (new)
def remove():
    rem_win = Tk()
    rem_win.config(bg="orange")
    rem_win.geometry("350x200")
    rem_win.title("Remove User")
    
    # Added label with a message at the top
    Label(rem_win, text="Remove Account - Confirm your details", bg="orange", font=("Arial", 14, "bold")).grid(row=0, columnspan=2, pady=10)
    
    def remove_user():
        username = rem_user.get()
        password = rem_pass.get()
        conn = pymysql.connect(host='localhost', user='', password='', db='')
        mydb = conn.cursor()
        # Check if credentials are correct
        mydb.execute("SELECT * FROM fun WHERE Username=%s AND Password=%s", (username, password))
        if mydb.fetchone():
            # Delete only that user's record
            mydb.execute("DELETE FROM fun WHERE Username=%s AND Password=%s", (username, password))
            conn.commit()
            messagebox.showinfo("Message", "User details removed successfully")
        else:
            messagebox.showerror("Message", "Invalid credentials")
        conn.close()
    
    Label(rem_win, text="Username", width=10, bg="orange", font=15).grid(row=1, column=0, padx=10, pady=10)
    Label(rem_win, text="Password", width=10, bg="orange", font=15).grid(row=2, column=0, padx=10, pady=10)
    
    rem_user = Entry(rem_win)
    rem_user.grid(row=1, column=1, padx=10, pady=10)
    rem_pass = Entry(rem_win, show="*")
    rem_pass.grid(row=2, column=1, padx=10, pady=10)
    
    Button(rem_win, text="Remove", command=remove_user, font=10, bd=5, relief="raised").place(x=120, y=150)

# --- Updated Toggle Password Functionality ---
def toggle_password():
    # If the password is hidden (masked), show it and set icon to open eye (👁)
    if text2.cget('show') == '*':
        text2.config(show='')
        btn_eye.config(text="👁")
    else:
        text2.config(show='*')
        btn_eye.config(text="🙈")

# UI Components for the main window
Label(win, text="ARTIFICIAL CAMERA", font=40, bd=10, relief="raised", width=50).grid(row=0)
frame2 = Frame(win, bd=10, relief="raised", width=400, height=280, bg="orange").place(x=50, y=100)
lb1 = Label(win, text="Login ", font=20).place(x=220, y=102)
Label(win, text="Username", font=20, width=10, bg="orange").place(x=100, y=150)
Label(win, text="Password", font=20, width=10, bg="orange").place(x=100, y=190)

text = Entry(win)
text.place(x=270, y=150)

# Password entry with toggle button (initially password is hidden and icon is set to monkey 🙈)
text2 = Entry(win, show="*", font=("Arial", 12))
text2.place(x=270, y=190, width=150)
btn_eye = Button(win, text="🙈", command=toggle_password, bd=0, relief="flat", bg="orange")
btn_eye.place(x=430, y=190)

Button(win, text="Login", font=10, bd=5, relief="groove", command=login).place(x=100, y=250)
Button(win, text="Forgot", font=10, bd=5, relief="groove", command=forgot).place(x=320, y=250)
Button(win, text="Sign up", font=10, bd=5, relief="groove", command=sign).place(x=100, y=310)
Button(win, text="Remove", font=10, bd=5, relief="groove", command=remove).place(x=320, y=310)

win.mainloop()
