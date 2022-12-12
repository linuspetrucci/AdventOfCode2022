def part1():
    elves = read_input()
    count = 0
    for elf1, elf2 in elves:
        elf1_1, elf1_2 = elf1
        elf2_1, elf2_2 = elf2
        if (elf2_1 <= elf1_1 and elf2_2 >= elf1_2) or (elf1_1 <= elf2_1 and elf1_2 >= elf2_2):
            count += 1
    return count


def part2():
    elves = read_input()
    count = 0
    for elf1, elf2 in elves:
        elf1_1, elf1_2 = elf1
        elf2_1, elf2_2 = elf2
        elf1_range = range(elf1_1, elf1_2+1)
        elf2_range = range(elf2_1, elf2_2+1)
        if elf1_1 in elf2_range or elf1_2 in elf2_range or elf2_1 in elf1_range or elf2_2 in elf1_range:
            count += 1
    return count


def read_input():
    with open('input.txt', 'r') as pairs:
        line = pairs.readline()
        elves = []
        while line:
            pair = line.split(',')
            elf1 = pair[0].split('-')
            elf2 = pair[1].split('-')
            elves.append(((int(elf1[0]), int(elf1[1])), (int(elf2[0]), int(elf2[1]))))
            line = pairs.readline()
        return elves


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
