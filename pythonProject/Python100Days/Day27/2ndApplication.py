from tkinter import *
from tkinter import messagebox


def button_click():
    new_text = input.get()
    my_label.config(text=new_text)

def show_message_box():
    messagebox.showinfo("Message", "Button is clicked")

window = Tk()
window.title("First Applicaiton")
window.minsize(800,500)

my_label = Label(text="I am a Label", font=("Aerial", 24, "bold"))
my_label.config(text="Text Added",padx=5,pady=5)
my_label.grid(column=0,row=0)


#button component
my_button = Button(text="Click Me",command=button_click)
my_button.grid(column=1,row=1,padx=5,pady=5)


#2nd button
my_button2 = Button(text="Submit", command=show_message_box)
my_button2.grid(column=3,row=0)

#Entry
input = Entry(width=25)
print(input.get())
input.grid(column=3,row=2,padx=10,pady=10)




window.mainloop()