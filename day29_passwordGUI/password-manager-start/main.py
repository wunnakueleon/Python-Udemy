from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=18)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=11)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()




