maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current_node, path = queue.popleft()
        x, y = current_node

        if current_node == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_node = (x + dx, y + dy)
            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols and maze[next_node[0]][next_node[1]] == 0 and next_node not in visited:
                queue.append((next_node, path + [next_node]))
                visited.add(next_node)

    return None  # No path found
  
def dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])

    while stack:
        current_node, path = stack.pop()
        x, y = current_node

        if current_node == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_node = (x + dx, y + dy)
            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols and maze[next_node[0]][next_node[1]] == 0 and next_node not in visited:
                stack.append((next_node, path + [next_node]))
                visited.add(next_node)

    return None  # No path found

def plot_maze(maze, path=None):
    maze_array = np.array(maze)
    plt.imshow(maze_array, cmap='binary')

    if path:
        for (x, y) in path:
            plt.plot(y, x, 'ro')

    plt.show()

if __name__ == "__main__":
    print("Script is running")  # Debug print

    start = (0, 0)
    end = (4, 4)

    print("Running BFS...")  # Debug print
    bfs_path = bfs(maze, start, end)
    print("BFS Path:", bfs_path)  # Debug print

    print("Running DFS...")  # Debug print
    dfs_path = dfs(maze, start, end)
    print("DFS Path:", dfs_path)  # Debug print

    plot_maze(maze, bfs_path)
    plot_maze(maze, dfs_path)