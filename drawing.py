import gr
import tkinter
import math
import random

width=1280
height=700
scale=1
changeScale=0.001
weedMod = 0 # чтобы включить мод поменяй значение на True

root = tkinter.Tk()
canvas=tkinter.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

def centreX(x):
    return x + canvas.winfo_reqwidth()/2

def centreY(y):
    return y + canvas.winfo_reqheight()/2

def colorToList(colorStr):
    redStr = str(colorStr[1] + colorStr[2])
    greenStr = str(colorStr[3] + colorStr[4])
    blueStr = str(colorStr[5] + colorStr[6])
    redInt = eval("0x" + redStr)
    greenInt = eval("0x" + greenStr)
    blueInt = eval("0x" + blueStr)
    colorList = [redInt, greenInt, blueInt]
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
        return -1

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

def mixedColorLine(e: gr.Edge):
    if (e.v1.color == e.v2.color):
        return e.v1.color
    else:
        colorlistE = []
        colorListV1 = colorToList(e.v1.color)
        redIntV1 = colorListV1[0]
        greenIntV1 = colorListV1[1]
        blueIntV1 = colorListV1[2]

        colorListV2 = colorToList(e.v2.color)
        redIntV2 = colorListV2[0]
        greenIntV2 = colorListV2[1]
        blueIntV2 = colorListV2[2]

        if (redIntV1 == redIntV2):
            colorlistE.append(redIntV1)
        else:
            redIntE = (redIntV1 + redIntV2) / 2
            colorlistE.append(redIntE)

        if (greenIntV1 == greenIntV2):
            colorlistE.append(greenIntV1)
        else:
            greenIntE = (greenIntV1 + greenIntV2) / 2
            colorlistE.append(greenIntE)

        if (blueIntV1 == blueIntV2):
            colorlistE.append(blueIntV1)
        else:
            blueIntE = (blueIntV1 + blueIntV2) / 2
            colorlistE.append(blueIntE)

        return listToColor(colorlistE)

def changeRad(p:gr.Vertex):
    rad=(math.atan(p.z / 200)/(math.pi/2)*p.rad)+p.rad
    if (rad < 3):
        rad = 3
    elif (rad>12):
        rad=12
    return rad

def colorRandom(v: gr.Vertex):
    colorList = [0, 0, 0]

    redInt = random.randint(0, 255)
    greenInt = random.randint(0, 255)
    blueInt = random.randint(0, 255)

    colorList[0] = redInt
    colorList[1] = greenInt
    colorList[2] = blueInt
    return listToColor(colorList)


def colorTransition(v: gr.Vertex):
    colorList = colorToList(v.color)
    redInt = colorList[0]
    greenInt = colorList[1]
    blueInt = colorList[2]

    if (redInt + v.vr > 255 or redInt + v.vr < 0):
        v.vr = -v.vr
    if (greenInt + v.vg > 255 or greenInt + v.vg < 0):
        v.vg = -v.vg
    if (blueInt + v.vb > 255 or blueInt + v.vb < 0):
        v.vb = -v.vb
    redInt = redInt + v.vr
    greenInt = greenInt + v.vg
    blueInt = blueInt + v.vb

    colorList[0] = redInt
    colorList[1] = greenInt
    colorList[2] = blueInt

    v.color = listToColor(colorList)
    return v.color

def setPointID(graph:gr.Graph):
    for i in graph.V:
        i.id = canvas.create_oval(centreX(i.x) - i.rad, centreY(i.y) - i.rad,
                                 centreX(i.x) + i.rad, centreY(i.y) + i.rad,
                                 fill = colorRandom(i))
        i.vr = random.randint(1, 10)
        i.vg = random.randint(1, 10)
        i.vb = random.randint(1, 10)

def setLineID(graph:gr.Graph):
    for i in graph.E:
        i.color = mixedColorLine(i)
        i.id = canvas.create_line(i.v1.x, i.v1.y, i.v2.x, i.v2.y, fill=colorRandom(i))

def setID(graph:gr.Graph):
    setLineID(graph)
    setPointID(graph)

def updatePoints(graph:gr.Graph):
    for i in graph.V:
        rad = changeRad(i)
        canvas.coords(i.id, centreX(i.x*scale-rad), centreY(i.y*scale-rad),
                      centreX(i.x*scale+rad), centreY(i.y*scale+rad))
        if weedMod:
            colorTransition(i)
        canvas.itemconfig(i.id, fill=blackoutPoint(i))

def updateLines(graph:gr.Graph):
    for i in graph.E:
        canvas.coords(i.id, centreX(i.v1.x*scale), centreY(i.v1.y*scale),
                      centreX(i.v2.x*scale), centreY(i.v2.y*scale))

        if weedMod:
            i.color = mixedColorLine(i)
        canvas.itemconfig(i.id, fill=blackoutLine(i))

def checkPoint(graph:gr.Graph):
    global  scale
    for i in graph.V:
        if (centreX(i.x*scale)>width-10
            or centreY(i.y*scale)>height-10
            or centreX(i.x*scale)<10
            or centreY(i.y*scale)<10):
            scale=scale-changeScale

def drawing(graph:gr.Graph):
    updateLines(graph)
    updatePoints(graph)
    checkPoint(graph)
