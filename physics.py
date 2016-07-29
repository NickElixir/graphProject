from tkinter import*
import time, gr
import constans
import math, random
d = constans.dc
k = constans.kc
l = constans.lc
q = constans.qc

def setConstans(g:gr.Graph):#координаты каждой вершины
    for i in g.V:
        i.x = random.uniform(-1, 1)
        i.y = random.uniform(-1, 1)
        i.z = random.uniform(-1, 1)
        i.q = q
    for i in g.E:
        i.k = k
        i.l = l

def physStep(g:gr.Graph):

    for i in g.V:#сила кулона
        x1 = i.x
        y1 = i.y
        z1 = i.z
        q1 = i.q
        for j in g.V:
            if i != j:
                x2 = j.x
                y2 = j.y
                z2 = j.z
                q2 = j.q
                r = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2  + (z1 - z2)**2)
                a = q1*q2 / r

                ax = (x1 - x2) / math.sqrt(r)*a
                ay = (y1 - y2) / math.sqrt(r)*a
                az = (z1 - z2) / math.sqrt(r)*a
                i.vx += ax
                i.vy += ay
                i.vz += az

    for i in g.E:#сила гука
        x1 = i.v1.x
        x2 = i.v2.x
        y1 = i.v1.y
        y2 = i.v2.y
        z1 = i.v1.z
        z2 = i.v2.z
        k = i.k
        l = i.l
        r = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        a = k * (l - r)
        ax = (x1 - x2) / math.sqrt(r) * a
        ay = (y1 - y2) / math.sqrt(r) * a
        az = (z1 - z2) / math.sqrt(r) * a
        #Начало особого места
        i.v1.vx += ax
        i.v2.vx -= ax
        i.v1.vy += ay
        i.v2.vy -= ay
        i.v1.vz += az
        i.v2.vz -= az
        #Конец особого места
    for i in g.V:#итоговое замедление и изменение координат
        #u = d
        u = d/((i.vx**2 + i.vy**2+i.vz**2)+1)**(1/8)
        if g.degree(i) != 0:
            u /= g.degree(i)

        i.vx *= u
        i.vy *= u
        i.vz *= u
        i.x += i.vx
        i.y += i.vy
        i.z += i.vz
def main():
    g = gr.Graph()
    g.randomTree(6)
    setConstans(g)
    physStep(g)
if __name__=="__main__":
    main()