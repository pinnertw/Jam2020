#bin/python3

def voisin(rl, cl):
    if compet_lev[rl][cl] == -1:
        return False
    left = 0
    right = 0
    top = 0
    bot = 0
    nb = 0
    # left
    for i in range(1, rl + 1):
        if compet_lev[rl - i][cl] != -1:
            left = compet_lev[rl-i][cl]
            nb += 1
            break
    for i in range(1, r - rl):
        if compet_lev[rl + i][cl] != -1:
            right = compet_lev[rl + i][cl]
            nb += 1
            break

    for i in range(1, cl + 1):
        if compet_lev[rl][cl - i] != -1:
            top = compet_lev[rl][cl - i]
            nb += 1
            break
    for i in range(1, c - cl):
        if compet_lev[rl][cl + i] != -1:
            bot = compet_lev[rl][cl + i]
            nb += 1
            break
    act = compet_lev[rl][cl]
    return nb > 0 and (act < (left + right + top + bot) / nb)

t = int(input())  # read a line with a single integer
for nb_test in range(1, t + 1):
    r, c = [int(s) for s in input().split(' ')]

    compet_lev = []
    for row in range(r):
        compet_row = [int(s) for s in input().split(' ')]
        compet_lev.append(compet_row)

    flag = True
    interest = 0
    while flag:
        flag = False
        loc = []
        interest_loc = 0
        for row in range(r):
            loc_row = []
            for col in range(c):
                if compet_lev[row][col] == -1:
                    loc_row.append(-1)
                elif voisin(row, col):
                    loc_row.append(-1)
                    flag = True
                    interest_loc += compet_lev[row][col]
                else:
                    loc_row.append(compet_lev[row][col])
                    interest_loc += compet_lev[row][col]
            loc.append(loc_row)
        interest += interest_loc
        compet_lev = loc

    print("Case #{}: {}".format(nb_test, interest))
