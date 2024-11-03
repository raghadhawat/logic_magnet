class GameLevels:
    def __init__(self):
        self.levels = []

    def add_level(self, level):
        self.levels.append(level)

    def select_level(self, level_num):
        if 1 <= level_num <= len(self.levels):
            return self.levels[level_num - 1]
        else:
            print("Invalid level number!")

    def edit_level(self, level_num, new_level):
        if 1 <= level_num <= len(self.levels):
            self.levels[level_num - 1] = new_level
            print(f"Level {level_num} has been updated.")
        else:
            print("Invalid level number!")