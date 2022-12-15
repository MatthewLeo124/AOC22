with open("input.txt", "r") as f:
    clock_cycle = 1
    x_reg = 1 #Start from 1, not 0
    vals = []
    print("Part 2:\n")
    while True:
        #Start of instruction
        line = f.readline().strip().split()
        
        #Reach EOF, END
        if not line:
            break

        #If no-op
        if line[0] == "noop":
            if clock_cycle == 20 or (clock_cycle - 20) % 40 == 0:
                vals.append(clock_cycle * x_reg)

            if (clock_cycle - 1) % 40 in [x_reg - 1, x_reg, x_reg + 1]:
                print("#", end='')
            else:
                print(".", end='')

            if clock_cycle % 40 == 0:
                    print("")
            #End of Cycle
            clock_cycle += 1 

        #If Addx
        else:
            for _ in range(2):
                #Middle of cycle
                if clock_cycle == 20 or (clock_cycle - 20) % 40 == 0:
                    vals.append(clock_cycle * x_reg)

                if (clock_cycle - 1) % 40 in [x_reg - 1, x_reg, x_reg + 1]:
                    print("#", end='')
                else:
                    print(".", end='')

                if clock_cycle % 40 == 0:
                    print("")
                #End of cycle
                clock_cycle += 1 
            #Post cycle
            x_reg += int(line[1])
    
    #Part 1

    print(f"\nPart 1: {sum(vals)}")
    print(clock_cycle)

