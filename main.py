from bfs import BFS
from dfs import DFS
from game_play import GamePlay
from the_levels import setup_levels
from tree_node import create_move_tree_for_purple, print_tree 




game_levels = setup_levels()

print("Available Levels:")
for i, level in enumerate(game_levels.levels, 1):
    print(f"Level {i}")

selected_level_num = int(input("Choose a level to start (enter the level number): "))
selected_level = game_levels.select_level(selected_level_num)


dfs = DFS(selected_level)
dfs.search()
# dfs.print_full_tree(dfs.root)
# bfs = BFS(selected_level)
# bfs.search()
# game_play = GamePlay(selected_level)

# print(f"Initial grid for Level {selected_level_num}:")
# selected_level.print_grid()
# while True:
#     magnet_types = game_play.check_magnet_types()
   


#     if magnet_types == "both" :
#         chosen_magnet = input("Choose the magnet you want to move ('R' for red, 'P' for purple): ")

#         while True:
#             row = int(input("Enter the row for the new position of the magnet: "))
#             col = int(input("Enter the column for the new position of the magnet: "))
#             if chosen_magnet == 'R':
#                 game_play.make_move_red(row, col)
#             elif chosen_magnet == 'P':
#                 game_play.make_move_purple(row, col)
#             else:
#                 print("Invalid magnet choice. Please choose 'R' or 'P'.")
#                 continue
#             break
            
#     elif magnet_types == "red" :
#         row = int(input("Enter the row for the new position of the red magnet: "))
#         col = int(input("Enter the column for the new position of the red magnet: "))
#         game_play.make_move_red(row, col)
        
#     elif magnet_types == "purple" :
#         row = int(input("Enter the row for the new position of the purple magnet: "))
#         col = int(input("Enter the column for the new position of the purple magnet: "))
#         game_play.make_move_purple(row, col)

#     game_play.print_current_grid()

#     if game_play.check_win_condition():
#         print("Congratulations! You have won!")

#         if selected_level_num < len(game_levels.levels):
#             selected_level_num += 1
#             selected_level = game_levels.select_level(selected_level_num)
#             game_play = GamePlay(selected_level)

#             print(f"Starting Level {selected_level_num}:")
#             selected_level.print_grid()
#         else:
#             print("You have completed all levels!")
#             break