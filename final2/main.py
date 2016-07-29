import math, random, tkinter, time, drawing, physics, gr, rotate

def main1():
    print("Main Start")
    g = gr.Graph()
    g.readVertexFile('vertices.txt')
    g.readEdgeFile('only_with_pairs.txt')
    print(len(g.V))
    drawing.setID(g)  # вставь граф
    physics.setConstans(g)

    while True:
        physics.physStep(g)
        physics.physStep(g)
        drawing.drawing(g) #вставь граф
        drawing.canvas.update()
        rotate.rotate(g, [1, 2, 3], 0.001)
        #time.sleep(1/60)

def main2():
    print("Main Start")
    g1 = gr.Graph()
    g2 = gr.Graph()
    g1.createCircle(2)
    g2.createCircle(2)
    g3 =  gr.multiply(g1, g2)
    g4 =  gr.multiply(g1, g3)
    g = gr.multiply(g1, g3)

    print(len(g.V))
    drawing.setID(g)  # вставь граф
    physics.setConstans(g)

    while True:
        physics.physStep(g)
        physics.physStep(g)
        drawing.drawing(g) #вставь граф
        drawing.canvas.update()
        rotate.rotate(g, [1, 2, 3], 0.001)
        time.sleep(1/60)

def main():
    main2()

if __name__ == '__main__':
    main()
