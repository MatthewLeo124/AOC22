from itertools import islice
points = {}

def setup_points():
    alphabet = list(map(chr, range(97, 123)))   #a -> z
    alphabet += list(map(chr, range(65, 91)))   #A -> Z
    for i in range(1, 53):                      #Associate points: a: 1, A: 27 z:26, Z:52
        points[alphabet[i - 1]] = i

def p1(line):
    h = len(line) // 2
    h1, h2 = set(line[:h]), set(line[h:])
    return(points[h1.intersection(h2).pop()])

def p2(lines):
    elf1 = set(lines[0].strip())
    elf2 = set(lines[1].strip())
    elf3 = set(lines[2].strip())
    return points[elf1.intersection(elf2, elf3).pop()]

setup_points()
with open("input.txt", "r") as f:
    #print(sum(map(p1, f)))
    f.seek(0, 0)
    total = 0
    for t_lines in iter(lambda: tuple(islice(f, 3)), ()):
        total += p2(t_lines)
    print(total)
