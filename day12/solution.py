#S: {X: 0, Y: 20}
#E: {X: 146, Y: 20}
import math
import heapq

def initialise_map(f):
    height_map = []
    e = None
    s = None
    for r, line in enumerate(f):
        chars = line.strip()
        t = []
        for c, char in enumerate(chars):
            if char == "E" or char == "S":
                if char == "E":
                    e = (r, c)
                    t.append(ord('z') - ord('a'))
                elif char == "S":
                    s = (r, c)
                    t.append(ord('a') - ord('a'))
            else:
                t.append(ord(char) - ord('a'))
        height_map.append(t)
    return s, e, height_map

#Manhattan distance
def heuristic(row, col, row_end, col_end):
    return abs(row - row_end) + abs(col - col_end)


#Part 1 We discover a route from S -> E.
#Part 2 We go in reverse and go from E -> any 'a'

with open("input.txt", "r") as f:
    #P1: Start, end, heights = initialise_map(f)
    end, start, heights = initialise_map(f)
    prio = []
    rows = len(heights)
    cols = len(heights[0])
    costs = [[math.inf] * cols for _ in range(rows)]
    costs[start[0]][start[1]] = 0
    heapq.heappush(prio, (0, start[0], start[1]))
    ns = [0, 1, 0, -1, 0]

    while prio:
        w, row, col = heapq.heappop(prio)

        #Part 1: When we have reached the end, return the number of steps taken to get here.
        #if row == end[0] and col == end[1]:
        #    break

        #Part2: If we have discovered 'a', return it.
        if heights[row][col] == ord('a') - ord('a'):
            print(costs[row][col])
            break

        #Get Neighbours
        for i in range(4):
            n_row, n_col = row + ns[i], col + ns[i + 1]

            #Make sure the new row and col is in bounds.
            if not (0 <= n_row < rows and 0 <= n_col < cols):
                continue

            #For P1: heights[n_row][n_col]<= heights[row][col] + 1
            #Part 1: The tile we are want to explore can be at most 1 taller or any amount shoter
            #Part 2: The current tile must can only be 1 taller than the one we want to move to.
            if  heights[row][col] <= heights[n_row][n_col] + 1:
                #Cost to get to any node is 1
                new_cost = costs[row][col] + 1

                #If our calculated cost is > new cost, replace it
                if costs[n_row][n_col] > new_cost:
                    costs[n_row][n_col] = new_cost

                    #A* Search is F = G + H, 
                    #G is the cost function (+1 in this case),
                    #F is the priority number
                    #heuristic is the manhattan distance
                    #Note that BFS and Djikstra's are special cases of A*
                    # Djikstra where h = 0 for all nodes.
                    # BFS where H = 0 and C = 1 for all nodes. 

                    priority = new_cost #+ heuristic(n_row, n_col, end[0], end[1])
                    heapq.heappush(prio, (priority, n_row, n_col))
                    #print(n_row, n_col, priority)

    print(costs[end[0]][end[1]])

