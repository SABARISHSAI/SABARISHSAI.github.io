from tkinter import *


window = Tk()
window.title("mile to km converter")
window.config(padx=25,pady=25)



def miles_to_km():
    try:
        miles = float(miles_input.get())  # Convert input to float
        km = round(miles * 1.60934)  # Conversion factor
        kilometer_result_label.config(text=f"{km}")
        kilometer_result_label.grid(column = 1, row=1)
    except ValueError:
        return "Invalid input. Please enter a number."

miles_input = Entry(width=7)
miles_input.grid(column= 1,row=0)


miles_label = Label(text = "Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)







window.mainloop()
