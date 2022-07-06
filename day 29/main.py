from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- 
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0, password)
    pyperclip.copy(password)

#----------------------------- SEARCHER -------------------------------------#
def find_password():
    website = website_input.get()
    try:
        with open("100-days-of-code/day 29/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} found.")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("100-days-of-code/day 29/data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("100-days-of-code/day 29/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("100-days-of-code/day 29/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

                
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passowrd Mananger")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_file = PhotoImage(file="100-days-of-code/day 29/logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:",)# font=("Arial", 10, "normal"))
website_label.grid(row=1, column=0)
passwordLabel = Label(text="Password:",)# font=("Arial", 10, "normal"))
passwordLabel.grid(row=3, column=0)


email_username = Label(text="Email/Username:",)# font=("Arial", 10, "normal"))
email_username.grid(row=2, column=0, )

website_input = Entry(width=43)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=43)
email_input.insert(0, "hackman@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=25)
password_input.grid(row=3, column=1)




generate = Button(text="Generate Password", command=generator)# font=("Arial", 10, "normal"))
generate.grid(row=3, column=2)
#generate.config(width=10)

add = Button(text="Add", command=save_password)# font=("Arial", 10, "normal"))
add.grid(row=4, column=1, columnspan=2)
add.config(width=36)

search = Button(text="Search", width=13, command=find_password)
search.grid(row=1, column=2)




window.mainloop()