import tkinter
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
class Edge:
    def __init__(self, v1, v2, l=0.0, k=0.0, color='white'):
        self.v1 = v1
        self.v2 = v2
        self.l = l
        self.k = k
        self.color = color
class Graph:
    def __init__(self, V=[], E=[]):
        self.V = V
        self.E = E
    def addVertex(self):
        v = Vertex()
        self.V.append(v)
    def addEdge(self, v1, v2):
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
    def delVertex(self, v):
        countV = self.V.count(v)
        if count == 0:
            print('Error: No such vertex')
            return -1
        else:
            self.V.pop(V.index(v))
            return 0
    def delEdge(self, v1, v2):
        e = Edge(v1, v2)
        e2 = Edge(v2, v1)
        if self.E.count(e) < 1 or self.E.count(e2) < 1:
            print('Error: Incorrect args')
            return -1 
        else:
            self.E.pop(E.index(e))
            return 0
    def startProcess(self):
	root = tkinter.Tk()
	root.title('Graph')
	root.geometry('600x600')
	canvas = Canvas(root, width=600, height=600)
	canvas.place(x=0, y=0)
