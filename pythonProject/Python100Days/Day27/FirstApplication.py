
from tkinter import *



window = Tk()
window.title("First Applicaiton")
window.minsize(800,500)

my_label = Label(text="I am a Label", font=("Aerial", 24, "bold"))
my_label.pack()

#edit component of label
#my_label["text"] = "My text"
my_label.config(text="My First application")

def button_click():
    new_text = input.get()
    my_label.config(text=new_text)

#button component
my_button = Button(text="Click Me",command=button_click)
my_button.pack()


#Entry
input = Entry(width=25)
input.pack()
input.insert(END,"Write anything...")

#text

text = Text(height=5,width=20)
#put cursor in text box
text.focus()
text.insert(END,"You can multiple lines of text")
print(text.get("1.0",END))
text.pack()

#spinbox

def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=1, to=10, width=5,command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)

scale = Scale(from_=1,to=100,command=scale_used)
scale.pack()

#checkbox

def checkboxbutton_used():
    print(checkbox_state.get())

checkbox_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checkbox_state, command=checkboxbutton_used)
checkbox_state.get()
checkbutton.pack()

#radio button

def radio_button_used():
    print(radio_button_state.get())

radio_button_state = IntVar()

radio_button1 = Radiobutton(text="Option1", value=1, variable = radio_button_state,
                            command=radio_button_used)

radio_button2 = Radiobutton(text="Option2", value=2, variable = radio_button_state,
                            command=radio_button_used)

radio_button1.pack()
radio_button2.pack()


#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Orange", "Pears", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()