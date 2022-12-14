import os

def increaseXCoord(coordinate):
    return [coordinate[0] + 1, coordinate[1]]

def decreaseXCoord(coordinate):
    return [coordinate[0] - 1, coordinate[1]]

def increaseYCoord(coordinate):
    return [coordinate[0], coordinate[1] + 1]

def decreaseYCoord(coordinate):
    return [coordinate[0], coordinate[1] - 1]

def moveCoordinate(direction, coordinate):
    if(direction == "U"):
        return increaseYCoord(coordinate)
    elif(direction == "D"):
        return decreaseYCoord(coordinate)
    elif(direction == "L"):
        return decreaseXCoord(coordinate)
    elif(direction == "R"):
        return increaseXCoord(coordinate)

def moveTCoordinate(tCoordinate, hCoordinate):
    if tCoordinate[0] < hCoordinate[0]:
        tCoordinate = increaseXCoord(tCoordinate)
    elif tCoordinate[0] > hCoordinate[0]:
        tCoordinate = decreaseXCoord(tCoordinate)    

    if(tCoordinate[1] < hCoordinate[1]):
        tCoordinate = increaseYCoord(tCoordinate)
    elif(tCoordinate[1] > hCoordinate[1]):
        tCoordinate = decreaseYCoord(tCoordinate)

    return tCoordinate

def adjacent(a, b):
    '''
    Returns True if a and b are adjacent points
    '''
    if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
        return True
    elif a[0] == b[0] and a[1] == b[1]: # Overlapping condition
        return True
    else:
        return False

dir_containing_file = r'C:\\Users\\User\Desktop\\projects\\AOC22\\day9'

# 👇️ change to directory containing file
os.chdir(dir_containing_file)

file_name = 'shortinput.txt'

currentHCoordinate = [0,0]
currentTCoordinate = [0,0]
currentDirection = None
uniqueTCoordinates = [[0,0]]
count = 0;

with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        x = line.split(" ")
        direction = x[0] #U, D, L, R
        numberOfMoves = int(x[1])

        for i in range(numberOfMoves):
            currentHCoordinate = moveCoordinate(direction, currentHCoordinate)
            
            isAdjacent = adjacent(currentHCoordinate, currentTCoordinate)
            if not isAdjacent:
                currentTCoordinate = moveTCoordinate(currentTCoordinate, currentHCoordinate)
                if not currentTCoordinate in uniqueTCoordinates:
                    uniqueTCoordinates.append(currentTCoordinate)
                    count = count + 1;
            # if it is adjacent, don't move the tail
        pass
    pass

print(count)