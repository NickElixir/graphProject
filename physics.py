import time, gr, math, random
d = 0.9

def setConstans (g:gr.Graph):
    for i in g.V:
        i.x = random.uniform(-1, 1)
        i.y = random.uniform(-1, 1)
        i.z = random.uniform(-1, 1)
def physStep(g:gr.Graph):
    for i in g.V:
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
    for i in g.E:
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
        i.v1.vx += ax
        i.v2.vx -= ax
        i.v1.vy += ay
        i.v2.vy -= ay
        i.v1.vz += az
        i.v2.vz -= az
    for i in g.V:
        i.vx *= d
        i.vy *= d
        i.vz *= d
        i.x += i.vx
        i.y += i.vy
        i.z += i.vz
