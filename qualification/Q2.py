#bin/python3
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
    nb_act = int(input())
    act = []
    for i in range(nb_act):
        act.append([int(s) for s in input().split(" ")] + [i])
    i = 0
    C_end = 0

    J_end = 0
    res = [' '] * nb_act
    act.sort(key = lambda x: x[0])
    while i < len(act) and res != "IMPOSSIBLE":
        if C_end <= act[i][0]:
            C_end = act[i][1]
            res[act[i][2]] = 'C'
        elif J_end <= act[i][0]:
            J_end = act[i][1]
            res[act[i][2]] = 'J'
        else:
            res = "IMPOSSIBLE"
        i += 1
    if res != "IMPOSSIBLE":
        res = ''.join(res)
    print("Case #{}: {}".format(j, res))
