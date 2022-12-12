score_win = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 'B': {'X': 0, 'Y': 3, 'Z': 6}, 'C': {'X': 6, 'Y': 0, 'Z': 3}}
score_play = {'X': 1, 'Y': 2, 'Z': 3}


def read_input():
    with open('input.txt') as f:
        line = f.readline()
        opponent = []
        me = []
        while line:
            line = line.split(' ')
            opponent.append(line[0])
            me.append(line[1][0])
            line = f.readline()
        return opponent, me


def part1():
    opponent, me = read_input()
    points = sum([score_win[opponent[i]][me[i]] + score_play[me[i]] for i in range(len(opponent))])
    print('points:', points)


def part2():
    map_outcome = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'}, 'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
                   'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}
    opponent, me = read_input()
    me = [map_outcome[opponent[i]][me[i]] for i in range(len(me))]
    points = sum([score_win[opponent[i]][me[i]] + score_play[me[i]] for i in range(len(opponent))])
    print('points:', points)


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
