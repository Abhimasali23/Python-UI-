from tkinter import *

def button_clicked():
    print("Do something")

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am Label", font=("Times New Roman", 24))
my_label.config(text="New text")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)

# Entry
input = Entry()
input.grid(column=4, row=4)
print(input.get())

# New Button
new_button = Button(text="Touch Me", command=button_clicked)
new_button.grid(column=3, row=1)






window.mainloop()
