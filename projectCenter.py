from tkinter import *


def addtolist():
    projectlist = [entry.get(), entry1.get(), entry2.get(), entry3.get()]
    print(projectlist)

root = Tk()

root.geometry("450x300")

label = Label(root, text="Employees I.D. number: ")
label.place(x=40, y=0)
entry = Entry(bd=5)
entry.place(x=250, y=0)

label1 = Label(root, text="Name of your project: ")
label1.place(x=40, y=40)
entry1 = Entry(bd=5)
entry1.place(x=250, y=40)

label2 = Label(root, text="Team lead on project: ")
label2.place(x=40, y=80)
entry2 = Entry(bd=5)
entry2.place(x=250, y=80)

label3 = Label(root, text="Time spent on project this week: ")
label3.place(x=40, y=120)
entry3 = Entry(bd=5)
entry3.place(x=250, y=120)

submit = Button(root, text="Submit", command = addtolist)
submit.place(x=150, y=160)

root.mainloop()

