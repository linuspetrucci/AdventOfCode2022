def part1():
    stacks, amount, origin, destination = read_input()

    for j, amount_j in enumerate(amount):
        for i in range(amount_j):
            stacks[destination[j]-1].append(stacks[origin[j]-1].pop())
    top_crates = [stack.pop() for stack in stacks]
    return top_crates


# ['[G]', '[C]', '[F]', '[G]', '[L]', '[D]', '[N]', '[J]', '[Z]']
def part2():
    stacks, amount, origin, destination = read_input()

    for j, amount_j in enumerate(amount):
        for i in range(amount_j):
            stacks[destination[j]-1].append(stacks[origin[j] - 1].pop(-amount_j+i))
    top_crates = [stack.pop() for stack in stacks]
    return top_crates


def read_input():
    with open('input.txt', 'r') as f:
        line = f.readline()
        num_stacks = len(line) // 4
        stacks = [[] for _ in range(num_stacks)]
        while not line[1].isdigit():
            for i in range(num_stacks):
                if line[i*4:(i+1)*4-1] != '   ':
                    stacks[i].append(line[i*4:(i+1)*4-1])
            line = f.readline()
        _ = f.readline()
        line = f.readline()
        amount = []
        origin = []
        destination = []
        while line:
            split_line = line.split(' ')
            amount.append(int(split_line[1]))
            origin.append(int(split_line[3]))
            destination.append(int(split_line[5]))
            line = f.readline()
        for stack in stacks:
            stack.reverse()
        return stacks, amount, origin, destination


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
