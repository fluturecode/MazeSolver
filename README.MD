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