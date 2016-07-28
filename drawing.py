import gr
import tkinter
import math
width=1280
height=700
scale=1

root = tkinter.Tk()
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

def changeRad(p:gr.Vertex):
    rad=(math.atan(p.z / 200)/(math.pi/2)*p.rad)+p.rad
    if (rad < 3):
        rad = 3
    elif (rad>12):
        rad=12
    return rad

def colorToList(colorStr):
    redStr = str(colorStr[1] + colorStr[2])
    greenStr = str(colorStr[3] + colorStr[4])
    blueStr = str(colorStr[5] + colorStr[6])
    redInt = eval("0x" + redStr)
    greenInt = eval("0x" + greenStr)
    blueInt = eval("0x" + blueStr)
    colorList=[redInt, greenInt, blueInt]
    return colorList

def listToColor(colorList):

    redInt=colorList[0]
    greenInt=colorList[1]
    blueInt=colorList[2]

    redStr=str(hex(int(redInt)))
    greenStr=str(hex(int(greenInt)))
    blueStr=str(hex(int(blueInt)))

    if (len(redStr) == 3):
        redStr = '0' + redStr[2]
    elif (len(redStr) == 4):
        redStr = redStr[2] + redStr[3]
    else:
        return -1;

    if (len(greenStr) == 3):
        greenStr = "0" + greenStr[2]
    elif (len(greenStr) == 4):
        greenStr = greenStr[2] + greenStr[3]
    else:
        return -1

    if (len(blueStr) == 3):
        blueStr = "0" + blueStr[2]
    elif(len(blueStr) == 4):
        blueStr = blueStr[2] +blueStr[3]

    color="#" + redStr + greenStr + blueStr
    return color

def blackoutPoint(v:gr.Vertex):
        colorList = colorToList(v.color)
        redInt = colorList[0]
        greenInt = colorList[1]
        blueInt = colorList[2]
        atanGraphic=(math.atan(v.z / 10)/math.pi/2)
        redInt=atanGraphic*redInt/2+redInt/2
        greenInt=atanGraphic*greenInt/2+greenInt/2
        blueInt=atanGraphic*blueInt/2+blueInt/2
        colorList[0]=redInt
        colorList[1]=greenInt
        colorList[2]=blueInt
        return listToColor(colorList)

def blackoutLine(e:gr.Edge):
    colorList = colorToList(e.color)
    redInt = colorList[0]
    greenInt = colorList[1]
    blueInt = colorList[2]
    atanGraphic = (math.atan((e.v1.z + e.v2.z)/2 / 10) / math.pi / 2)
    redInt = atanGraphic * redInt / 2 + redInt / 2
    greenInt = atanGraphic * greenInt / 2 + greenInt / 2
    blueInt = atanGraphic * blueInt / 2 + blueInt / 2
    colorList[0] = redInt
    colorList[1] = greenInt
    colorList[2] = blueInt
    return listToColor(colorList)

def updatePoints(graph:gr.Graph):
    for i in graph.V:
        rad = changeRad(i)
        canvas.coords(i.id, centreX(i.x*scale-rad), centreY(i.y*scale-rad),
                      centreX(i.x*scale+rad), centreY(i.y*scale+rad))
        canvas.itemconfig(i.id, fill=blackoutPoint(i))
def updateLines(graph:gr.Graph):
    for i in graph.E:
        canvas.coords(i.id, centreX(i.v1.x*scale), centreY(i.v1.y*scale),
                      centreX(i.v2.x*scale), centreY(i.v2.y*scale))
        canvas.itemconfig(i.id, fill=blackoutLine(i))
def checkPoint(graph:gr.Graph):
    global  scale
    for i in graph.V:
        if (centreX(i.x*scale)>width-10
            or centreY(i.y*scale)>height-10
            or centreX(i.x*scale)<10
            or centreY(i.y*scale)<10):
            scale=scale-0.001

def drawing(graph:gr.Graph):
    updateLines(graph)
    updatePoints(graph)
    checkPoint(graph)
