from tkinter import *

window = Tk()
window.title("Button Show")
window.minsize(width=500, height=500)

my_label = Label(text="I am a Label", font=("Aerial ", 24, "bold"))
my_label.pack()

my_label["text"] = "Lee bal"
my_label.config(text="Lee")

def clicked():
    my_label.config(text="Bro")
    print(my_label["text"])


button = Button(text="Clicking", command=clicked)
button.pack()




window.mainloop()




