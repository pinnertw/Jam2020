t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    string = input()
    res = []
    index = 0
    stack = []
    while index < len(string):
        num = int(string[index])
        if len(stack) == 0:
            res.append("(" * num + str(num))
            stack.append(num)
        elif num < stack[-1]:
            p = stack.pop()
            res.append(")" * p)
            stack.append(num)
        elif num > stack[-1]:
            loc = ""
            while len(stack) > 0 and num > stack[-1]:
                p = stack.pop()
                loc = "(" * p + str(p) + loc
            res.append(loc)
            stack.append(num)
        else:
            res.append(str(num))

        index += 1
    while len(stack) != 0:
        p = stack.pop()
        res.append("(" * p + str(p)  + ")" * p)

    res = "".join(res)
    print("Case #{}: {}".format(i, res))
