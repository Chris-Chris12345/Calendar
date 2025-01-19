from  tkinter import *

import calendar


def showCal():
    new_gui = Tk()
    new_gui.title("Calendar")
    new_gui.geometry("550x600")
    new_gui.config(background="white")

    year_fetch = int(year_input.get())
    year_content = calendar.calendar(year_fetch)
    cal_year = Label(new_gui,text=year_content,font=("Consolas 10 bold"))
    cal_year.grid(row=5,column=1,padx=50)

    new_gui.mainloop()


#driver code

if __name__ == "__main__":
    gui = Tk()
    gui.title("Calendar")
    gui.geometry("325x350")
    gui.config(background="white")

    calendar_label = Label(gui,text="Calendar",font=("Comic sans",40,"bold"),bg="blue",fg="white")
    enteryear_label = Label(gui,text="Enter year",font=("Comic sans",25),bg="red",fg="black")

    year_input = Entry(gui,font=("Comic sans",20),bg="grey",fg="blue")
    show_button = Button(gui,text="Show calendar",font=("Times new Roman",20,"italic"),bg="black",fg="white",command=showCal)
    exit_button = Button(gui,text="EXIT",font=("Arial",25),command=exit)


    calendar_label.grid(row=1,column=1)
    enteryear_label.grid(row=2,column=1)
    year_input.grid(row=3,column=1)
    show_button.grid(row=4,column=1)
    exit_button.grid(row=6,column=1)

    gui.mainloop()
