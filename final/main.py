import math, random, tkinter, time, drawing, physics, gr, rotate

def main():
    print("Main Start")
    g = gr.Graph()
    g.readVertexFile('vertices.txt')
    g.readEdgeFile('only_with_pairs.txt')
    print(len(g.V))
    drawing.setID(g)  # вставь граф
    physics.setConstans(g)

    while True:
        physics.physStep(g)
        drawing.drawing(g) #вставь граф
        drawing.canvas.update()
        rotate.rotate(g, [1, 2, 3], 0.01)
        #time.sleep(1/60)



if __name__ == '__main__':
    main()
