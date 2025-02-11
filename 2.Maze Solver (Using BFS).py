import random
from collections import deque
def generate_maze(rows, cols):
    maze = [['#'] * cols for _ in range(rows)] 
    def carve(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < rows - 1 and 1 <= ny < cols - 1 and maze[nx][ny] == '#':
                maze[nx - dx // 2][ny - dy // 2] = '.'
                maze[nx][ny] = '.'
                carve(nx, ny)
    maze[1][1] = '.'
    carve(1, 1)   
    return maze
def print_maze(maze):
    for row in maze:
        print("".join(row))
def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = (1, 1), (rows - 2, cols - 2)
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path    
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (1 <= nx < rows - 1 and 1 <= ny < cols - 1 and 
                maze[nx][ny] == '.' and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
maze = generate_maze(rows, cols)
print("\nGenerated Maze:")
print_maze(maze)
solution_path = solve_maze(maze)
if solution_path:
    print("\nSolution Path (coordinates):", solution_path)
else:
    print("\nNo solution found.")
