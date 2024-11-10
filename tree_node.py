from magnet_game import MagnetsGame


class TreeNode:
    def __init__(self, grid_state):
        self.grid_state = grid_state
        self.children = []
        self.parent = None 

def clone_grid(grid):
    return [row[:] for row in grid]

def generate_purple_move_tree(game_level, node, visited, start_pos=None):
    start_row, start_col = start_pos if start_pos else (0, 0)
    
    for row in range(start_row, game_level.rows):
        for col in range(start_col if row == start_row else 0, game_level.cols):
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
                    node.children.append(child_node)
                    
                    generate_purple_move_tree(new_game_level, child_node, visited, (row, col + 1))

def create_move_tree_for_purple(game_level):
    root = TreeNode(clone_grid(game_level.grid))
    
    visited = {tuple(tuple(row) for row in game_level.grid)}
    
    generate_purple_move_tree(game_level, root, visited)
    
    return root
def print_tree(node, level=0, branch="Root", prefix=""):
    print(f"{branch} - Level {level}", end=" ")

    print("Grid state:")
    for row in node.grid_state:
        print("    " + ' '.join(row))
    
    print("    " + "-" * 20)
    
    if node.children:
        for i, child in enumerate(node.children):
            connector = " ── " if i > 0 else "├── "  
            print(f"{connector}{branch} - Level {level + 1}", end=" ")
            print_tree(child, level + 1, branch=f"Branch {i + 1}", prefix="")

