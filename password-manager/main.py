import json
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import *

def gen_password():
    pass_in.delete(0,END)
    letters = list("abcdefghijklmnopqrstuvwxyz")
    numbers = list("1234567890")
    symbols = list("!@#$%^&*()_-")

    l = [choice(letters) for _ in range(randint(8, 10))]
    s = [choice(symbols) for _ in range(randint(2, 4))]
    n = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = l + s + n
    shuffle(password_list)
    password = ''.join(password_list)
    pass_in.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    site = web_in.get()
    email = email_in.get()
    pas = pass_in.get()

    new_entry = {
        site: {
            "Email": email,
            "Password": pas
        }
    }

    if site == "" or email == "" or pas == "":
        messagebox.showerror(title="Invalid", message="Please make sure you haven't left any field empty")
        return

    is_ok = messagebox.askokcancel(title= f"{site}", message=f"These are the details entered: \nEmail: {email}\nPassword: {pas}\n is it ok to save?")

    def write(d):
        df = open("data.json", "w")
        json.dump(d, df, indent=4)
        df.close()

    if is_ok:
        try:
            df = open("data.json", "r")
            data = json.load(df)
            data.update(new_entry)
        except FileNotFoundError:
            write(new_entry)
        else:
            write(data)
        finally:
            web_in.delete(0,END)
            pass_in.delete(0, END)

def search():
    site = web_in.get()
    try:
        df = open("data.json", "r")
        data = json.load(df)
        email = data[site]["Email"]
        pas = data[site]["Password"]
    except KeyError:
        messagebox.showerror("Invalid",f"{site} not registered")
    except FileNotFoundError:
        messagebox.showerror("Invalid",f"dataset is empty")
    else:
        email_in.delete(0, END)
        pass_in.delete(0, END)
        messagebox.showinfo(title=site,message=f"Email: {email}\n Password: {pas}")
        email_in.insert(0,email)
        pass_in.insert(0, pas)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

logo = PhotoImage(file="logo.png")

canvas = Canvas(width=200,height=200)
canvas.create_image(100,100, image=logo)
canvas.grid(row=0,column=1)


#labels
website = Label(text="Website:")
website.grid(row=1,column=0)

email_user = Label(text="Email/Username:")
email_user.grid(row=2,column=0)

password = Label(text="Password:")
password.grid(row=3,column=0)

#Entries
web_in = Entry(width=33)
web_in.grid(row=1,column=1,sticky=W)
web_in.focus()

email_in = Entry(width=52)
email_in.grid(row=2,column=1,columnspan=2,sticky=W)
email_in.insert(0,"rushabh22runwal@gmail.com")

pass_in = Entry(width=33)
pass_in.grid(row=3,column=1, sticky=W)


#buttons
gen_pass = Button(text="Generate Password",command=gen_password)
gen_pass.grid(row=3,column=2, sticky=W)

add_btn = Button(text="Add",width=44,command=add_data)
add_btn.grid(row=4,column=1,columnspan=2, sticky=W)

search_btn = Button(text="Search",width=14,command=search)
search_btn.grid(row=1,column=2)

window.mainloop()