from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

    new_data = {
        website_input_get :{
            "email": email_input_get,
            "password": password_input_get
        }
    }

    if len(password_input_get) == 0:
        password_check = messagebox.askretrycancel(title="Password or Website Needs Modification", message=f"Password or Website cannot be empty")

    else:
        
        try:
            with open("password-manager-json/data.json", "r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("password-manager-json/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("password-manager-json/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

            print(website_input_get)
            print(email_input_get)
            print(password_input_get)


def search_password():
    website_get = website_input.get()
    with open("password-manager-json/data.json") as data_file:
        data = json.load(data_file)

    try:
        email = data[website_get]["email"]
        password = data[website_get]["password"] 
    except KeyError:
        print("No Key")
        no_key = messagebox.showinfo(title="keyError", message=f"{website_get} \n Not Found")
    else:
        key_found = messagebox.showinfo(title=website_get, message=f"{data[website_get]["email"]} \n{data[website_get]["password"]}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
key_image = PhotoImage(file="password-manager-json/logo.png")
canvas.create_image(100, 95, image=key_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=18)
website_input.grid(column=1, row=1, columnspan=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, "wunna@gmail.com")

password_input = Entry(width=18)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=get_inputs)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search_password, width=10)
search_button.grid(column=2, row=1)

window.mainloop()




