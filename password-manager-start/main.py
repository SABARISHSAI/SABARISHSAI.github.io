from tkinter import *
from tkinter import messagebox, END
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")
# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get().upper()
    try:
        with open("data.json","r") as data:
            dict1=json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(message="no details exist")
    else:
        with open("data.json", "r") as data:
            dict1 = json.load(data)
            try:
                messagebox.showinfo(message = f"email:{dict1[website]["email"]}\npassword:{dict1[website]["password"]}")
            except KeyError:
                messagebox.showinfo(message="no such website exists")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().upper()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="oops!", message="you have left some fields empty, please fill it")
    else:
        try:
            with open("data.json", "r") as pwf:
                data = json.load(pwf)
        except FileNotFoundError:
            with open("data.json", "w") as pwf:
                json.dump(new_data, pwf, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as pwf:
                json.dump(data, pwf, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.pack()
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command=lambda: generate_password())
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=36, command=lambda: save())
add_button.grid(row=5, column=1, columnspan=3)
search_button = Button(text="search", width=15, command=lambda: find_password())
search_button.grid(row=1, column=3)

window.mainloop()