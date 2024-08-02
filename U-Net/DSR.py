# Name: Ahmed Hosny Abdelrazik
# Sec: 1
# Bn: 2
from collections import defaultdict, deque


def bfs(graph, source, destination) -> dict[int, list[int]]: 
    paths = defaultdict(list)
    paths[source] = [source]
    paths[destination] = [-1]

    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        vertex = queue.popleft()
        for neighbour in sorted(graph[vertex]):
            if neighbour not in visited and neighbour != destination and paths[vertex] != [-1]:
                new_path = paths[vertex] + [neighbour]
                if paths[neighbour] == [] or len(new_path) < len(paths[neighbour]) or (len(new_path) == len(paths[neighbour]) and new_path < paths[neighbour]):
                    paths[neighbour] = new_path
                    queue.append(neighbour)
                    visited.add(neighbour)
    return paths

if __name__ == '__main__':
    graph = defaultdict(list)
    nodes, edges = map(int, input().split())
    for _ in range(edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    source, destination = map(int, input().split())
    paths = bfs(graph, source, destination)
    for i in range(nodes):
        if i + 1 in paths:
            print(' '.join(str(x) for x in paths[i + 1]))
        else:
            print('-1')