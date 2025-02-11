import random
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
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
maze = generate_maze(rows, cols)
print_maze(maze)
