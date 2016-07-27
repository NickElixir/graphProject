import gr
import tkinter
import math

width=1000 #ширина окна
height=500 #высота окна
scale=1
indent=10

root = tkinter.Tk()                                                  #создание окна
canvas=tkinter.Canvas(root, width=width, height=height, bg="black")  #создание окна
canvas.pack()                                                        #создание окна

def centreX(x):
    return x + canvas.winfo_reqwidth()/2 #центровка по x

def centreY(y):
    return y + canvas.winfo_reqheight()/2 #центровка по y

def setPointID(graph:gr.Graph):
    for i in graph.V:
        i.id = canvas.create_oval(centreX(i.x) - i.rad, centreY(i.y) - i.rad, #создание вершин на полотне
                                 centreX(i.x) + i.rad, centreY(i.y) + i.rad,
                                 fill = i.color)

def setLineID(graph:gr.Graph):
    for i in graph.E:
        i.id = canvas.create_line(i.v1.x, i.v1.y, i.v2.x, i.v2.y, fill=i.color) #создание ребер на полотне

def setID(graph:gr.Graph): #создание и вершин, и ребер на полотне
    setLineID(graph)
    setPointID(graph)

def changeRad(p:gr.Vertex):
    rad=(math.atan(p.z)/(math.pi/2)*p.rad)+p.rad #изменение радиуса для псевдо-3D
    return rad

def updatePoints(graph:gr.Graph):
    for i in graph.V:
        rad = changeRad(i)
        canvas.coords(i.id, centreX((i.x-rad)*scale), centreY((i.y-rad)*scale), #обновление координат вершин на плоскости
                      centreX((i.x+rad)*scale), centreY((i.y+rad)*scale))
def updateLines(graph:gr.Graph):
    for i in graph.E:
        canvas.coords(i.id, centreX(i.v1.x*scale), centreY(i.v1.y*scale), #обновление координат ребер на плоскости
                      centreX(i.v2.x*scale), centreY(i.v2.y*scale))
def checkPoint(graph:gr.Graph):
    global  scale
    for i in graph.V:
        if (centreX(i.x*scale)>width-indent
            or centreY(i.y*scale)>height-indent #проверка координат вершин, чтобы они не ушли за видимую область
            or centreX(i.x*scale)<0+indent
            or centreY(i.y*scale)<0+indent):
            scale=scale-0.1

def drawing(graph:gr.Graph): #основная функция, которая рисует граф на плоскости
    updateLines(graph)
    updatePoints(graph)
    checkPoint(graph)

import time, random
setID(***) #вставь граф

print()
while True:
    drawing(***) #вставь граф
    canvas.update()
    time.sleep(0.016)



