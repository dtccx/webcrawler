import Tkinter
import mas
import tkMessageBox

ui = Tkinter.Tk()
ui.geometry('450x380')
ui.configure(background='light green')
L1 = Tkinter.Label(ui, text="user")
L1.place(x = 50, y = 50)
user_name = Tkinter.StringVar()
user_name.set("operr126")
E1 = Tkinter.Entry(ui, width=30, textvariable = user_name)
E1.place(x = 150, y = 50)

L2 = Tkinter.Label(ui, text="password")
L2.place(x = 50, y = 150)
pwd = Tkinter.StringVar()
pwd.set("Hawkins2@")
E2 = Tkinter.Entry(ui, width=30, textvariable = pwd)
E2.place(x = 150, y = 150)

def get_data():
    content = mas.get_content(user_name.get(), pwd.get())

    if content == None:
        tkMessageBox.showerror('Error 01','Cannot connect to server')
    else:
        if mas.get_excel(content):
            tkMessageBox.showinfo('Success','Get all the data')
        else:
            tkMessageBox.showerror('Error 02','Cannot get data')

def get_correction():
    content = mas.get_correction(user_name.get(), pwd.get())
    if content == True:
        tkMessageBox.showinfo('Success','Get all the data')
    else:
        tkMessageBox.showerror('Error','Cannot get data')

button = Tkinter.Button(ui, text = 'get drivers & vehicles data', command = get_data)
button.place(x = 130, y = 250)

button2 = Tkinter.Button(ui, text = 'get correction', command = get_correction)
button2.place(x = 130, y = 300)

ui.mainloop()
