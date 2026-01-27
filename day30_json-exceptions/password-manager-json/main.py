from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_input.delete(0, END)
    #Password Generator Project
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    letter_list = [choice(letters) for letter in range(randint(8, 10))]
    symbol_list = [choice(symbols) for symbol in range(randint(2, 4))]
    number_list = [choice(numbers) for number in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list

    shuffle(password_list)

    password = ("").join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

    print(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_inputs():
    website_input_get = website_input.get()
    email_input_get = email_input.get()
    password_input_get = password_input.get()

    if len(password_input_get) == 0 or len(website_input_get) == 0:
        password_check = messagebox.askretrycancel(title="Password or Website Needs Modification", message=f"Password or Website cannot be empty")

    else:
        is_ok = messagebox.askokcancel(title=website_input_get, message=f"These are the details entered: \nEmail: {email_input_get} "
                            f"\nPassword: {password_input_get} \nIs it Ok to save?")
        
        if is_ok:

            with open("password-manager-start/password_manager.txt", mode="a") as password_manage_file:
                password_manage_file.write("\n" + f"{website_input_get} | {email_input_get} | {password_input_get}")

            website_input.delete(0, END)
            password_input.delete(0, END)

        print(website_input_get)
        print(email_input_get)
        print(password_input_get)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
key_image = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(100, 95, image=key_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, "wunna@gmail.com")

password_input = Entry(width=18)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=11, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=get_inputs)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()




