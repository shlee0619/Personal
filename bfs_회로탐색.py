from collections import deque

def bfs_find_paths(graph, start, end):
    queue = deque([(start, [start])])
    paths = []

    while queue:
        current, path= queue.popleft()
        if current == end:
            paths.append(path)
        for neighbor in graph[current]:
            if neighbor not in path:
                queue.append((neighbor, path+[neighbor]))
    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_find_paths(graph, 'A', 'F'))  