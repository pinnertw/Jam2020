#!/bin/python3
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    size = int(input())
    mat = []
    for j in range(size):
        mat.append([int(s) for s in input().split(' ')])
    trace = 0

    row = 0
    column = 0

    for j in range(size):
        a = set()
        aflag = True
        b = set()
        bflag = True
        trace += mat[j][j]
        for k in range(size):
            if mat[j][k] in a and aflag:
                row += 1
                aflag = False
            else:
                a.add(mat[j][k])
            if mat[k][j] in b and bflag:
                column += 1
                bflag = False
            else:
                b.add(mat[k][j])

    print("Case #{}: {} {} {}".format(i, trace, row, column))
  # check out .format's specification for more formatting options
