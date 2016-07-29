import random


class Vertex:
    def __init__(self, x=0.0, y=0.0, z=0.0, color='#ffffff', colorCode=0, rad=5, q=1.0, vx=0.0, vy=0.0, vz=0.0, vr=0.0, vg=0.0, vb=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.colorCode = 0
        self.rad = rad
        self.q = q
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.id = 0.0
        self.vr = 0.0
        self.vg = 0.0
        self.vb = 0.0


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, l=0.0, k=0.0, color='white'):
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

    def addEdge(self, v1: Vertex, v2: Vertex):
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

    def delVertex(self, v: Vertex):
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

    def delEdge(self, v1: Vertex, v2: Vertex):
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

    def createEmpty(self, n: int):
        self.clearAll()
        for i in range(n):
            self.addVertex()

    def randomTree(self, n: int):
        self.clearAll()
        self.addVertex()
        count = 0
        for i in range(n-1):
            self.addVertex()
            count += 1
            k = random.randrange(0, count)
            self.addEdge(self.V[count], self.V[k])

    def readVertexFile(self, fileName: str):
        stream = open(fileName, 'r')
        n = stream.readline()
        self.createEmpty(int(n))
        count = 0
        for line in stream:
            color = int(line)
            self.V[count].colorCode = color
            if color == 1:
                self.V[count].color = '#ff0000'
            elif color == 2:
                self.V[count].color = '#0000ff'
            count += 1

    def readEdgeFile(self, fileName: str):
        stream = open(fileName, 'r')
        for line in stream:
            splitted = line.split()
            self.addEdge(self.V[int(splitted[0])-1], self.V[int(splitted[1])-1])

    def degree(self, v: Vertex):
        count = 0
        for e in self.E:
            if e.v1 == v or e.v2 == v:
                count += 1
        return count
