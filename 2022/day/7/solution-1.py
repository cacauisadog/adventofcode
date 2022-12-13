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
        if root.size <= 100000:
            dirsizes.append(root.size)
        get_dirsizes(root.left_child, dirsizes)

    if root.right_sibling:
        get_dirsizes(root.right_sibling, dirsizes)


root = Node("/")
dirtree = create_dirtree(root)
dirsizes = []
get_dirsizes(root, dirsizes)
print_tree(root)
solution1 = sum(dirsizes)
print(f"Solution 1: {solution1}")
