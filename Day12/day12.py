import sys


def part1():
    start, end, graph = read_input(1)
    dist = dijkstra(start, graph)
    return dist[end]


def part2():
    start, end, graph = read_input(2)
    dist = dijkstra(end, graph)
    min_dist_a = sys.maxsize
    for i, letter in enumerate(open('input.txt', 'r').read().strip().replace('\n', '')):
        if letter == 'a' and min_dist_a > dist[i]:
            min_dist_a = dist[i]
    return min_dist_a


def dijkstra(start, graph):
    dist = [sys.maxsize for _ in graph.keys()]
    q = set(graph.keys())
    dist[start] = 0

    while q:
        min_dist = sys.maxsize
        u = -1
        for i in q:
            if dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if min_dist == sys.maxsize:
            break
        q.remove(u)

        for neighbor in graph[u]:
            if neighbor in q and dist[neighbor] > dist[u] + 1:
                dist[neighbor] = dist[u] + 1
    return dist


def read_input(part):
    lines = open('input.txt', 'r').read().strip().split('\n')
    matrix = [[lines[i][j] for j in range(len(lines[0]))] for i in range(len(lines))]
    start = 0
    end = 0
    graph = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if matrix[i][j] == 'S':
                start = i * len(lines[0]) + j
                matrix[i][j] = 'a'
            if matrix[i][j] == 'E':
                end = i * len(lines[0]) + j
                matrix[i][j] = 'z'
            graph[i * len(lines[0]) + j] = get_neighbors(i, j, matrix, part)
    return start, end, graph


def get_neighbors(x, y, matrix, part):
    neighbors = []
    for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if new_x >= len(matrix) or new_y >= len(matrix[0]) or new_x < 0 or new_y < 0:
            continue
        if ord(matrix[new_x][new_y]) - ord(matrix[x][y]) <= 1 and part == 1:
            neighbors.append(new_x * len(matrix[0]) + new_y)
        if ord(matrix[new_x][new_y]) - ord(matrix[x][y]) >= -1 and part == 2:
            neighbors.append(new_x * len(matrix[0]) + new_y)
    return neighbors


if __name__ == '__main__':
    print(f'part1: {part1()}')
    print(f'part2: {part2()}')
