import random

class GuessGame:

    def __init__(self,min,max):
        self.target=self.generate_random(min,max)
        self.trail_count=0

    def generate_random(self,min,max):
        return random.randint(min,max)
    
    def guess_num(self,num):
        if(self.target==num):
            print(f'YOU GUESS IT GOOD! its {self.target} and the number of trail is {self.trail_count} ')
            return True
        elif(self.target>num):
            print('its greater than that ! try again: ')
        else:
            print('its less than that ! try again: ')

        self.trail_count+=1
        return False

    def play(self):
        while True:
            try:
                num = int(input('enter number: '))
                if self.guess_num(num):
                    break
            except ValueError:
                print('please enter integer number')

    def __repr__(self):
        return(f'target({self.target}) , trail_count({self.trail_count})')

p=GuessGame(1,100)
print(p)
p.play()
        