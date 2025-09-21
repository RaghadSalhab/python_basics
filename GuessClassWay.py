import random

class GuessGame:

    instance =None

    def __new__(cls, *args, **kwds):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance

    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.attempts=[]

    def generate_random(self,min,max):
        return random.randint(min,max)
    
    def guess_num(self,num):
        self.attempts.append(num)
        self.trail_count+=1

        if(self.target==num):
            print(f'YOU GUESS IT GOOD! its {self.target} and the number of trail is {self.trail_count} ')
            return True
        elif(self.target>num):
            print('its greater than that ! try again: ')
        else:
            print('its less than that ! try again: ')

        return False

    def play(self):
        self.target=self.generate_random(self.min,self.max)
        self.trail_count=0
        print(f'the guessing num is : { self.target}')
        
        print('start a new game')
        while True:
            try:
                num = int(input('enter number: '))
                if self.guess_num(num):
                    break
            except ValueError:
                print('please enter integer number')

    def __repr__(self):
        return(f'target({self.target}) , trail_count({self.trail_count})')
    
    def __iter__(self):
        return iter(self.attempts)

p=GuessGame(1,100)
while True:
    choice=input('do you what to play (yes, no): ')
    if choice.lower()=='yes':
        p.play()
    else:
        print('finish the program')
        break
