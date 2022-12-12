
def part1():
    return max(get_elves())


def part2():
    elves = get_elves()
    elves.sort()
    return sum(elves[-3:])


def get_elves():
    with open('input.txt') as f:
        lines = f.readlines()
        elves = []
        j = 0
        for i, line in enumerate(lines):
            elves.append(0)
            if lines[i] != '\n':
                elves[j] += int(lines[i])
            else:
                j = j + 1
        return elves


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
