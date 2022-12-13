total_space = 70000000
need_unused = 30000000

class Node:
    def __init__(self, name: str, size: int = 0):
        self.name = name
        self.size = size
        self.parent: Node = None
        self.left_child: Node = None
        self.right_sibling: Node = None

    def get_child_by_name(self, name: str):
        if self.left_child and self.left_child.name == name:
            return self.left_child

        sibling = self.left_child.right_sibling

        while sibling:
            if sibling.name == name: return sibling
            sibling = sibling.right_sibling

        return f"Child not found: {name}"

    def set_parent(self, parent):
        self.parent = parent
        if self.size > 0:
            while parent:
                parent.size += self.size
                parent = parent.parent

    def set_new_child(self, child):
        if self.left_child is None:
            self.left_child = child

        else:
            last_child = self.left_child

            while last_child.right_sibling is not None:
                last_child = last_child.right_sibling

            last_child.right_sibling = child


def create_dirtree(root):
    currentdir = root

    with open("input.txt", "r") as input:
        for line in input:
            command = line.strip().split(" ")
            if command[0] == "$":
                if command[1] == "cd":
                    dirname = command[2]
                    if dirname == "/":
                        continue
                    if dirname == "..":
                        currentdir = currentdir.parent
                        continue

                    currentdir = currentdir.get_child_by_name(dirname)

            elif command[0] == "dir":
                dirname = command[1]
                newdir = Node(dirname)
                newdir.set_parent(currentdir)
                currentdir.set_new_child(newdir)
            else:
                size = int(command[0])
                filename = command[1]
                newfile = Node(filename, size)
                newfile.set_parent(currentdir)
                currentdir.set_new_child(newfile)


def print_tree(root):
    print(f"{root.name} ({root.size})")
    if root.left_child:
        print_tree(root.left_child)
    if root.right_sibling:
        print_tree(root.right_sibling)
                
    
def get_dirsizes(root, dirsizes):
    if root.left_child:  # is a directory
        dirsizes.append(root.size)
        get_dirsizes(root.left_child, dirsizes)

    if root.right_sibling:
        get_dirsizes(root.right_sibling, dirsizes)


root = Node("/")
dirtree = create_dirtree(root)
dirsizes = []
get_dirsizes(root, dirsizes)
sorted_sizes = sorted(dirsizes, reverse=True)
need_to_delete = need_unused - (total_space - root.size)
print(f"Total dir sizes: {root.size} on root dir {root.name}")
print(f"Need to delete: {need_to_delete}")
solution2 = None
for size in sorted_sizes:
    if size >= need_to_delete:
        solution2 = size

    else:
        break


print(solution2)
