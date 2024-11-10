from game_levels import GameLevels
from magnet_game import MagnetsGame

def setup_levels():
    game_levels = GameLevels()

    # Level 1 setup
    level1 = MagnetsGame(3, 4)
    level1.place_item(1, 2, 'S')
    level1.place_item(1, 3, 'C')
    level1.place_item(1, 1, 'C')
    level1.place_item(2, 0, 'P')
    game_levels.add_level(level1)

    # Level 2 setup
    level2 = MagnetsGame(5, 5)
    level2.place_item(1, 2, 'S')
    level2.place_item(2, 1, 'S')
    level2.place_item(3, 2, 'S')
    level2.place_item(2, 3, 'S')
    level2.place_item(0, 2, 'C')
    level2.place_item(2, 0, 'C')
    level2.place_item(2, 2, 'C')
    level2.place_item(4, 2, 'C')
    level2.place_item(2, 4, 'C')
    level2.place_item(4, 0, 'P')
    game_levels.add_level(level2)

    # Level 3 setup
    level3 = MagnetsGame(3, 4)
    level3.place_item(1, 2, 'S')
    level3.place_item(0, 3, 'C')
    level3.place_item(2, 3, 'C')
    level3.place_item(2, 0, 'P')
    game_levels.add_level(level3)

    # Level 4 setup
    level4 = MagnetsGame(5, 3)
    level4.place_item(1, 1, 'S')
    level4.place_item(3, 1, 'S')
    level4.place_item(0, 0, 'C')
    level4.place_item(0, 2, 'C')
    level4.place_item(4, 1, 'C')
    level4.place_item(2, 0, 'P')
    game_levels.add_level(level4)

    # Level 5 setup
    level5 = MagnetsGame(4, 3)
    level5.place_item(1, 0, 'S')
    level5.place_item(2, 0, 'S')
    level5.place_item(1, 2, 'S')
    level5.place_item(2, 2, 'S')
    level5.place_item(0, 0, 'C')
    level5.place_item(0, 2, 'C')
    level5.place_item(3, 0, 'C')
    level5.place_item(3, 1, 'P')
    game_levels.add_level(level5)

    # Level 6 setup
    level6 = MagnetsGame(3, 5)
    level6.place_item(1, 1, 'S')
    level6.place_item(1, 3, 'S')
    level6.place_item(0, 3, 'C')
    level6.place_item(1, 2, 'C')
    level6.place_item(2, 3, 'C')
    level6.place_item(2, 0, 'P')
    game_levels.add_level(level6)

    # Level 7 setup
    level7 = MagnetsGame(5, 4)
    level7.place_item(1, 0, 'S')
    level7.place_item(2, 0, 'S')
    level7.place_item(3, 1, 'S')
    level7.place_item(3, 2, 'S')
    level7.place_item(0, 0, 'C')
    level7.place_item(2, 3, 'C')
    level7.place_item(4, 3, 'C')
    level7.place_item(2, 1, 'P')
    game_levels.add_level(level7)

    # Level 8 setup
    level8 = MagnetsGame(3, 4)
    level8.place_item(1, 1, 'S')
    level8.place_item(1, 2, 'S')
    level8.place_item(0, 0, 'C')
    level8.place_item(0, 2, 'C')
    level8.place_item(2, 2, 'C')
    level8.place_item(2, 0, 'P')
    game_levels.add_level(level8)

     # Level 9 setup
    level9 = MagnetsGame(1, 7)
    level9.place_item(0, 5, 'S')
    level9.place_item(0, 3, 'S')
    level9.place_item(0, 6, 'C')
    level9.place_item(0, 1, 'C')
    level9.place_item(0, 0, 'P')
    game_levels.add_level(level9)

      # Level 10 setup
    level10 = MagnetsGame(4, 4)
    level10.place_item(2, 2, 'S')
    level10.place_item(2, 3, 'S')
    level10.place_item(3, 1, 'S')
    level10.place_item(3, 0, 'C')
    level10.place_item(1, 1, 'C')
    level10.place_item(1, 3, 'C')
    level10.place_item(3, 3, 'C')
    level10.place_item(0, 0, 'P')
    game_levels.add_level(level10)
    
     # Level 11 setup
    level11 = MagnetsGame(2, 5)
    level11.place_item(0, 0, 'S')
    level11.place_item(0, 4, 'S')
    level11.place_item(0, 1, 'C')
    level11.place_item(0, 2, 'C')
    level11.place_item(0, 3, 'C')
    level11.place_item(1, 2, 'R')
    game_levels.add_level(level11)
    
    
     # Level 12 setup
    level12 = MagnetsGame(5, 4)
    level12.place_item(0, 0, 'S')
    level12.place_item(1, 0, 'S')
    level12.place_item(4, 3, 'S')
    level12.place_item(2, 0, 'C')
    level12.place_item(4, 0, 'C')
    level12.place_item(4, 2, 'C')
    level12.place_item(3, 1, 'R')
    game_levels.add_level(level12)
   
    
     # Level 13 setup
    level13 = MagnetsGame(3, 6)
    level13.place_item(0, 0, 'S')
    level13.place_item(0, 4, 'S')
    level13.place_item(0, 5, 'S')
    level13.place_item(0, 3, 'C')
    level13.place_item(1, 1, 'C')
    level13.place_item(2, 1, 'C')
    level13.place_item(2, 3, 'R')
    game_levels.add_level(level13)

    
     # Level 14 setup
    level14 = MagnetsGame(4, 4)
    level14.place_item(3, 0, 'S')
    level14.place_item(0, 3, 'S')
    level14.place_item(2, 0, 'S')
    level14.place_item(1, 2, 'C')
    level14.place_item(2, 2, 'C')
    level14.place_item(2, 1, 'C')
    level14.place_item(1, 0, 'C')
    level14.place_item(3, 3, 'R')
    game_levels.add_level(level14)

    
     # Level 15 setup
    level15 = MagnetsGame(3, 5)
    level15.place_item(0, 0, 'C')
    level15.place_item(0, 1, 'S')
    level15.place_item(0, 2, 'C')
    level15.place_item(0, 3, 'S')
    level15.place_item(1, 4, 'C')
    level15.place_item(2, 4, 'C')
    level15.place_item(2, 2, 'R')
    level15.place_item(1, 2, 'P')
    game_levels.add_level(level15)

    
     # Level 16 setup
    level16 = MagnetsGame(5, 5)
    level16.place_item(1, 2, 'S')
    level16.place_item(3, 2, 'S')
    level16.place_item(4, 0, 'C')
    level16.place_item(4, 3, 'C')
    level16.place_item(0, 3, 'C')
    level16.place_item(0, 4, 'C')
    level16.place_item(2, 0, 'R')
    level16.place_item(2, 4, 'P')
    game_levels.add_level(level16)

    
     # Level 17 setup
    level17 = MagnetsGame(4, 4)
    level17.place_item(2, 0, 'S')
    level17.place_item(0, 2, 'S')
    level17.place_item(1, 3, 'C')
    level17.place_item(1, 1, 'C')
    level17.place_item(2, 2, 'C')
    level17.place_item(3, 1, 'C')
    level17.place_item(0, 0, 'R')
    level17.place_item(3, 3, 'P')
    game_levels.add_level(level17)
    
    
     # Level 18 setup
    level18 = MagnetsGame(5, 6)
    level18.place_item(0, 3, 'S')
    level18.place_item(2, 0, 'S')
    level18.place_item(2, 5, 'S')
    level18.place_item(1, 3, 'C')
    level18.place_item(2, 3, 'C')
    level18.place_item(2, 2, 'C')
    level18.place_item(2, 1, 'C')
    level18.place_item(4, 2, 'R')
    level18.place_item(4, 3, 'P')
    game_levels.add_level(level18)
 
   
     # Level 19 setup
    level19 = MagnetsGame(5, 5)
    level19.place_item(0, 1, 'S')
    level19.place_item(0, 3, 'S')
    level19.place_item(4, 1, 'S')
    level19.place_item(4, 3, 'S')
    level19.place_item(1, 0, 'C')
    level19.place_item(2, 1, 'C')
    level19.place_item(1, 4, 'C')
    level19.place_item(3, 0, 'C')
    level19.place_item(3, 2, 'C')
    level19.place_item(3, 4, 'C')
    level19.place_item(2, 2, 'R')
    level19.place_item(0, 2, 'P')
    game_levels.add_level(level19)
    
    
     # Level 20 setup
    level20 = MagnetsGame(5, 4)
    level20.place_item(0, 1, 'S')
    level20.place_item(0, 2, 'S')
    level20.place_item(4, 0, 'S')
    level20.place_item(0, 3, 'C')
    level20.place_item(1, 0, 'C')
    level20.place_item(2, 0, 'C')
    level20.place_item(3, 0, 'C')
    level20.place_item(4, 3, 'R')
    level20.place_item(4, 2, 'P')
    game_levels.add_level(level20)
    
    
     # Level 21 setup
    level21 = MagnetsGame(3, 4)
    level21.place_item(0, 1, 'S')
    level21.place_item(1, 1, 'S')
    level21.place_item(1, 2, 'S')
    level21.place_item(2, 1, 'C')
    level21.place_item(1, 0, 'C')
    level21.place_item(0, 2, 'C')
    level21.place_item(2, 3, 'R')
    level21.place_item(2, 0, 'P')
    game_levels.add_level(level21)
  
    
     # Levell22 setup
    level22 = MagnetsGame(4, 5)
    level22.place_item(0, 3, 'S')
    level22.place_item(0, 4, 'S')
    level22.place_item(3, 0, 'S')
    level22.place_item(1, 4, 'C')
    level22.place_item(2, 1, 'C')
    level22.place_item(1, 0, 'C')
    level22.place_item(0, 1, 'C')
    level22.place_item(3, 2, 'R')
    level22.place_item(0, 0, 'P')
    game_levels.add_level(level22)
    
    
    
     # Level 23 setup
    level23 = MagnetsGame(4, 5)
    level23.place_item(0, 3, 'S')
    level23.place_item(1, 4, 'S')
    level23.place_item(2, 0, 'S')
    level23.place_item(0, 2, 'C')
    level23.place_item(2, 3, 'C')
    level23.place_item(3, 2, 'C')
    level23.place_item(2, 2, 'C')
    level23.place_item(2, 1, 'C')
    level23.place_item(3, 4, 'P')
    level23.place_item(3, 2, 'R')
    game_levels.add_level(level23)
    
    
     # Level 24 setup
    level24 = MagnetsGame(5, 5)
    level24.place_item(0, 1, 'S')
    level24.place_item(1, 3, 'S')
    level24.place_item(3, 4, 'S')
    level24.place_item(0, 3, 'C')
    level24.place_item(2, 1, 'C')
    level24.place_item(2, 3, 'C')
    level24.place_item(4, 1, 'C')
    level24.place_item(4, 2, 'C')
    level24.place_item(3, 0, 'R')
    level24.place_item(1, 4, 'P')
    game_levels.add_level(level24)
    
    
     # Level 25 setup
    level25 = MagnetsGame(5, 4)
    level25.place_item(0, 0, 'C')
    level25.place_item(0, 3, 'C')
    level25.place_item(4, 0, 'C')
    level25.place_item(0, 0, 'S')
    level25.place_item(1, 2, 'S')
    level25.place_item(3, 2, 'S')
    level25.place_item(4, 3, 'S')
    level25.place_item(2, 0, 'C')
    level25.place_item(4, 2, 'C')
    level25.place_item(4, 1, 'C')
    level25.place_item(0, 3, 'R')
    level25.place_item(4, 0, 'P')
    game_levels.add_level(level25)
 




    return game_levels