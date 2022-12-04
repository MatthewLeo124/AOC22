top = []
curr = 0

with open("input.txt") as f:
    for line in f:
        if line == "\n":
            top.append(curr)
            curr = 0
        else:
            curr += int(line)

top.sort(reverse=True)
print(sum(top[0:3]))