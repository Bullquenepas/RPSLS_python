#Display welcome message // display rules of game
from human import Human
from ai import Ai

class Game:
    def __init__(self):
        pass

    def welcome(self):
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
    #greeting_message = welcome()

    # def display_gesture_options(self): 
    #     print(self.gesture)
    # display_gesture = display_gesture_options()

    def compare_gestures(self):
        
        if self.player_one == self.gesture[0]:
            if self.player_two == self.gesture[0]:
                print('It is a tie.')
            
            elif self.player_two == self.gesture[1]:
                self.player_two.player_score += 1

            

    def game_select(self):
        print("Please select single Press 1, or multiplayer press 2")
        self.game_mode = input("")


        if self.game_mode == "1":
            print("You have selected singleplayer.")
            self.player_one = Human() 
            self.player_two = Ai() 
            
        
        elif self.game_mode == "2":
            print("You have selected Multiplayer")
            self.player_one = Human() 
            self.player_two = Human() 
            

        else:
            print("You have not selected a proper game mode")
            self.game_select()




    
   
