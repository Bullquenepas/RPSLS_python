import re
from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.chosen_gesture = self.gesture[0:4]
        user_input = (input('Pick a gesture '))
        if user_input == self.gesture[0]:
            print('You chose rock!')
            return self.gesture[0]
        
        if user_input == self.gesture[1]:
            print('You chose paper!')
            return self.gesture[1]

        if user_input == self.gesture[2]:
            print('You chose scissors')
            return self.gesture[2]

        if user_input == self.gesture[3]:
            print ('You chose lizard!')
            return self.gesture[3]

        if user_input == self.gesture[4]:
            print ('You chose spock!')
            return self.gesture[4]

        else:
            print('not a valid option try again')
        
    
    
    
    