def ask(j):
    print(j, flush=True)
    tour += 1

if __name__ == '__main__':
    t, B = [int(x) for x in input().split(' ')]
    if B == 10:
        ma = 10
    elif B == 20:
        ma = 40
    else:
        ma = 150
    # By case
    for i in range(1, t + 1):
        res = [-1] * B
        index_00 = None
        index_01 = None
        index = 0
        tour = 1
        while index < B // 2 + 1:
            if index_00 is None and index_01 is None:
                ask(index + 1)
                res[index] = int(input())
                ask(B - index)
                res[-1-index] = int(input())
                if res[index] == res[-1-index]:
                    index_00 = index + 1
                else:
                    index_01 = index + 1
            elif 

        res = ''.join(res)
        print(res, flush=True)
        k = input()
        if k == "N":
            break
