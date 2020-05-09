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
    columnsFrame = tk.Frame(master=root, relief=tk.FLAT,
                                borderwidth=50, bg='#b3d9ff')
    tk.Label(master=columnsFrame, bg='#b3d9ff',
            text='Enter the number of columns:', font=('Gothic', 15)).pack()
    columnsEntry = tk.Entry(master=columnsFrame, width=10)

    rowsFrame = tk.Frame(master=root, relief=tk.FLAT,
                        borderwidth=50, bg='#99ccff')
    tk.Label(master=rowsFrame, bg='#99ccff',
            text='Enter the number of rows:', font=('Gothic', 15)).pack()
    rowsEntry = tk.Entry(master=rowsFrame, width=10)
    columnsFrame.pack(fill=tk.BOTH, side=tk.TOP)
    columnsEntry.pack(side=tk.LEFT)
    rowsEntry.pack(side=tk.LEFT)
    rowsFrame.pack(fill=tk.BOTH, side=tk.TOP)
    butFrame = tk.Frame(master=root, relief=tk.FLAT,
                        borderwidth=50, bg='#ffb3d9')
    theNextButton = tk.Button(
        master=butFrame, relief=tk.RAISED, text='Next', bg='#ffcce6', height=5)
    butFrame.pack(side= tk.BOTTOM, fill = tk.BOTH)
    theNextButton.pack(side=tk.BOTTOM, fill=tk.BOTH)

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

getStart()
