#!/user/bin/env phython

import random

def main():
    """Start guessing genre music between hip hop,jozz,rock,disco,classical and kpop."""
    print("Guess the genre music between hip hop,jozz,rock,disco,classical and kpop")
    
    music = ("hip hop" , "jozz" , "rock" , "disco", "classical" , "kpop")
    
    x = random.choice(music)
    guess = None
    
    while x !=guess:
        
        guess = str(input("pick a genre music:"))
        
        if x == guess:
            print("You got it ><!!.")
            
        else:
            print("You can do it try agian.")
            print("trust yourself.")
            print(":)")
            
main()  