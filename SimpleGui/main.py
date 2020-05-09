import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

def setGeometry(root):
    root.resizable(False, False)
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2.8 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/3.5 - windowHeight/2)
    root.geometry('+{}+{}'.format(positionRight, positionDown))

def setFrames():
    pass

def getStart():
    root.title('TableMaker')
    setGeometry(root)
    root.configure(bg='#ffcccc')
    TextFrame = tk.Frame(master=root, relief=tk.FLAT,
                      borderwidth=50, bg='#ffccff')
    helloText = tk.Label(master=TextFrame, bg='#ffccff',
                         text='Hi, this is a simple TableMaker app', font=('Forte', 25))
    helloText.pack()
    TextFrame.pack(fill=tk.BOTH, side=tk.TOP)
    EventFrame = tk.Frame(master=root, relief=tk.FLAT, bg='#ff8080', borderwidth=20)
    tk.Label(master=EventFrame, relief=tk.FLAT, text='Press any button to start', bg='#ff8080', fg='#000099',
                                width=30, font=('Forte', 25)).pack()
    EventFrame.pack(fill = tk.BOTH, side = tk.TOP)
    ImageFrame = tk.Frame(master=root, relief=tk.FLAT,
                          borderwidth=70, bg='#ffcccc')
    img = ImageTk.PhotoImage(Image.open('heart22.png'))
    tk.Label(master = ImageFrame, image = img ).pack()
    ImageFrame.pack(fill=tk.BOTH, side=tk.TOP)

    root.bind('<Key>', lambda a: createtest(EventFrame, TextFrame, ImageFrame))
    root.mainloop()


def createtest(EventFrame, TextFrame , ImageFrame):
    EventFrame.destroy()
    TextFrame.destroy()
    ImageFrame.destroy()
    root.bind('Key', setFrames())
    root.unbind('<Key>')




def throwToTableMenu():
    pass


getStart()
