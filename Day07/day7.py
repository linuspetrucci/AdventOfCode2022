def part1():
    root = read_input()
    dir_sizes = get_sizes(root, [])
    return sum([dir_size for dir_size in dir_sizes if dir_size <= 100000])


def get_sizes(directory, size_list):
    size_list.append(directory.size)
    for child in directory.children:
        if child.entry_type == 'dir':
            size_list = get_sizes(child, size_list)
    return size_list


def part2():
    root = read_input()
    dir_sizes = get_sizes(root, [])
    return min([dir_size for dir_size in dir_sizes if dir_size >= root.size - 70000000 + 30000000])


def read_input():
    input_string = open('input.txt', 'r').read().strip()
    input_string_list = input_string.split('\n')
    root = Directory('/', None, 'dir')
    curr_dir = root
    for line in input_string_list[1:]:
        if line[0] == '$':
            if line[2:4] == 'cd':
                if line[5:7] == '..':
                    curr_dir = curr_dir.parent
                else:
                    for directory in curr_dir.children:
                        if directory.name == line[5:len(line) - 1]:
                            curr_dir = directory
        else:
            if line[0:3] == 'dir':
                curr_dir.add_child(Directory(line[4:len(line) - 1], curr_dir, 'dir'))
            else:
                split_line = line.split(' ')
                curr_dir.add_child(Directory(split_line[1], curr_dir, 'file', int(split_line[0])))
                curr_dir.update_size()
    return root


class Directory:
    def __init__(self, name, parent, entry_type, size=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.entry_type = entry_type
        self.size = size

    def add_child(self, child):
        self.children.append(child)

    def update_size(self):
        new_size = 0
        for child in self.children:
            new_size += child.size
        self.size = new_size
        if self.parent:
            self.parent.update_size()


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
