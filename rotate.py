__author__ = 'Anton'

import math, gr

def rotateVector(Arr, vec, fi):
    cosFi = math.cos(fi)
    sinFi = math.sin(fi)
    x, y, z = vec
    xa, ya, za = Arr
    #     //Матрица поворота -
    # /*
    #  *   cosFi + (1-cosFi)xx;   (1-cosFi)xy - sinFi*z;     (1-cosFi)xz + sinFi*y;
    #  * (1-cosFi)yx + sinFi*z;     cosFi + (1-cosFi)yy;     (1-cosFi)yz - sinFi*x;
    #  * (1-cosFi)zx - sinFi*y;   (1-cosFi)zy + sinFi*x;       cosFi + (1-cosFi)zz;
    #  */

    A11 = cosFi + (1-cosFi)*x*x
    A12 = (1-cosFi)*x*y - sinFi*z
    A13 = (1-cosFi)*x*z + sinFi*y
    A21 = (1-cosFi)*y*x + sinFi*z
    A22 = cosFi + (1-cosFi)*y*y
    A23 = (1-cosFi)*y*z - sinFi*x
    A31 = (1-cosFi)*z*x - sinFi*y
    A32 = (1-cosFi)*z*y + sinFi*x
    A33 = cosFi + (1-cosFi)*z*z

    x = A11 * xa + A12 * ya + A13 * za
    y = A21 * xa + A22 * ya + A23 * za
    z = A31 * xa + A32 * ya + A33 * za
    return [x, y, z]

def rotateVertex(ver:gr.Vertex, vec, fi):
    ver.x, ver.y, ver.z = rotateVector([ver.x, ver.y, ver.z], vec, fi)
    ver.vx, ver.vy, ver.vz = rotateVector([ver.vx, ver.vy, ver.vz], vec, fi)

def rotate(g:gr.Graph, vec, fi):
    for v in g.V:
        rotateVertex(v, vec, fi)

def main():
    g = gr.Graph()
    g.randomTree(10)
    rotate(g, [1,0,0], 0.1)
    return 0

if __name__ == "__main__":
    main()