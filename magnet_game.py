from grid import Grid

class MagnetsGame(Grid):
    def __init__(self, rows=3, cols=3):
        super().__init__(rows, cols)
        self.prev_magnet_position = None

    def move_magnet_purple(self, row, col):
        if  not self.is_valid_position(row, col) :
            print("Cannot move the magnet to an invalid position!")
            return 
        if  self.grid[row][col] == 'S' or self.grid[row][col] == 'X':
            print("Cannot move the magnet to a rock position or an invalid position!")
            return
        
        self.find_and_clear_magnet_purple()

        # Move the magnet to the new position
        self.place_item(row, col, 'P')
        self.prev_magnet_position = (row, col)

        self.apply_rules_purple(row, col)

    def move_magnet_red(self, row, col):
        if  not self.is_valid_position(row, col) :
            print("Cannot move the magnet to an invalid position!")
            return 
        if  self.grid[row][col] == 'R' or self.grid[row][col] == 'X':
            print("Cannot move the magnet to a rock position or an invalid position!")
            return
        
        self.find_and_clear_magnet_red()

        # Move the magnet to the new position
        self.place_item(row, col, 'R')
        self.prev_magnet_position = (row, col)

        self.apply_rules_red(row, col)

    def apply_rules_purple(self, row, col):
        for r in range(row-1, -1, -1):
            if self.is_valid_position(r, col) and (self.grid[r][col] == 'S' or self.grid[r][col] == 'R'):
                if r - 1 >= 0 and (self.grid[r - 1][col] == '.' or self.grid[r - 1][col] == 'C'):
                    self.grid[r][col], self.grid[r - 1][col] = ('C' if (r, col) in self.circles_positions else '.'), self.grid[r][col]
                elif r - 1 >= 0 and (self.grid[r - 1][col] == 'S' or self.grid[r - 1][col] == 'R'):
                    if r - 2 >= 0:
                        self.grid[r - 2][col] = self.grid[r - 1][col] 
                    self.grid[r][col], self.grid[r - 1][col]  = ('C' if (r, col) in self.circles_positions else '.'), self.grid[r][col]
                    
                break

        for r in range(row+1, self.rows):
            if self.is_valid_position(r, col) and (self.grid[r][col] == 'S' or self.grid[r][col] == 'R') :
                if r + 1 < self.rows and (self.grid[r + 1][col] == '.' or self.grid[r + 1][col] == 'C'):
                    self.grid[r][col], self.grid[r + 1][col] = ('C' if (r, col) in self.circles_positions else '.'), self.grid[r][col]
                elif r + 1 < self.rows and (self.grid[r + 1][col] == 'S' or self.grid[r + 1][col] == 'R'):
                    if r + 2 < self.rows:
                        self.grid[r + 2][col] = self.grid[r + 1][col]
                    self.grid[r][col], self.grid[r + 1][col] = ('C' if (r, col) in self.circles_positions else '.'), self.grid[r][col]
                    
                break

        for c in range(col-1, -1, -1):
            if self.is_valid_position(row, c) and (self.grid[row][c] == 'S' or self.grid[row][c] == 'R'):
                if c - 1 >= 0 and (self.grid[row][c - 1] == '.' or self.grid[row][c - 1] == 'C'):
                    self.grid[row][c], self.grid[row][c - 1] = ('C' if (row, c) in self.circles_positions else '.'), self.grid[row][c]
                elif c - 1 >= 0 and (self.grid[row][c - 1] == 'S' or self.grid[row][c - 1] == 'R'):
                    if c - 2 >= 0:
                        self.grid[row][c - 2] = self.grid[row][c - 1]
                    self.grid[row][c], self.grid[row][c - 1] = ('C' if (row, c) in self.circles_positions else '.'), self.grid[row][c]
                    
                break

        for c in range(col+1, self.cols):
            if self.is_valid_position(row, c) and (self.grid[row][c] == 'S' or self.grid[row][c] == 'R'):
                if c + 1 < self.cols and (self.grid[row][c + 1] == '.' or self.grid[row][c + 1] == 'C'):
                    self.grid[row][c], self.grid[row][c + 1] = ('C' if (row, c) in self.circles_positions else '.'), self.grid[row][c]
                elif c + 1 < self.cols and (self.grid[row][c + 1] == 'S' or self.grid[row][c + 1] == 'R'):
                    if c + 2 < self.cols:
                        self.grid[row][c + 2] = self.grid[row][c + 1]
                    self.grid[row][c], self.grid[row][c + 1] = ('C' if (row, c) in self.circles_positions else '.'), self.grid[row][c]
                    
                break
    
    def apply_rules_red(self, row, col):
        for r in range(row-1, -1, -1):
            if self.is_valid_position(r, col) and (self.grid[r][col] == 'S' or self.grid[r][col] == 'P'):
                if not self.grid[r + 1][col] == 'R' and (self.grid[r + 1][col] == '.' or self.grid[r + 1][col] == 'C'):
                    self.grid[r][col], self.grid[r + 1][col] = ('C' if (r, col) in self.circles_positions else '.'), self.grid[r][col]
                
                

        for r in range(row+1, self.rows):
             if self.is_valid_position(r, col) and (self.grid[r][col] == 'S' or self.grid[r][col] == 'P'):
                if not self.grid[r - 1][col] == 'R' and (self.grid[r - 1][col] == '.' or self.grid[r - 1][col] == 'C'):
                    self.grid[r][col], self.grid[r - 1][col] = ('C' if (r, col) in self.circles_positions else '.'), self.grid[r][col]
                

        for c in range(col-1, -1, -1):
            if self.is_valid_position(row, c) and (self.grid[row][c] == 'S' or self.grid[row][c] == 'P'):
                if not self.grid[row][c + 1] == 'R' and (self.grid[row][c + 1] == '.' or self.grid[row][c + 1] == 'C'):
                    self.grid[row][c], self.grid[row][c + 1] = ('C' if (row, c) in self.circles_positions else '.'), self.grid[row][c]
                

        for c in range(col+1, self.cols):
           if self.is_valid_position(row, c) and (self.grid[row][c] == 'S' or self.grid[row][c] == 'P'):
                if not self.grid[row][c - 1] == 'R' and (self.grid[row][c - 1] == '.' or self.grid[row][c - 1] == 'C'):
                    self.grid[row][c], self.grid[row][c - 1] = ('C' if (row, c) in self.circles_positions else '.'), self.grid[row][c]
                

    def find_and_clear_magnet_purple(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 'P' :
                    if (row, col) in self.circles_positions:
                        self.place_item(row, col, 'C')
                    else:
                        self.place_item(row, col, '.')
    
   


    def find_and_clear_magnet_red(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 'R' :
                    if (row, col) in self.circles_positions:
                        self.place_item(row, col, 'C')
                    else:
                        self.place_item(row, col, '.')
                    

    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

