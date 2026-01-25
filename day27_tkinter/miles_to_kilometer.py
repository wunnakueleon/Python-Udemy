from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

mile_label = Label(text="Miles", font=("Arial ", 24, "normal"))
mile_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Arial ", 24, "normal"))
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial ", 24, "normal"))
km_label.grid(column=2, row=1)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

km_output = Label(text="0", font=("Arial ", 24, "normal"))
km_output.grid(column=1, row=1)

def calculate():
    data = int(mile_input.get()) * 1.60934
    km_output.config(text=str(data))

    
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()

