import time

class obj():
    def __init__(self):
        self.x = 0
        self.y = 0

"""
Check the 3x3 grid around a point, the difference in the multiple of the x and y must be one if its adjacent
e.g. 
.Y.
.X.
...
X coord = (2,2)
Y coord = (2,3)
(Hx-Tx) * (Hy-Ty) = (2-2) * (2-3) = 0

..Y
.X.
...
X coord = (2,2)
Y coord = (3,3)
(Hx-Tx) * (Hy-Ty) = (2-3) * (2-3) = -1

...
.X.
Y..
X coord = (2,2)
Y coord = (1,1)
(Hx-Tx) * (Hy-Ty) = (2-1) * (2-1) = 1

...
.X.
..Y
X coord = (2,2)
Y coord = (3,1)
(Hx-Tx) * (Hy-Ty) = (2-3) * (2-1) = -1

Y..
.X.
...
X coord = (2,2)
Y coord = (1,3)
(Hx-Tx) * (Hy-Ty) = (2-1) * (2-3) = -1
"""


def check_adjacent(xs, ys, check):
    if check not in [0, 1, -1]:
        return False
    if abs(xs) > 1 or abs(ys) > 1:
        return False
    return True

def move_if_not_adjacent(head, tail):
    xs = head.x - tail.x
    ys = head.y - tail.y
    check = xs * ys
    if check_adjacent(xs, ys, check):
        return
    ## Move up.
    #"""
    #ooo
    #XXX
    #.Y.
    # 
    #If we move X up and it is suddenly not adjacent, it can only move to 3 locations
    #Which is immediately above, top diagonal left, top diagonal right.
    #"""

    if ys > 0:
        # Has moved from directly up
        if check == 0:
            tail.y += 1
        else: # Has moved diagonally
            if xs > 0: # Has moved frmo top right
                tail.x += 1
                tail.y += 1
            else: # Has moved from top left
                tail.x -= 1
                tail.y += 1
    # Move down.
    #"""
    #.Y.
    #XXX
    #ooo
    #If we move X down, then from tails perspective it can only have gone to 3 locations
    #    - immediately down
    #    - bottom left
    #    - bottom right
    #"""
    elif ys < 0:
        if check == 0: # Has moved from directly down
            tail.y -= 1
        else: # Has moved diagonally
            if xs > 0: # Has moved frmo bottom right
                tail.x += 1
                tail.y -= 1
            else: # Has moved from bottom left
                tail.x -= 1
                tail.y -= 1
    # Move left.
    #"""
    #oX.
    #oXY
    #oX.
    #If we move X left, then from tails perspective it can only have gone to 3 locations
    #    - immediately left
    #    - top left
    #    - bottom left
    #"""
    elif xs < 0:
        if check == 0: # Has moved from directly left
            tail.x -= 1
        else:
            if ys > 0: #Has moved from top left
                tail.x -= 1
                tail.y += 1
            else: #Has moved from bottom left
                tail.x -= 1
                tail.y -= 1
    # Move right.
    #"""
    #.Xo
    #YXo
    #.Xo
    #If we move X right, then from tails perspective it can only have gone to 3 locations
    #    - immediately right
    #    - top right
    #    - bottom right
    #"""
    else:
        if check == 0: #Has moved from directly right
            tail.x += 1
        else:
            if ys > 0: #Has moved from top right
                tail.y += 1
                tail.x += 1
            else: #Has moved from bottom right
                tail.y -= 1
                tail.x += 1

def move_head(head, direction):
    # Move up.
    if direction == "U":
        head.y += 1
    
    # Move down.
    elif direction == "D":
        head.y -= 1
    
    # Move left.
    elif direction == "L":
        head.x -= 1
    
    # Move right.
    else:
        head.x += 1

def part1(f):
    head = obj()
    tail = obj()
    seen = set()
    for line in f:
        instructions = line.strip().split()
        for _ in range(int(instructions[1])):
            move_head(head, instructions[0])
            move_if_not_adjacent(head, tail)
            if (tail.x, tail.y) not in seen:
                seen.add((tail.x, tail.y))
    print(len(seen))

def part2(f):
    head = obj()
    tails = []
    for _ in range(9):
        a = obj()
        tails.append(a)
    seen = set()
    for line in f:
        instructions = line.strip().split()
        for _ in range(int(instructions[1])):
            move_head(head, instructions[0])
            move_if_not_adjacent(head, tails[0])
            for i in range(0, len(tails) - 1):
                move_if_not_adjacent(tails[i], tails[i + 1])
                #print(tails[1].x, tails[1].y)
            if (tails[8].x, tails[8].y) not in seen:
                seen.add((tails[8].x, tails[8].y))
    print(len(seen))


with open("input.txt", "r") as f:
    part1(f)
    f.seek(0, 0)
    part2(f)
