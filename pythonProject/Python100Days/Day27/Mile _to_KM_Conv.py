from tkinter import *

FONT = "Aerial,20,Bold"
MILES = 1.609344

def cal_miles_to_km():
    miles = float(miles_entry.get())
    km = str(round(miles * MILES))
    KM_ENTRY.delete(0,END)
    KM_ENTRY.insert(0,km)


window = Tk()
window.minsize(350,250)
window.title("Mile to KM Converter")
window.config(padx=40,pady=40)

#text box:
miles_entry = Entry(width=10,borderwidth=5,border="4",font=FONT)
miles_entry.insert(END,"0")
miles_entry.grid(column=4,row=5,padx=10,pady=10)

#lable:
miles_label = Label(text="Miles",font=FONT)
miles_label.grid(column=5,row=5,padx=10,pady=10)

#isequalto
is_Equal_label = Label(text="is Equal to",font=FONT)
is_Equal_label.grid(padx=5,pady=5)

#KM text box
KM_ENTRY = Entry(width=10,border="4",font=FONT)
KM_ENTRY.grid(column=4,row=7,padx=10,pady=10)

#km
km_label = Label(text="KM.",font=FONT)
km_label.grid(column=5,row=7)


#button
button = Button(text="Calculate",height=1,width=10,command=cal_miles_to_km,font=FONT)
button.grid(column=4,row=8,padx=5,pady=5)

window.mainloop()