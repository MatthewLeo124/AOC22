with open("input.txt", "r") as f:
    p1 = 0
    p2 = 0
    for line in f:
        pair = [line.split(',')[0].strip(), line.split(',')[1].strip()]
        pair[0] = pair[0].split('-')
        pair[1] = pair[1].split('-')
        
        elf1_lower, elf1_higher = int(pair[0][0]), int(pair[0][1])
        elf2_lower, elf2_higher = int(pair[1][0]), int(pair[1][1])
        
        #p1 logic
        if (elf1_lower <= elf2_lower and elf1_higher >= elf2_higher) or (elf2_lower <= elf1_lower and elf2_higher >= elf1_higher):
            p1 += 1
        
        #p2 logic
        if not(elf1_lower > elf2_higher) and not(elf2_lower > elf1_higher):
            p2 += 1

print(p1)
print(p2)
