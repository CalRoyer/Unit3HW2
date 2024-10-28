#Treasure Quest Text Adventure Game 
import random

intro_art = '''
 _______ __   __ _______                                             
|       |  | |  |       |                                            
|_     _|  |_|  |    ___|                                            
  |   | |       |   |___                                             
  |   | |       |    ___|                                            
  |   | |   _   |   |___                                             
 _______|_______|________ _______ _______ __   __ ______   _______   
|       |    _ | |       |   _   |       |  | |  |    _ | |       |  
|_     _|   | || |    ___|  |_|  |  _____|  | |  |   | || |    ___|  
  |   | |   |_||_|   |___|       | |_____|  |_|  |   |_||_|   |___   
  |   | |    __  |    ___|       |_____  |       |    __  |    ___|  
  |   | |   |  | |   |___|   _   |_____| |       |   |  | |   |___   
 _______|___| ___________________________|_______|___|  |_|_______|  
|       |  | |  |       |       |       |                            
|   _   |  | |  |    ___|  _____|_     _|                            
|  | |  |  |_|  |   |___| |_____  |   |                              
|  |_|  |       |    ___|_____  | |   |                              
|      ||       |   |___ _____| | |   |                              
|____||_|_______|_______|_______| |___|                              '''

name = input("What is your name?:")


print(intro_art)

def intro():
    print(f"Welcome to the Treasure Quest {name}!")
    print("You are an adventurer seeking the hidden treasure in the Lost Forest.")
    print("Along the way, you will face choices and challenges. Choose wisely!")
    print("Let's begin your adventure!")

choice = input("Do you choose the 'well-traveled' path or the 'overgrown' path?(well-traveled/overgrown) ").strip().lower()
    
if choice == 'well-traveled':
        print("\nYou take the well-traveled path. It's easier to walk, but you wonder if it might lead to traps.")
elif choice == 'overgrown':
        print("\nYou push through the overgrown path. It's tough going, but you feel it might lead to something hidden.")
else:
        print("\nYou hesitate and can't decide. Suddenly, a gust of wind pushes you toward the overgrown path.")
        choice = 'overgrown'