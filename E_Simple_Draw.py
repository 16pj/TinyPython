from Tkinter import *
import subprocess
import os
import io
from PIL import Image


x_1, y_1 = 0, 0


##############################################################################

def exitTool():
    root.quit()

def saveFile():
    canvas.update()
    ps = canvas.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('/tmp/test.jpg')


############################################################################

def getStart(event):
    global x_1, y_1
    x_1, y_1 = event.x, event.y

def drawTool(event):
    global x_1, y_1
    canvas.create_line((x_1, y_1, event.x, event.y),fill=Clr,width=thck)
    x_1, y_1 = event.x, event.y

def Nothing(event):
    print("")

def Unbind():
    canvas.bind("<Button-1>", Nothing)
    canvas.bind("<B1-Motion>", Nothing)
    canvas.bind("<ButtonRelease-1>", Nothing)

def Pencil():
     Unbind()
     canvas.bind("<Button-1>", getStart)
     canvas.bind("<B1-Motion>", drawTool)

def drawRectangle(event):
    global x_1, y_1
    canvas.create_rectangle(x_1, y_1, event.x, event.y,fill=Clr,width=thck)

def Rectangle():
    Unbind()
    canvas.bind("<Button-1>", getStart)
    canvas.bind("<ButtonRelease-1>", drawRectangle)

def drawCircle(event):
    global x_1, y_1
    canvas.create_oval(x_1, y_1, event.x, event.y,fill=Clr,width=thck)

def Circle():
    Unbind()
    canvas.bind("<Button-1>", getStart)
    canvas.bind("<ButtonRelease-1>", drawCircle)

def drawLine(event):
    global x_1, y_1
    canvas.create_line(x_1, y_1, event.x, event.y,fill=Clr,width=thck)

def Text_input():
    Unbind()
    enter.pack(side=TOP)
    #submitButton.pack(side=TOP)
    canvas.bind("<Button-1>", Text)

def Text(event):
    global x_1, y_1
    x_1,  y_1 = event.x,  event.y
    s= enter.get()
    canvas.create_text(x_1, y_1, text = s,fill=Clr)

def Line():
    Unbind()
    canvas.bind("<Button-1>", getStart)
    canvas.bind("<ButtonRelease-1>", drawLine)

def eraseTool(event):
    x_1, y_1 = event.x, event.y
    canvas.create_rectangle(event.x-thckera, event.y-thckera,event.x+thckera,event.y+thckera,outline="white", fill="white")

def Eraser():
    Unbind()
    canvas.bind("<B1-Motion>",eraseTool)

def Clear():
    global thck, thckera, Clr
    canvas.delete(ALL)
    thck = 1
    thckera = 10
    Clr = "black"

def colorRed():
    global Clr
    Clr = "red"

def colorBlack():
    global Clr
    Clr = "black"

def colorGreen():
    global Clr
    Clr = "green"

def colorBlue():
    global Clr
    Clr = "blue"

def thck1():
    global thck, thckera
    thck = 1
    thckera = 10
def thck3():
    global thck, thckera
    thck = 3
    thckera = 15
def Thck5():
    global thck, thckera
    thck = 5
    thckera = 20

#################################################################################3


root = Tk()



toolFrame = Frame(root)
toolFrame.pack(side=LEFT)
canvasFrame = Frame(root)
canvasFrame.pack()

enter = Entry(canvasFrame)
#submitButton = Button(canvasFrame, text="Enter Text", command=Text)

Clr = "black"
thck = 1
thckera = 10
canvas = Canvas(canvasFrame, bg ='white')
canvas.grid(column=0, row=0, sticky=(N, W, E, S),)
canvas.pack()
clearButton = Button(toolFrame, text="Clear", command = Clear)
clearButton.pack(side=TOP, padx = 5, pady =10)
pencilButton = Button(toolFrame, text="Pencil", command = Pencil)
pencilButton.pack(side = TOP, padx = 5, pady =10)
eraserButton = Button(toolFrame, text = "Eraser", command = Eraser)
eraserButton.pack(side=TOP, padx = 5, pady =10)
rectangleButton = Button(toolFrame, text = "Rectangle", command = Rectangle)
rectangleButton.pack(side=TOP, padx = 5, pady =10)
circleButton = Button(toolFrame, text = "Circle", command = Circle)
circleButton.pack(side=TOP, padx = 5, pady =10)
lineButton = Button(toolFrame, text = "Line", command = Line)
lineButton.pack(side=TOP, padx = 5, pady =10)
textButton = Button(toolFrame, text = "Text", command = Text_input)
textButton.pack(side=TOP, padx = 5, pady =10)


menu = Menu(root)
root.config(menu = menu)

fileMenu = Menu (menu)
menu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label="Save", command = saveFile)
fileMenu.add_command(label="Exit", command = exitTool)

subMenu = Menu(menu)
menu.add_cascade(label = "Colours", menu = subMenu)
subMenu.add_command(label="RED", command = colorRed)
subMenu.add_command(label="BLUE", command = colorBlue)
subMenu.add_command(label="GREEN", command = colorGreen)
subMenu.add_command(label="BLACK", command = colorBlack)

editMenu = Menu (menu)
menu.add_cascade(label = "Thickness", menu = editMenu)
editMenu.add_command(label="Thickness 1", command = thck1)
editMenu.add_command(label="Thickness 3", command = thck3)
editMenu.add_command(label="Thickness 5", command = Thck5)

root.mainloop()


