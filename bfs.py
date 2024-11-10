from collections import deque
from magnet_game import MagnetsGame
from tree_node import TreeNode, clone_grid


class BFS:
    def __init__(self, initial_game_level):
        self.initial_game_level = initial_game_level

    def is_solution(self, grid_state):
        return all('C' not in row for row in grid_state)

    def print_solution_path(self, node):
        if node is None:
            return
        self.print_solution_path(node.parent)
        for row in node.grid_state:
            print(''.join(row))
        print()

    def search(self):
        root = TreeNode(clone_grid(self.initial_game_level.grid))
        visited = {tuple(tuple(row) for row in self.initial_game_level.grid)}
        queue = deque([(root, self.initial_game_level, None)])

        while queue:
            current_node, game_level, parent = queue.popleft()
            current_node.parent = parent

            if self.is_solution(current_node.grid_state):
                print("Solution found! BFS")
                self.print_solution_path(current_node)
                return

            for row in range(game_level.rows):
                for col in range(game_level.cols):
                    if game_level.grid[row][col] in ['.', 'C']:
                        new_grid = clone_grid(game_level.grid)
                        new_game_level = MagnetsGame(game_level.rows, game_level.cols)
                        new_game_level.grid = new_grid
                        new_game_level.circles_positions = game_level.circles_positions[:]
                        new_game_level.move_magnet_purple(row, col)

                        grid_state = tuple(tuple(r) for r in new_game_level.grid)
                        if grid_state not in visited:
                            visited.add(grid_state)
                            child_node = TreeNode(new_game_level.grid)
                            current_node.children.append(child_node)
                            queue.append((child_node, new_game_level, current_node))

        print("No solution found.")