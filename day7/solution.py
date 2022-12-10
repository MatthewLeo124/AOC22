#File system is modelled using a tree system like the following.
"""
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
"""
class TreeNode:
    def __init__(self, parent, name, data = 0):
        self.name = name
        self.parent = parent
        self.size = data
        self.children = []
    
    def is_subfolder(self, name):
        for folder in self.children:
            if folder.name == name:
                return True
        return False
    
    def get_subfolder(self, name):
        for folder in self.children:
            if folder.name == name:
                return folder
        return None

    def add_child(self, name, data = 0):
        to_add = TreeNode(self, name, data)
        self.children.append(to_add)
    
def get_subfolder_size(node, names, sizes):
    if not node.children:
        return
    for child in node.children:
        get_subfolder_size(child, names, sizes)
    names.append(node.name)
    sizes.append(node.size)

def calculate_size(node):
    if not node.children:
        return node.size
    for child in node.children:
        node.size += calculate_size(child)
    return node.size

def print_size(node):
    if not node.children:
        return 0
    total = 0
    for children in node.children:
        total += print_size(children)
    if node.size <= 100_000:
        total += node.size
    return total

def create_tree():
    with open("input.txt", "r") as f:
        curr = None
        for line in f:
            l = line.split()
            if l[0] == "$":
                if l[1] == "cd":
                    name = l[2]
                    if name == "/":
                        if not curr:
                            curr = TreeNode(None, name)
                        else:
                            while curr.parent:
                                curr = curr.parent
                    elif name == "..":
                        if curr.parent:
                            curr = curr.parent
                    else:
                        if (curr.is_subfolder(name)):
                            curr = curr.get_subfolder(name)
                if l[1] == "ls":
                    continue
            else:
                if l[0] == "dir":
                    if not (curr.is_subfolder(l[1])):
                        curr.add_child(l[1])
                else:
                    if not curr.is_subfolder(l[1]):
                        curr.add_child(l[1], int(l[0]))
        
        while curr.parent:
            curr = curr.parent
        
        return curr

root = create_tree()

#Part 1 
calculate_size(root)
#print(print_size(root))

#Part 2
names = []
sizes = []
total_space = 70_000_000
needed_space = 30_000_000
our_needed_space = abs(needed_space - root.size)
get_subfolder_size(root, names, sizes)

least = []
for size in sizes:
    curr_least = our_needed_space - size
    if curr_least < 0:
        least.append((curr_least, size))

print(least)
