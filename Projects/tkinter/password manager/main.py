from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# Password Generator


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# SAVE PASSWORD


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print(len(password))
    print(len(email))
    print(len(website))

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        proceed = messagebox.askyesno(title=website.title(), message=f"Email/User: {email} \nPassword: {password} \n"
                                                                     f"Save?")
        if proceed:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# UI SETUP


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, padx=15, pady=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, padx=15, pady=2)
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1, pady=2)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.config(borderwidth=1, justify="left")
generate_button.grid(row=3, column=2, sticky="w")
add_button = Button(text="Add", width=44, command=save)
add_button.config(borderwidth=1)
add_button.grid(row=4, column=1, columnspan=2, pady=2)

window.mainloop()
