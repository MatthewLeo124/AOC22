def p2_1():
    top = []
    curr = 0
    with open("input.txt", "r") as f:
        for line in f:
            if line == "\n":
                top.append(curr)
                curr = 0
            else:
                curr += int(line)

    top.sort(reverse=True)
    p1 = top[0]
    p2 = sum(top[0:3])
    print(p1)
    print(p2)

def p2_2():
    t1 = 0
    t2 = 0
    t3 = 0
    c = 0
    with open("input.txt", "r") as f:
        for line in f:
            if line == "\n":
                if c > t1:
                    t3 = t2
                    t2 = t1
                    t1 = c
                elif c > t2:
                    t3 = t2
                    t2 = c
                elif c > t3:
                    t3 = c
                c = 0
            else:
                c += int(line)
    p1 = t1
    p2 = t1 + t2 + t3
    print(p1)
    print(p2)

p2_1()
#p2_2()
