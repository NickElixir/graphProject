import gr
import tkinter
import time

width=1000
height=500
scale=1

root = tkinter.Tk() #создание полотна
canvas=tkinter.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

def centreX(x):
    return x + canvas.winfo_reqwidth()/2

def centreY(y):
    return y + canvas.winfo_reqheight()/2

def setPointID(graph:gr.Graph):
    for i in graph.V:
        i.id = canvas.create_oval(centreX(i.x) - i.rad, centreY(i.y) - i.rad,
                                 centreX(i.x) + i.rad, centreY(i.y) + i.rad,
                                 fill = i.color)

def setLineID(graph:gr.Graph):
    for i in graph.E:
        i.id = canvas.create_line(i.v1.x, i.v1.y, i.v2.x, i.v2.y, fill=i.color)

def setID(graph:gr.Graph):
    setLineID(graph)
    setPointID(graph)

def updatePoints(graph:gr.Graph):
    for i in graph.V:
        canvas.coords(i.id, centreX((i.x-i.rad)*scale), centreY((i.y-i.rad)*scale),
                      centreX((i.x+i.rad)*scale), centreY((i.y+i.rad)*scale))
def updateLines(graph:gr.Graph):
    for i in graph.E:
        canvas.coords(i.id, centreX(i.v1.x*scale), centreY(i.v1.y*scale),
                      centreX(i.v2.x*scale), centreY(i.v2.y*scale))
def drawing(graph:gr.Graph):
    updateLines(graph)
    updatePoints(graph)

setID(____) #создание вершин и ребер
while True: #обновление вершин и ребер
    drawing(_____) #нужно вести граф
    canvas.update()
    time.sleep(0.016)


