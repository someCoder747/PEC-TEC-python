from tkinter import *

window = Tk()
var = IntVar()

lbltemp = Label(window, text="Temperature:")
lblduration = Label(window, text="Duration of Temperature:")
lblspeed = Label(window, text="Speed of Heating/Cooling:")

lbltemp.grid(row = 0, column = 0, sticky = W, pady = 2)
lblduration.grid(row = 1, column = 0, sticky = W, pady = 2)

txttemp = Entry(window)
txtduration = Entry(window)

txttemp.grid(row = 0, column = 1, sticky = W, pady = 2)
txtduration.grid(row = 1, column = 1, sticky = W, pady = 2)

celsiusCHKBTN = Radiobutton(window, text = "Celsius", variable=var, value=1)
celsiusCHKBTN.grid(sticky= W)

fahrenheitCHKBTN = Radiobutton(window, text = "Fahrenheit", variable=var, value=2)
fahrenheitCHKBTN.grid(sticky= W)

kelvinCHKBTN = Radiobutton(window, text = "Kelvin", variable=var, value=3)
kelvinCHKBTN.grid(sticky= W)

def CancelFunction():
    cancel = "Process Canceled"
    label.config(text=cancel)
    nothing = "               "
    labeltwo.config(text=nothing)

def EnterFunction():
    if celsiusCHKBTN:
        process = "Temperature: " + txttemp.get() + " °C", "Duration: " + txtduration.get() + " minutes"
        labeltwo.config(text=process)
    elif fahrenheitCHKBTN:
        process = "Temperature: " + txttemp.get() + " °F", "Duration: " + txtduration.get() + " minutes"
        labeltwo.config(text=process)
    elif kelvinCHKBTN:
        process = "Temperature: " + txttemp.get() + " °K", "Duration: " + txtduration.get() + " minutes"
        labeltwo.config(text=process)

def ResetFunction():
    txttemp.delete(0,END)
    txtduration.delete(0,END)
    if ResetFunction():
        celsiusCHKBTN.set(0)
        fahrenheitCHKBTN.set(0)
        kelvinCHKBTN.set(0)

b1 = Button(window, text = "Enter", command=EnterFunction)
b2 = Button(window, text = "Reset", command=ResetFunction)
b3 = Button(window, text = "Cancel", command=CancelFunction)

b1.grid(row = 4, column = 2, sticky = S)
b2.grid(row = 4, column = 3, sticky = S)
b3.grid(row = 4, column = 4, sticky = S,)

label = Label(window)
label.grid()
labeltwo = Label(window)
labeltwo.grid()
window.mainloop()
