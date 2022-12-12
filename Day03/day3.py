def read_input():
    with open('input.txt') as f:
        line = f.readline()
        rucksacks = []
        while line:
            line = line.rstrip('\n')
            rucksacks.append(line)
            line = f.readline()
        return rucksacks


def part1():
    rucksacks = read_input()
    first = [item[:len(item) // 2] for item in rucksacks]
    second = [item[len(item) // 2:] for item in rucksacks]
    priority_sum = 0
    for i in range(len(first)):
        ascii_char = ord([item for item in first[i] if item in second[i]][0])
        if ascii_char > 90:
            priority_sum += ascii_char - 96
        else:
            priority_sum += ascii_char - 38
    return priority_sum


def part2():
    rucksacks = read_input()
    priority_sum = 0
    for i in range(0, len(rucksacks), 3):
        elf1 = rucksacks[i]
        elf2 = rucksacks[i+1]
        elf3 = rucksacks[i+2]
        ascii_char = ord([item for item in elf1 if (item in elf2 and item in elf3)][0])
        if ascii_char > 90:
            priority_sum += ascii_char - 96
        else:
            priority_sum += ascii_char - 38
    return priority_sum


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
