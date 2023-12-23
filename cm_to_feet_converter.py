from tkinter import *

wn = Tk()
wn.title("CM to FEET CONVERTER")
wn.config(padx=50, pady=50)

def cm_to_feet():
    cm = float(cm_input.get())
    feet = round(cm / 30.48)
    feet_result_label.config(text=f"{feet}")



cm_input = Entry(width=7)
cm_input.grid(row=0, column=1)

cm_label = Label(text="CM")
cm_label.grid(row=0, column=2)

feet_result_label = Label(text="0")
feet_result_label.grid(row=1, column=1)

feet_label = Label(text="FEET")
feet_label.grid(row=1, column=2)

convert_button = Button(text="Convert", command=cm_to_feet)
convert_button.grid(row=2, column=1)

wn.mainloop()