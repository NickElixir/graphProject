import random
import constants

colorVertexDefault = constants.colorVertexDefault
colorEdgeDefault = constants.colorEdgeDefault
radDefault = constants.radDefault

class Vertex:
    def __init__(self, x=0.0, y=0.0, z=0.0, color=colorVertexDefault, colorCode=0, rad=radDefault, q=1.0,
                 vx=0.0, vy=0.0, vz=0.0, vr=0.0, vg=0.0, vb=0.0):
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
    def __init__(self, v1: Vertex, v2: Vertex, l=0.0, k=0.0, color=colorEdgeDefault):
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
        if self.V.count(v1) < 1 or self.V.count(v2) < 1 or v1 == v2:
            print('Error: Incorrect args')
            return -1
        else:
            for i in self.E:
                if i.v1 == v1 and i.v2 == v2:
                    print('Error: Incorrect args')
                    return -1
                if i.v1 == v1 and i.v2 == v1:
                    print('Error: Incorrect args')
                    return -1

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

    def createChain(self, n: int):
        self.createEmpty(n)
        for i in range(1, n):
            self.addEdge(self.V[i], self.V[i-1])

    def createCircle(self, n:int):
        self.createChain(n)
        self.addEdge(self.V[n-1], self.V[0])


    def randomTree(self, n: int):
        self.clearAll()
        self.addVertex()
        count = 0
        for i in range(n-1):
            self.addVertex()
            count += 1
            k = random.randrange(0, count)
            self.addEdge(self.V[count], self.V[k])

    def randomGraph(self, n:int, p:float):
        self.createEmpty(n)
        for i in range(1, n):
            for j in range(0, i):
                a = random.uniform(0, 1)
                #print(a)
                if a < p:
                    self.addEdge(self.V[i], self.V[j])

    def readVertexFile(self, fileName: str):
        stream = open(fileName, 'r')
        n = stream.readline()
        self.createEmpty(int(n))
        count = 0
        for line in stream:
            color = int(line)
            self.V[count].colorCode = color
            if color == 1:
                self.V[count].color = constants.colorVertexFileGirls
            elif color == 2:
                self.V[count].color = constants.colorVertexFileBoys
            elif color == 3:
                self.V[count].color = constants.colorVertexFilePro
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

    def exportToFile(self, filename):
        f = open(filename, 'wt')
        for e in self.E:
            f.write(str(self.V.index(e.v1)) + " " + str(self.V.index(e.v2)) + '\n')
        f.close()

    def exportDegrees(self, filename):
        f = open(filename, 'wt')
        Arr = [0] * len(self.V)
        for v in self.V:
            k = self.degree(v)
            Arr[k] += 1

        for i in Arr:
            f.write(str(i) + '\n')

        f.close()

def multiply(A: Graph, B: Graph):
    g = Graph()
    m = len(A.V)
    n = len(B.V)
    print(m, n)
    g.createEmpty(m*n)
    for e in B.E:
        i = B.V.index(e.v1)
        j = B.V.index(e.v2)
        for k in range(m):
            g.addEdge(g.V[n*k+i], g.V[n*k+j])
    for e in A.E:
        i = A.V.index(e.v1)
        j = A.V.index(e.v2)
        for k in range(n):
            g.addEdge(g.V[n*i+k], g.V[n*j+k])
    return g
