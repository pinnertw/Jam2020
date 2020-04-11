#bin/python3

def num(r, k):
    r -= 1
    k -= 1
    den = 1
    nom = 1
    for i in range(1, k + 1):
        den *= (r - i + 1)
        nom *= i
    return den // nom

def add(ans, somme, r, k):
    ans.append(str(r) + " " + str(k))
    somme += num(r, k)
    return somme
DEBUG = True
t = int(input())  # read a line with a single integer
for nb_test in range(1, t + 1):
    nb = int(input())
    ans = []
    somme = 0
    r = 1
    k = 1
    for i in range(nb):
        somme = add(ans, somme, r, k)
    print("Case #{}:".format(nb_test))
    for i in ans:
        print(i)
    if DEBUG:
        print(somme)
        print(len(ans))
