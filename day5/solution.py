"""
Input crate towers

[M] [H]         [N]                
[S] [W]         [F]     [W] [V]    
[J] [J]         [B]     [S] [B] [F]
[L] [F] [G]     [C]     [L] [N] [N]
[V] [Z] [D]     [P] [W] [G] [F] [Z]
[F] [D] [C] [S] [W] [M] [N] [H] [H]
[N] [N] [R] [B] [Z] [R] [T] [T] [M]
[R] [P] [W] [N] [M] [P] [R] [Q] [L]
 1   2   3   4   5   6   7   8   9 
"""

def part1(f):
    towers = []
    for _ in range(0, 9):
        towers.append(f.readline().strip().split(','))
    for line in f:
        line = line.strip().split()
        qty = int(line[1])
        sender = int(line[3]) - 1
        receiver = int(line[5]) - 1
        for _ in range(0, qty):
            towers[receiver].append(towers[sender].pop())

    s = ""
    for tower in towers:
        s += tower.pop()
    print(s)

def part2(f):
    towers = []
    for _ in range(0, 9):
        towers.append(f.readline().strip().split(','))
    for line in f:
        line = line.strip().split()
        qty = int(line[1])
        sender = int(line[3]) - 1
        receiver = int(line[5]) - 1
        temp = []
        for _ in range(0, qty):
            temp.append(towers[sender].pop())
        towers[receiver] += temp[::-1]

    s = ""
    for tower in towers:
        s += tower.pop()
    print(s)

with open("input.txt", "r") as f:
    part1(f)
    f.seek(0, 0)
    part2(f)