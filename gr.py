import random

class Vertex:
    def __init__(self, x=0.0, y=0.0, z=0.0, color='white', rad=5, q=1.0, vx=0.0, vy=0.0, vz=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.rad = rad
        self.q = q
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.id = 0.0
class Edge:
    def __init__(self, v1:Vertex, v2:Vertex, l=0.0, k=0.0, color='white'):
        self.v1 = v1
        self.v2 = v2
        self.l = l
        self.k = k
        self.color = color
        self.id = 0
class Graph:
    def __init__(self, V=[], E=[]):
        self.V = V
        self.E = E
    def addVertex(self):
        v = Vertex()
        self.V.append(v)
    def addEdge(self, v1:Vertex, v2:Vertex):
        e = Edge(v1, v2)
        e2 = Edge(v2, v1)
        if self.V.count(v1) < 1 or self.V.count(v2) < 1 or v1 == v2:
            print('Error: Incorrect args')
            return -1
        elif self.E.count(e) > 0 or self.E.count(e2) > 0:
            print('Error: Incorrect args')
            return -1
        else:
            self.E.append(e)
            return 0
    def delVertex(self, v:Vertex):
        countV = self.V.count(v)
        if countV == 0:
            print('Error: No such vertex')
            return -1
        else:
            for e in self.E:
                if v == e.v1 or v == e.v2:
                    self.delEdge(e.v1, e.v2)
                    self.V.remove(v)
            return 0
    def delEdge(self, v1:Vertex, v2:Vertex):
        allBad = True
        for e in self.E:
            if (e.v1 == v1 and e.v2 == v2) or (e.v1 == v2 and e.v2 == v1):
                self.E.remove(e)
                allBad = False
                return 0
        if allBad:
            print('Error: incorrect args')
            return -1
    def makeEmpty(self):
        self.E = []
    def clearAll(self):
        self.V = []
        self.makeEmpty()
    def createEmpty(self, n:int):
        self.clearAll()
        for i in range(n):
            self.addVertex()
    def randomTree(self, n:int):
        self.clearAll()
        self.addVertex()
        count = 1
        for i in range(n):
            self.addVertex()
            count += 1
            k = random.randrange(0, count-1)
            while count-1 == k:
                k = random.randrange(0, count-1)
            self.addEdge(self.V[count-1], self.V[k])
