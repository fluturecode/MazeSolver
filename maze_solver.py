from collections import deque

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        (current_node, path) = queue.popleft()
        x, y = current_node
        
        if current_node == end:
            return path
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_node = (x + dx, y + dy)
            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols and maze[next_node[0]][next_node[1]] == 0 and next_node not in visited:
                queue.append((next_node, path + [next_node]))
                visited.add(next_node)
    
    return None