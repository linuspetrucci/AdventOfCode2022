def part1():
    tree_matrix = read_input()
    visible = [[False for i in range(len(tree_matrix))] for j in range(len(tree_matrix[0]))]

    visible = determine_visible(tree_matrix, visible, 0, len(tree_matrix), 0, len(tree_matrix[0]))
    visible = determine_visible(tree_matrix, visible, 0, len(tree_matrix), len(tree_matrix[0]) - 1, -1, -1)
    visible = determine_visible(tree_matrix, visible, 0, len(tree_matrix), 0, len(tree_matrix[0]), reverse=True)
    visible = determine_visible(tree_matrix, visible, 0, len(tree_matrix[0]), len(tree_matrix) - 1, -1, -1,
                                reverse=True)
    return sum([sum(row) for row in visible])


def determine_visible(matrix, visible, range1_start, range1_stop, range2_start, range2_stop, step=1, reverse=False):
    for i in range(range1_start, range1_stop):
        prev_tree = -1
        a = i
        for j in range(range2_start, range2_stop, step):
            if reverse:
                (i, j) = (j, a)
            if int(matrix[i][j]) > prev_tree:
                visible[i][j] = True
                prev_tree = int(matrix[i][j])
    return visible


def part2():
    tree_matrix = read_input()
    distances = [[0 for i in range(len(tree_matrix))] for j in range(len(tree_matrix[0]))]

    for i in range(len(tree_matrix)):
        for j in range(len(tree_matrix[0])):
            distances[i][j] = determine_distance(tree_matrix, i, j)
    return max([max(distance) for distance in distances])


def determine_distance(tree_matrix, x, y):
    if x == 0 or y == 0 or x == len(tree_matrix) - 1 or y == len(tree_matrix[0]) - 1:
        return 0
    size = int(tree_matrix[x][y])
    x_copy = x - 1
    viz = 1
    while x_copy > 0 and int(tree_matrix[x_copy][y]) < size:
        viz += 1
        x_copy -= 1
    x_copy = x + 1
    score = viz
    viz = 1
    while x_copy < len(tree_matrix) - 1 and int(tree_matrix[x_copy][y]) < size:
        viz += 1
        x_copy += 1
    score *= viz
    viz = 1
    y_copy = y - 1
    while y_copy > 0 and int(tree_matrix[x][y_copy]) < size:
        viz += 1
        y_copy -= 1
    score *= viz
    viz = 1
    y_copy = y + 1
    while y_copy < len(tree_matrix[0]) - 1 and int(tree_matrix[x][y_copy]) < size:
        viz += 1
        y_copy += 1
    return score * viz


def read_input():
    with open('input.txt', 'r') as f:
        input_string = f.read()
        input_string_split = input_string.split('\n')
        tree_matrix = [[*input_string_split[i]] for i in range(len(input_string_split))]
        vertical_lines = ['' for i in range(len(input_string_split[0]))]

        for line in input_string_split:
            for i, tree in enumerate(line):
                vertical_lines[i] += tree
        return tree_matrix


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
