
def f(n):
    if n == 1:
        return[['-']*3]
    m = [l+[' ']*3+l for l in f(n-1)]
    w = len(m[0])
    y = len(m)//2
    x = w//4-1

    m= map(list, m + [' '*w,' '*x+'-'*(w-x-x)+' '*x,' '*w] + m)
    m = list(m)
    for i in range(y,len(m)-y):
        m[i][x] = m[i][w + ~x] ='|+'[m[i][x] > ' ']
    return m


for n in 1,2,3,4:
 print(n)
 R=f(n)
 for l in R:print(''.join(l))
 print()


# #-----------------------------------------------------------------------
# # htree.py
# #-----------------------------------------------------------------------
#
# import stddraw
# import sys
#
# #-----------------------------------------------------------------------
#
# # Draw to standard draw a level n H-tree centered at (x. y) with lines
# # of length lineLength.
#
# def drawLine(x1, y1, x2, y2):
#   print(x1, y1, x2, y2)
#
# def drawHTree(x, y, lineLength, n):
#     if n == 0:
#         return
#     x0 = x - lineLength/2
#     x1 = x + lineLength/2
#     y0 = y - lineLength/2
#     y1 = y + lineLength/2
#
#     drawLine(x0, y, x1, y)
#     drawLine(x0, y0, x0, y1)
#     drawLine(x1, y0, x1, y1)
#
#     drawHTree(x0, y0, lineLength/2, n-1)
#     drawHTree(x0, y1, lineLength/2, n-1)
#     drawHTree(x1, y0, lineLength/2, n-1)
#     drawHTree(x1, y1, lineLength/2, n-1)
#
# print(drawHTree(0.5,0.5,0.5,4))
# #-----------------------------------------------------------------------
#
# # Accept integer n as a command-line argument. Draw a level n H-tree
# # centered at (.5, .5) with lines of length .5.
#
# def main():
#     n = int(sys.argv[1])
#     stddraw.setPenRadius(0.0)
#     draw(n, .5, .5, .5)
#     stddraw.show()
#
# if __name__ == '__main__':
#     main()
#
# #-----------------------------------------------------------------------
