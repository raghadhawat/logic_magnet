from collections import deque
from magnet_game import MagnetsGame
from tree_node import TreeNode, clone_grid

class BFS:
    def __init__(self, initial_game_level):
        self.initial_game_level = initial_game_level

    def is_solution(self, grid_state):
        return all('C' not in row for row in grid_state)

    def print_solution_path(self, parent_map, solution_node):
        path = []
        current = solution_node
        while current is not None:
            path.append(current.grid_state)
            current = parent_map.get(current)

        # Print steps from start to solution
        print("Solution Path:")
        for step_num, grid in enumerate(reversed(path), start=1):
            print(f"Step {step_num}:")
            for row in grid:
                print(''.join(row))
            print()

    def search(self):
        root = TreeNode(clone_grid(self.initial_game_level.grid))
        visited = {tuple(tuple(row) for row in self.initial_game_level.grid)}
        queue = deque([root])
        parent_map = {root: None}  # Track parent-child relationships

        while queue:
            current_node = queue.popleft()

            if self.is_solution(current_node.grid_state):
                print("Solution found! BFS")
                self.print_solution_path(parent_map, current_node)
                return

            game_level = self.initial_game_level.clone()  # Ensure the game level matches the current node
            game_level.grid = clone_grid(current_node.grid_state)

            # Find all magnets and iterate through their possible moves
            magnets = [
                (row, col)
                for row in range(game_level.rows)
                for col in range(game_level.cols)
                if game_level.grid[row][col] in ['P', 'R']
            ]

            for row, col in magnets:
                for n_row in range(game_level.rows):
                    for n_col in range(game_level.cols):
                        if not game_level.is_valid_position(n_row, n_col):
                            continue
                        if game_level.grid[n_row][n_col] not in ['.', 'C']:
                            continue

                        # Clone the grid and move the magnet
                        new_grid = clone_grid(game_level.grid)
                        new_game_level = MagnetsGame(game_level.rows, game_level.cols)
                        new_game_level.grid = new_grid
                        new_game_level.circles_positions = game_level.circles_positions[:]
                        
                        if game_level.grid[row][col] == 'P':
                            new_game_level.move_magnet_purple(n_row, n_col)
                        elif game_level.grid[row][col] == 'R':
                            new_game_level.move_magnet_red(n_row, n_col)

                        grid_state = tuple(tuple(r) for r in new_game_level.grid)
                        if grid_state not in visited:
                            visited.add(grid_state)
                            child_node = TreeNode(new_game_level.grid)
                            parent_map[child_node] = current_node  # Record parent-child relationship
                            queue.append(child_node)

        print("No solution found.")
