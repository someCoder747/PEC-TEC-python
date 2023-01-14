from tkinter import *
def Getresult():

    hotorcold = str(txthotorcold.get())
    temper = float(txttemp.get())

    if (hotorcold == 'H'):
        lblresult.config(text="Heat Temperature: " temper, font=("Arial", 18), bg="yellow", fg="black")
        lblresult.place(x=10, y=150)

    elif (hotorcold == 'C'):
        lblresult.config(text="Cool Temperature: " temper, font=("Arial", 18), bg="yellow", fg="black")
        lblresult.place(x=10, y=150)


window = Tk()
window.geometry("250x250")
window.title("Temperature Container Menu")
window.config(bg="yellow")

lblhotorcold = Label(window, text="Heat/Cool: ", font=("Arial", 12), bg= "yellow", fg="black")
lblhotorcold.place (x=10, y=30)

lbltemp = Label(window, text="Temperature: ", font=("Arial", 12), bg= "yellow", fg="black")
lbltemp.place (x=10, y=60)

txthotorcold = Entry (window)
txthotorcold.place (x=91, y=33)

txttemp = Entry (window)
txttemp.place (x=110, y=63)

btnenter = Button(window, text= "Enter", font=("Arial", 18), bg= "gray", fg="black", command=Getresult)
btnenter.place (x=10, y=100)

lblresult = Label(window, text= "----------------", font=("Arial", 18), bg= "yellow", fg="black")
lblresult.place (x=10, y=170)

window.mainloop()
