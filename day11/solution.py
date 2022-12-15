#Monkey will inspect item and create worry level function
#We will then calm down a little by given func (integer divsion by 3)
#Monkey will then thow the item based on a test

#Part 1 has //= 3 in every function
#Part 2 removes this and changes the # rounds from 20 --> 10,000
#Need to use the LCM of all the divisors to not affect the solution.
#Chinese remainder theorem is the key idea behind p2.
class monkey_obj():
    def __init__(self):
        self.items = []
        self.test_num = 0
        self.inspected = 0

class item_obj():
    def __init__(self, worry):
        self.worry = worry

def monkey_zero(item, monkey):
    item.worry *= 13
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def monkey_one(item, monkey):
    item.worry += 2
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def monkey_two(item, monkey):
    item.worry += 8
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def monkey_three(item, monkey):
    item.worry += 1
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def monkey_four(item, monkey):
    item.worry *= 17
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def monkey_five(item, monkey):
    item.worry += 3
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def monkey_six(item, monkey):
    item.worry *= item.worry
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def monkey_seven(item, monkey):
    item.worry += 6
    item.worry %= 2*3*5*7*11*13*17*19
    if item.worry % monkey.test_num == 0:
        return True
    return False

def setup():
    agg_items = [
        [54, 98, 50, 94, 69, 62, 53, 85],
        [71, 55, 82],
        [77, 73, 86, 72, 87],
        [97, 91],
        [78, 97, 51, 85, 66, 63, 62],
        [88],
        [87, 57, 63, 86, 87, 53],
        [73, 59, 82, 65]
    ]
    monkeys = []
    test_nums = [3, 13, 19, 17, 5, 7, 11, 2]
    for i in range(8):
        m = monkey_obj()
        m.test_num = test_nums[i]
        for item in agg_items[i][::-1]:
            m.items.append(item_obj(item))
        monkeys.append(m)
    return monkeys

def partx(monkeys, part):
    rounds = 0
    if part == 1:
        rounds = 20
    else:
        rounds = 10000
    for _ in range(rounds):
        for i in range(8):
            monkey = monkeys[i]
            while monkey.items:
                item = monkey.items.pop()
                match i:
                    case 0:
                        if monkey_zero(item, monkey):
                            monkeys[2].items.insert(0, item)
                        else:
                            monkeys[1].items.insert(0, item)
                    case 1:
                        if monkey_one(item, monkey):
                            monkeys[7].items.insert(0, item)
                        else:
                            monkeys[2].items.insert(0, item)
                    case 2:
                        if monkey_two(item, monkey):
                            monkeys[4].items.insert(0, item)
                        else:
                            monkeys[7].items.insert(0, item)
                    case 3:
                        if monkey_three(item, monkey):
                            monkeys[6].items.insert(0, item)
                        else:
                            monkeys[5].items.insert(0, item)
                    case 4:
                        if monkey_four(item, monkey):
                            monkeys[6].items.insert(0, item)
                        else:
                            monkeys[3].items.insert(0, item)
                    case 5:
                        if monkey_five(item, monkey):
                            monkeys[1].items.insert(0, item)
                        else:
                            monkeys[0].items.insert(0, item)
                    case 6:
                        if monkey_six(item, monkey):
                            monkeys[5].items.insert(0, item)
                        else:
                            monkeys[0].items.insert(0, item)
                    case 7:
                        if monkey_seven(item, monkey):
                            monkeys[4].items.insert(0, item)
                        else:
                            monkeys[3].items.insert(0, item)
                    case _:
                        print("We have an issue")
                monkey.inspected += 1
    top = []
    for i in range(8):
        top.append(monkeys[i].inspected)
    top = sorted(top)
    print(top[-1] * top[-2])

monkeys1 = setup()
partx(monkeys1, 1)
monkeys2 = setup()
partx(monkeys2, 2)