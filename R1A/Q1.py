#bin/python3
def equal(str1, str2):
    print(str1, str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


t = int(input())  # read a line with a single integer
for nb_test in range(1, t + 1):
    nb_condition = int(input())
    conditions = []
    for i in range(nb_condition):
        s = input()
        conditions.append(s[1:])
    string = conditions[0]

    flag = True
    for i in conditions:
        if len(i) <= len(string) and string[-len(i):] == i:
            pass
        elif len(i) > len(string) and i[-len(string):] == string:
            string = i
        else:
            flag = False
    if flag:
        print("Case #{}: {}".format(nb_test, string))
    else:
        print("Case #{}: {}".format(nb_test, "*"))
