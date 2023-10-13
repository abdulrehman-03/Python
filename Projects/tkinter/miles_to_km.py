from tkinter import *

window = Tk()
window.title("Tkinter GUI")
window.minsize(width=300, height=130)
window.config(padx=20, pady=15)


def calculate():
    miles = int(mile.get())
    km = round(miles * 1.609344, 1)
    kms.config(text=km)


mile = Entry(width=7)
mile.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)
mile_label.config(padx=10)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)
equal_label.config(padx=15, pady=10)

kms = Label(text=0)
kms.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=10)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
