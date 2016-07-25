import tkinter
class Vertex:
    def __init__(self, x=0.0, y=0.0, z=0.0, color='white', rad=5, q=1.0, vx=0.0, vy=0.0, vz=0.0):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.color = 'white'
        self.rad = 5
        self.q = 1.0
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0
class Edge:
    def __init__(self, v1, v2, l=0.0, k=0.0, color='white'):
        self.v1 = v1
        self.v2 = v2
        self.l = 0.0
        self.k = 0.0
        self.color = 'white'
class Graph:
    def __init__(self, V=[], E=[]):
        self.V = V
        self.E = E
    def addVertex(self):
        v = Vertex()
        V.append(v)
    def addEdge(self, v1, v2):
        e = Edge(v1, v2)
        e2 = Edge(v2, v1)
        if V.count(v1) < 1 or V.count(v2) < 1 or v1 == v2:
            print('Error: Incorrect args')
            return -1
        elif E.count(e) > 0 or E.count(e2) > 0:
            print('Error: Incorrect args')
            return -1
        else:
            E.append(e)
            return 0
    def delVertex(self, v):
        countV = V.count(v)
        if count == 0:
            print('Error: No such vertex')
            return -1
        else:
            V.pop(V.index(v))
            return 0
    def delEdge(self, v1, v2):
        e = Edge(v1, v2)
        e2 = Edge(v2, v1)
        if E.count(e) < 1 or E.count(e2) < 1:
            print('Error: Incorrect args')
            return -1 
        else:
            E.pop(E.index(e))
            return 0            
V = []
E = []
