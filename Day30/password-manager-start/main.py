from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def search_function():
    web = Website_entry.get()
    email = email_entry.get()
    try:
        with open("Day30/password-manager-start/data.json","r") as file:
                data = json.load(file)
        if web in data:
            p_word = data[web]['password']
            messagebox.showinfo(title=web,message=f"Email: {email}\nPassword: {p_word}")
        else:
             messagebox.showinfo(title="Error",message="No details for the website exists.")            
    except:
        messagebox.showinfo(title="Error",message="No Data File Found.")   

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_function():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','&','(',')','*','+']  
    nr_letters = 6
    nr_symbols = 4
    nr_numbers = 2

    password=[]
    for i in range(0,nr_letters):
        password.append(random.choice(letters))
    for i in range(0,nr_symbols):
        password.append(random.choice(symbols))
    for i in range(0,nr_numbers):
        password.append(random.choice(numbers))   
    random.shuffle(password)
    new_pass = "".join(password) 
    password_entry.insert(0,new_pass)  
    pyperclip.copy(new_pass)  

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_function():
    web = Website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
         web: {
            "email": email,
            "password": password
        }
    }

    if web=="" or password=="":
        messagebox.showinfo(title="Oops",message="Please don't leave any fiels empty!")
    else:    
        try:
            with open("Day30/password-manager-start/data.json","r") as file:
                #Reading the old data
                data = json.load(file)
        except:
                with open("Day30/password-manager-start/data.json","w") as file: 
                    json.dump(new_data, file, indent = 4)
        else:           
            #Updating old data with new data
            data.update(new_data)
            with open("Day30/password-manager-start/data.json","w") as file:    
                #Saving updated data
                json.dump(data, file, indent = 4)
        finally:        
            Website_entry.delete(0,END)
            password_entry.delete(0,END)    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width = 200, height = 200)
lock_png = PhotoImage(file = "Day29\password-manager-start\logo.png")
canvas.create_image(100,100,image = lock_png)
canvas.grid(column=1,row=0)

Website_label = Label(text = "Website:")
Website_label.grid(column=0,row=1)
email_label = Label(text = "Email/Username:")
email_label.grid(column=0,row=2)
Password_label = Label(text = "Password:")
Password_label.grid(column=0,row=3)

Website_entry = Entry(width=21)
Website_entry.grid(column=1,row=1)
Website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"harijanakiraman12@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

search_button = Button(text="Search", width=15,command=search_function)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate Password", width=15,command=password_function)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_function)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()