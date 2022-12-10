#Suposed to be a sliding window
#But doesn't work on the len = 14 case.
#Sliding window doesn't have to jump around, which broke this.
def solution(s, lim):
    def unique(ss):
        if len(set(ss)) == lim:
            return True
        return False

    end = lim
    while end < len(s):
        window = s[end - lim:end]
        c = s[end]
        if c in window:
            offset = window.index(c) + 1
            end += offset
        elif unique(window):
            break
        else:
            end += 1
    print(end)

#Brute force approach
def brute_force(s):
    i = 14
    while i < len(s):
        if len(set(s[i - 14: i])) != 14:
            i += 1
        else:
            return i

#Taken from reddit u: kebabmybob.
def sliding_window(s, marker):
    counts = dict()
    window = set()
    for i in range(marker):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
        window.add(s[i])
    for i in range(marker, len(s)):
        start = s[i - marker]
        end = s[i]
        counts[start] -= 1
        if not counts[start]:
            window.remove(start)

        if end in counts:
            counts[end] += 1
        else:
            counts[end] = 1
        window.add(end)
        if len(window) == marker:
            print(i + 1)
            break


with open("input.txt", "r") as f:
    s = f.read().strip()
    solution(s, 4)
    print(brute_force(s))
    sliding_window(s, 14)
    sliding_window(s, 30)

           
