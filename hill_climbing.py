from collections import deque
from magnet_game import MagnetsGame
from tree_node import clone_grid

class HillClimbing:
    def __init__(self, initial_game_level):
        self.initial_game_level = initial_game_level

    def is_solution(self, grid_state):
        
        return all('C' not in row for row in grid_state)

    def evaluate_state(self, grid_state):
       
        return sum(row.count('C') for row in grid_state)

    def print_solution_path(self, parent_map, solution_node):
      
        path = []
        current = solution_node
        while current is not None:
            path.append(current)
            current = parent_map.get(current)

       
        print("Solution Path:")
        for step_num, grid_state in enumerate(reversed(path), start=1):
            print(f"Step {step_num}:")
            for row in grid_state:
                print(''.join(row))
            print()

    def search(self):
       
        current_grid_state = tuple(tuple(row) for row in self.initial_game_level.grid)
        current_cost = self.evaluate_state(current_grid_state)
        
       
        parent_map = {current_grid_state: None}

        while True:
          
            game_level = self.initial_game_level.clone()
            game_level.grid = [list(row) for row in current_grid_state]

            magnets = [
                (row, col)
                for row in range(game_level.rows)
                for col in range(game_level.cols)
                if game_level.grid[row][col] in ['P', 'R']
            ]

          
            best_neighbor = None
            best_cost = current_cost

            for row, col in magnets:
                for n_row in range(game_level.rows):
                    for n_col in range(game_level.cols):
                        if not game_level.is_valid_position(n_row, n_col):
                            continue
                        if game_level.grid[n_row][n_col] not in ['.', 'C']:
                            continue

                       
                        new_grid = clone_grid(game_level.grid)
                        new_game_level = MagnetsGame(game_level.rows, game_level.cols)
                        new_game_level.grid = new_grid
                        new_game_level.circles_positions = game_level.circles_positions[:]

                        if game_level.grid[row][col] == 'P':
                            new_game_level.move_magnet_purple(n_row, n_col)
                        elif game_level.grid[row][col] == 'R':
                            new_game_level.move_magnet_red(n_row, n_col)

                 
                        new_grid_state = tuple(tuple(r) for r in new_game_level.grid)
                        new_cost = self.evaluate_state(new_grid_state)

                      
                        if new_cost < best_cost: 
                            best_neighbor = new_grid_state
                            best_cost = new_cost

           
            if best_neighbor and best_cost < current_cost:
                parent_map[best_neighbor] = current_grid_state  
                current_grid_state = best_neighbor
                current_cost = best_cost
            else:
                
                if self.is_solution(current_grid_state):
                    print("Solution found using Hill Climbing!")
                    self.print_solution_path(parent_map, current_grid_state)
                else:
                    print("No solution found.")
                return
