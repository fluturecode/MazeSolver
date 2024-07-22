# Maze Solver using BFS and DFS

## Description
This project implements a maze solver using Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms. The solver finds paths from a starting point to an endpoint in a maze represented by a 2D grid.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/MazeSolver.git
    cd MazeSolver
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv maze_solver_env
    source maze_solver_env/bin/activate  # On macOS/Linux
    # or
    maze_solver_env\Scripts\activate  # On Windows
    ```

3. **Install the required libraries**:
    ```bash
    pip install numpy matplotlib
    ```

## Usage
1. **Activate the virtual environment** (if not already activated):
    ```bash
    source maze_solver_env/bin/activate  # On macOS/Linux
    # or
    maze_solver_env\Scripts\activate  # On Windows
    ```

2. **Run the `maze_solver.py` script**:
    ```bash
    python maze_solver.py
    ```

## Example
Below is an example of a maze and the paths found by BFS and DFS:

```plaintext
Maze:
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
0 1 1 1 0
0 0 0 0 0

BFS Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
DFS Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]


## Project Structure

MazeSolver/
│
├── maze_solver_env/     # Virtual environment directory
├── README.md            # Project documentation
└── maze_solver.py       # Main script for maze solving

How it Works

The maze_solver.py script defines a maze using a 2D grid where 1 represents walls and 0 represents paths. It then uses BFS and DFS algorithms to find paths from the start point (0, 0) to the endpoint (4, 4). The results are printed to the console and visualized using Matplotlib.

Dependencies

	•	Python 3.6+
	•	NumPy
	•	Matplotlib

License

This project is licensed under the MIT License - see the LICENSE file for details.