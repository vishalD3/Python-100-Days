from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
              "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbol = ["@", "#", "$", "%", "&", "*", "_", "=", "+", "<", ">", "?"]

    password_letter = [choice(letter) for _ in range(randint(8,10))]
    password_symbol = [choice(symbol) for _ in range(randint(2,4))]
    password_numbers = [choice(number) for _ in range(randint(2,4))]

    password_list = password_letter + password_symbol +  password_numbers
    shuffle(password_list)

    passwrd= "".join(password_list)
    password_entry.insert(0,passwrd)
    pyperclip.copy(passwrd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password_txt = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password_txt,
        }
    }

    if len(website) == 0 or len(password_txt) == 0:
        messagebox.showinfo(title="Oops", message="Do not leave any field empty")

    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- Find PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password_txt = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} "
                                                       f"\nPassword: {password_txt}")
        if website not in data:
            messagebox.showinfo(title="Error", message=f"Data is not present for {website}. "
                                                       "\n Please use Add button" )
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0,column=1)

#Label
website_name = Label(text="Website:")
website_name.grid(row=1,column=0)
email_username = Label(text="Email/Username:")
email_username.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)


#Entries
website_entry = Entry(width=30)
website_entry.grid(row=1,column=1,padx=5)
website_entry.focus()
email_username_entry = Entry(width=49)
email_username_entry.grid(row=2,column=1,columnspan=2,padx=5)
email_username_entry.insert(0,"abc@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3,column=1,padx=5)

#buttons:
generate_Password_button = Button(text="Generate Password",command=password_generator)
generate_Password_button.grid(row=3, column=2,pady=5)
add_button = Button(text="Add", width=42,command=save)
add_button.grid(row=4,column=1,columnspan=2,padx=10)
search_Button = Button(text="Search",command=find_password)
search_Button.grid(row=1,column=2,pady=5)
window.mainloop()