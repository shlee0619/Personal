from collections import deque


def bfs_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    queue = deque([start, 0])
    visited = set([start])

    while queue:
        (x,y),steps=queue.popleft()
        if (x,y) == end:
            return steps

        for dx, dy, in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx,ny), steps+1))


    return -1


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)