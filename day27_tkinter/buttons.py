from tkinter import *

window = Tk()
window.title("Button Show")
window.minsize(width=500, height=500)

my_label = Label(text="I am a Label", font=("Arial ", 24, "bold"))
my_label.pack()

my_label["text"] = "Lee bal"
my_label.config(text="Lee")

def clicked():
    text = input.get()
    my_label.config(text=f"{text}")
    print(my_label["text"])


input = Entry(width=10)

print(input.get())
button = Button(text="Clicking", command=clicked)
button.pack()
input.pack()





window.mainloop()




