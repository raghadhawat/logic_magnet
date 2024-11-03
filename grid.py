class Grid:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.grid = [['.' for _ in range(cols)] for _ in range(rows)]
        self.circles_positions = []

    def place_item(self, row, col, item):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = item
            if item == 'C':
                self.circles_positions.append((row, col))
        else:
            print("Invalid position!")

    def print_grid(self):
        for row in self.grid:
            print(' '.join(row))