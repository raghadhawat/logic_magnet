from game_levels import GameLevels


class GamePlay:
    def __init__(self, game_level):
        self.moves = []
        self.game_level = game_level

    def make_move_purple(self, row, col):
        self.game_level.move_magnet_purple(row, col)
        self.moves.append([row, col, [row[:] for row in self.game_level.grid]])
    
    def make_move_red(self, row, col):
        self.game_level.move_magnet_red(row, col)
        self.moves.append([row, col, [row[:] for row in self.game_level.grid]])
     

    def check_magnet_types(self):
        red_found = False
        purple_found = False

        for row in self.game_level.grid:  # Access grid from game_level
            if 'R' in row:
                red_found = True
            if 'P' in row:
                purple_found = True

        if red_found and purple_found:
            return "both"
        elif red_found:
            return "red"
        elif purple_found:
            return "purple"
        else:
            return "none"

    def print_current_grid(self):
        print("Current grid:")
        self.game_level.print_grid()

    def check_win_condition(self):
        for row in self.game_level.grid:
            if 'C' in row:
                return False
        return True