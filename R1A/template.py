#bin/python3
t = int(input())  # read a line with a single integer
for nb_test in range(1, t + 1):
    nb_act = int(input())
    act = []
    for i in range(nb_act):
        act.append([int(s) for s in input().split(" ")] + [i])
    print("Case #{}: {}".format(nb_test, res))
