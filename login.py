import tkinter
import os
import subprocess
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry('840x540')
window.configure(bg="#ECB390")
window.iconbitmap('login.ico')

def login():
    username = "pythonproject"
    password = "01234"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        open_python_file('C:\\Users\\ASUS\\Downloads\\project1.py')
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def open_python_file(file_path):
    try:
        os.system(f'python {file_path}')
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Failed to open file: {e}")

frame = tkinter.Frame(bg="#ECB390")

login_label = tkinter.Label(frame, text="Login Page", bg="#ECB390", fg='#002B5B', font=("Arial", 40), justify="center")
username_label = tkinter.Label(frame, text="Username:", bg="#ECB390", fg='#002B5B', font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 40), justify="center")
password_label = tkinter.Label(frame, text="Password:", bg="#ECB390", fg='#002B5B', font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 40), justify="center")
button_frame = tkinter.Frame(frame, bg="#ECB390")
login_button = tkinter.Button(button_frame, text="Login", bg="#4CBB17", fg="#FFFFFF", font=("Arial", 20), command=login)
exit_button = tkinter.Button(button_frame, text="Exit", bg="#FF0000", fg="#FFFFFF", font=("Arial", 20), command=exit)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0, columnspan=2, pady=10)
username_entry.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="ew")
password_label.grid(row=3, column=0, columnspan=2, pady=10)
password_entry.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="ew")
button_frame.grid(row=5, column=0, columnspan=2, pady=20)
login_button.grid(row=0, column=0, padx=5)
exit_button.grid(row=0, column=1, padx=5)

frame.pack()

window.mainloop()
