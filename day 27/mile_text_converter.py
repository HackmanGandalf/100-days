from tkinter import *

def calculator():
    answer = float(input.get()) * 1.60934
    result.config(text=answer)

def calculator2():
    answer = float(input2.get()) * 0.3048
    result2.config(text=answer)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=50)
window.config(padx=15, pady=15)

#############################################################################
### mile to km converter ####
Topic1 = Label(text="Miles to Kilometer converter", font=("Arial",  10, "bold"))
Topic1.grid(row=0, column=1)
Topic1.config(padx=5, pady=5)

input = Entry(width=10)
input.focus()
input.grid(row=1, column=1)
#input.config(padx=5, pady=5)

miles = Label(text="Miles", font=("Arial",  10, "normal"))
miles.grid(row=1, column=2)
miles.config(padx=5, pady=5)

is_equal_to = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_to.grid(row=2, column=0)
is_equal_to.config(padx=5, pady=5)

result = Label(text=0, font=("Arial", 10, "normal"))
result.grid(row=2, column=1)
result.config(padx=5, pady=5)

km = Label(text="km", font=("Arial", 10, "normal"))
km.grid(row=2, column=2)
km.config(padx=5, pady=5)

calculate = Button(text="Calculate", font=("Arial", 10, "normal"), command=calculator)
calculate.grid(row=3, column=1)
#############################################################################

################################################################################
###convert foot to meter #####
Topic1 = Label(text="Foot to Meter Converter", font=("Arial",  10, "bold"))
Topic1.grid(row=5, column=1)
Topic1.config(padx=5, pady=5)

input2 = Entry(width=10)
input2.focus()
input2.grid(row=6, column=1)
#input.config(padx=5, pady=5)

feet = Label(text="Foot", font=("Arial",  10, "normal"))
feet.grid(row=6, column=2)
feet.config(padx=5, pady=5)

is_equal_to = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_to.grid(row=7, column=0)
is_equal_to.config(padx=5, pady=5)

result2 = Label(text=0, font=("Arial", 10, "normal"))
result2.grid(row=7, column=1)
result2.config(padx=5, pady=5)

meter = Label(text="Meter", font=("Arial", 10, "normal"))
meter.grid(row=7, column=2)
meter.config(padx=5, pady=5)

calculate2 = Button(text="Calculate", font=("Arial", 10, "normal"), command=calculator2)
calculate2.grid(row=8, column=1)





window.mainloop()