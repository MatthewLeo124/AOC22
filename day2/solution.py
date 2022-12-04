#P1: A: Rock, B: Paper, C: Scissors
#P2: X: Rock, Y: Paper, Z: Scissors
#Score: 1 -> Rock; 2 -> Paper; 3 -> Scissors
#Score: Loss -> 0, Draw -> 3, Win -> 6

p1_s = 0
p2_s = 0
p1_transform = {
    "X" : 1, #Rock      A
    "Y" : 2, #Paper     B
    "Z" : 3  #Scissors  C
}


#Rock > scissors, even with rock
#Scissors > Paper, = Scissors
#Paper > Rock, = Paper

def p1(line):
    f, s = line.split()
    s = p1_transform[s]
    if f == "A":
        if s == 1:
            return 3 + s
        if s == 2:
            return 6 + s
        else:
            return s
    if f == "B":
        if s == 1:
            return s
        if s == 2:
            return 3 + s
        if s == 3:
            return 6 + s
    if f == "C":
        if s == 1:
            return 6 + s
        if s == 2:
            return s
        if s == 3:
            return 3 + s

#X = Lose
#Y = Draw
#Z = Win

def p2(line):
    f, s = line.split()
    if s == "X":
        if f == "A":
            return 3
        if f == "B":
            return 1
        if f == "C":
            return 2
    if s == "Y":
        if f == "A":
            return 3 + 1
        if f == "B":
            return 3 + 2
        if f == "C":
            return 3 + 3
    if s == "Z":
        if f == "A":
            return 6 + 2
        if f == "B":
            return 6 + 3
        if f == "C":
            return 6 + 1
    


with open("input.txt", "r") as f:
    p1_s = sum(map(p1, f))

with open("input.txt", "r") as f:
    p2_s = sum(map(p2, f))

print(p1_s)
print(p2_s)