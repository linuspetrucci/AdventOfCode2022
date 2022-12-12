def part1():
    x = read_input()
    return sum((i+1) * x[i] for i in range(19, 221, 40))


def part2():
    x = read_input()
    for i, signal in enumerate(x):
        if abs(signal - (i%40)) <= 1:
            print('#', end='')
        else:
            print('.', end='')
        if ((i+1) % 40) == 0:
            print()


def read_input():
    lines = open('input.txt').read().strip().split('\n')
    x = [1]
    for i, line in enumerate(lines):
        if line[0] == 'a':
            x.append(x[-1])
            x.append(x[-1] + int(line[5:]))
        else:
            x.append(x[-1])
    return x


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
