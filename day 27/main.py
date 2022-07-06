from tkinter import *

def button_clicked():
    #print("i got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=200)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.pack()
#my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=25)



button = Button(text="click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

new_button = Button(text="c'est un nouvelle button", font=("Arial", 24, "normal"))
new_button.grid(column=2, row=0)

input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)




window.mainloop()