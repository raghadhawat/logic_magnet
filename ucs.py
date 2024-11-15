from heapq import heappush, heappop
from collections import deque
from magnet_game import MagnetsGame
from tree_node import TreeNode, clone_grid

class UCS:
    def __init__(self, initial_game_level):
        self.initial_game_level = initial_game_level

    def is_solution(self, grid_state):
        return all('C' not in row for row in grid_state)

    def print_solution_path(self, parent_map, costs, solution_node):
        path = []
        current = solution_node
        while current is not None:
            path.append(current)
            current = parent_map.get(current)

        # Print steps from start to solution
        print("Solution Path:")
        for step_num, grid_state in enumerate(reversed(path), start=1):
            cost = costs[grid_state]
            print(f"Step {step_num} (Weight: {cost}):")
            for row in grid_state:
                print(''.join(row))
            print()

    def search(self):
        initial_grid_state = tuple(tuple(row) for row in self.initial_game_level.grid)
        
        # Priority queue with (cost, grid state)
        pq = []
        heappush(pq, (0, initial_grid_state))

        visited = {initial_grid_state: 0}  # Map to track the minimum cost to reach each state
        parent_map = {initial_grid_state: None}  # To reconstruct the solution path

        while pq:
            current_cost, current_grid_state = heappop(pq)

            # Check if the current state is a solution
            if self.is_solution(current_grid_state):
                print("Solution found! UCS")
                self.print_solution_path(parent_map, visited, current_grid_state)
                return

            # Restore the game level for this state
            game_level = self.initial_game_level.clone()
            game_level.grid = [list(row) for row in current_grid_state]

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
                            step_cost = 2  # Cost for moving purple magnet
                        elif game_level.grid[row][col] == 'R':
                            new_game_level.move_magnet_red(n_row, n_col)
                            step_cost = 1  # Cost for moving red magnet

                        new_grid_state = tuple(tuple(r) for r in new_game_level.grid)
                        new_cost = current_cost + step_cost

                        # Check if we should update this state in the visited map
                        if new_grid_state not in visited or visited[new_grid_state] > new_cost:
                            visited[new_grid_state] = new_cost
                            parent_map[new_grid_state] = current_grid_state  # Record parent-child relationship
                            heappush(pq, (new_cost, new_grid_state))

        print("No solution found.")
