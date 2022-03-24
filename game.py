#Display welcome message // display rules of game
from human import Human
from ai import Ai

class Game:
    def __init__(self):
        pass

    def welcome():
        print('Welcome to a wonderful game of chance!')
        print('Each player picks a variable and reveals it at the same time. The winner is the one who defeats the others. In a tie, the process is repeated until a winner is found.')
        print('You can choose between Rock Paper Scissors Lizard Spock')
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
    greeting_message = welcome()

    # def display_gesture_options(self): 
    #     print(self.gesture)
    # display_gesture = display_gesture_options()

    def compare_gestures(self):
        pass

    def game_select(self):
        print("Please select single Press 1, or multiplayer press 2")
        self.game_mode = input("")


        if self.game_mode == "1":
            print("You have selected singleplayer.")
            player_one = () 
            player_one.player_name()
            player_two = Ai() 
            player_two.player_name()
        
        if self.game_mode == "2":
            print("You have selected Multiplayer")
            player_one = Human() 
            player_one.player_name()
            player_two = Human() 
            player_two.player_name()

        else:
            print("You have not selected a proper game mode")
            self.game_select()




    
   
