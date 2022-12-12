def part1():
    signal = read_input()
    buffer = []
    for i, data in enumerate(signal):
        while data in buffer:
            buffer.pop(0)
        buffer.append(data)
        if len(buffer) == 4:
            return i + 1


def part2():
    signal = read_input()
    buffer = []
    for i, data in enumerate(signal):
        while data in buffer:
            buffer.pop(0)
        buffer.append(data)
        if len(buffer) == 14:
            return i + 1


def read_input():
    with open('input.txt', 'r') as f:
        return f.readline()


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
