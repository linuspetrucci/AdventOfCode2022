def part1():
    monkeys = read_input(1)
    for i in range(20):
        for monkey in monkeys:
            monkey.take_turn(monkeys)
    return sorted([monkey.inspections for monkey in monkeys])[-1] * sorted([monkey.inspections for monkey in monkeys])[-2]


def part2():
    monkeys = read_input(2)
    for i in range(10000):
        for monkey in monkeys:
            monkey.take_turn(monkeys)
    return sorted([monkey.inspections for monkey in monkeys])[-1] * sorted([monkey.inspections for monkey in monkeys])[-2]


def read_input(part):
    monkeys_raw = open('input.txt', 'r').read().strip().split('\n\n')
    monkeys = []
    modulus = 1
    for monkey_raw in monkeys_raw:
        split_monkey_raw = monkey_raw.split('\n')
        starting_items = [int(item) for item in split_monkey_raw[1][18:].split(',')]
        operation = eval('lambda old : ' + split_monkey_raw[2][19:])
        div = int(split_monkey_raw[3][21:])
        if_true = int(split_monkey_raw[4][29:])
        if_false = int(split_monkey_raw[5][30:])
        monkeys.append(Monkey(starting_items, operation, div, if_true, if_false, part))
        modulus *= div
    for monkey in monkeys:
        monkey.modulus = modulus
    return monkeys


class Monkey:
    def __init__(self, starting_items, operation, div, if_true, if_false, part, modulus=0):
        self.items = starting_items
        self.operation = operation
        self.divisor = div
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0
        self.part = part
        self.modulus = modulus

    def take_turn(self, monkey_list):
        for item in self.items:
            item = self.operation(item)
            item = item // 3 if self.part == 1 else item % self.modulus
            if item % self.divisor == 0:
                monkey_list[self.if_true].items.append(item)
            else:
                monkey_list[self.if_false].items.append(item)
            self.inspections += 1
        self.items = []


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
