from tkinter import *

myWindow = Tk()

def closeMywindow():
    myWindow.quit()

def throwToTableMenu():
    closeMywindow()
    tableMenu = Tk()
    tableMenu.title('Edit your table')
    tableMenu.configure(bg='white')
    tableMenu.mainloop()

def getStart():
    myWindow.title('Table creator')
    myWindow.configure(bg='#c1d5d2')
    Label(myWindow, text='Press the button below to start creating your table',
                font=("TimesNewRoman", 13), bg='#c1d5d2').grid(column = 5 , row = 5, sticky= 'e')

    Button(myWindow, text='Создать таблицу', bg='#808080',
                fg='#000000',command = throwToTableMenu).grid(column=5)

    Button(myWindow, text='quit',  bg='#808080',
        fg='#000000', command=closeMywindow).grid(column=100, row=100)
    myWindow.mainloop()


getStart()



