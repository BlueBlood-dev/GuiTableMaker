import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

def setGeometry():
    root.resizable(False, False)
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2.5 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/3.5 - windowHeight/2)
    root.geometry('+{}+{}'.format(positionRight, positionDown))

def getStart():
    root.title('TableMaker')
    root.configure(bg='#ffcccc')
    frame1 = tk.Frame(master=root, relief=tk.FLAT,
                      borderwidth=50, bg='#ffccff')
    helloText = tk.Label(master=frame1, bg='#ffccff',
                         text='Hi, this is a simple TableMaker app', font=('TimesNewRoman', 20))
    helloText.pack()
    frame1.pack(fill=tk.BOTH, side=tk.TOP)
    ButtonFrame = tk.Frame(master=root, relief=tk.FLAT, bg='#ff8080', borderwidth=20)
    tk.Button(master=ButtonFrame, relief=tk.RAISED, text='Press me to start', bg='#ff8080', fg='#000099',
                                width=30, font=('TimesNewRoman', 25), command = throwToTableMenu).pack()
    ButtonFrame.pack(fill = tk.BOTH, side = tk.TOP)
    ImageFrame = tk.Frame(master=root, relief=tk.FLAT,
                          borderwidth=70, bg='#ffcccc')
    img = ImageTk.PhotoImage(Image.open('heart22.png'))
    tk.Label(master = ImageFrame, image = img ).pack()
    ImageFrame.pack(fill=tk.BOTH, side=tk.TOP)
    setGeometry()
    root.mainloop()


def setMainFrames():
    pass

def throwToTableMenu():
    pass


getStart()
