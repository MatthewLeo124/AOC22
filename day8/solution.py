def check_if_seen(data, x, y, n_col, n_row):
    x_before = False
    x_after = False
    y_before = False
    y_after = False
    point = data[x][y]

    #Check before 0 -> y
    for i in range(0, y):
        if data[x][i] >= point:
            x_before = True
            break

    #Check y -> n_col
    for i in range(y+1, n_col):
        if data[x][i] >= point:
            x_after = True
            break

    #Check 0 -> x
    for i in range(0, x):
        if data[i][y] >= point:
            y_before = True
            break

    #Check x -> n_row
    for i in range(x+1, n_row):
        if data[i][y] >= point:
            y_after = True
            break

    if x_before and x_after and y_before and y_after:
        return True
    return False

def find_viewing_distance(data, x, y, n_col, n_row):
    x_before = 0
    x_after = 0
    y_before = 0
    y_after = 0
    point = data[x][y]

    #Check before y -> 0
    for i in range(y-1, -1, -1):
        if data[x][i] >= point:
            x_before += 1
            break
        x_before += 1

    #Check y -> n_col
    for i in range(y+1, n_col):
        if data[x][i] >= point:
            x_after += 1
            break
        x_after += 1

    #Check 0 -> x
    for i in range(x-1, -1, -1):
        if data[i][y] >= point:
            y_before += 1
            break
        y_before += 1

    #Check x -> n_row
    for i in range(x+1, n_row):
        if data[i][y] >= point:
            y_after += 1
            break
        y_after += 1

    return x_before * x_after * y_before * y_after

def solution1(data):
    n_col = len(data[0])
    n_row = len(data)
    seen = []
    for i, row in enumerate(data):
        seen_row = []
        for j, _ in enumerate(row):
            if j == 0 or j == (n_col - 1):
                continue
            if i == 0 or i == (n_row - 1):
                continue
            if check_if_seen(data, i, j, n_col, n_row):
                seen_row.append(1)
            else:
                seen_row.append(0)
        if seen_row:
            seen.append(seen_row)

    total = 0
    for x in seen:
        for y in x:
            total += y
    total = (n_col * n_row) - total
    print(total)

def solution2(data):
    n_col = len(data[0])
    n_row = len(data)
    seen = []
    for i, row in enumerate(data):
        seen_row = []
        for j, _ in enumerate(row):
            if j == 0 or j == (n_col - 1):
                continue
            if i == 0 or i == (n_row - 1):
                continue
            seen_row.append(find_viewing_distance(data, i, j, n_col, n_row))
        if seen_row:
            seen.append(seen_row)

    total = 0
    for x in seen:
        for y in x:
            total = max(y, total)
    print(total)

with open("input.txt", "r") as f:
    data = []
    for row in f:
        data.append([int(x) for x in row.strip()])
"""
data = [
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
]
"""

solution1(data)
solution2(data)
