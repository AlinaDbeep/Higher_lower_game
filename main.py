#Hi, this is the Higher Lower game. 
#The rules are simple: you guess all the comparisons, you win. 
#the data may be a bit old, yet you may try out the game
#Good luck!!!


logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from data import data
from os import system, name
from time import sleep

def clear():
    _ = system('clear')


def game():
    number = 0
    game_off = False
    while not game_off:
        sleep(0)
        clear()
        if number == 50:
            print("Congrats! You won the game!!!")
        else:
            a = data[number]
            score = number
            print(logo)
            print("Compare A: " + a["name"] + ", a(n) " + a['description'] + ", from " + a["country"])
            number += 1
            b = data[number]
            print(vs)
            print("Against B: " + b["name"]+ ", a(n) " + b['description'] + ", from " + b["country"])
            answer = input("Who has more followers? Type 'A' or 'B': ").lower()
            if answer == 'a' and a["follower_count"] > b["follower_count"]:
                print("You are correct")
            elif answer == 'b' and a["follower_count"] < b["follower_count"]:
                print("You are correct")
            else:
                print("You lost")
                again = input(f"Your score is {score}. Wanna play again? Type 'y' or 'n': ")
                if again == 'y':
                    game()
                else:
                    print("It was nice seeing you! Bye!")
                    game_off = True
                    
    
game()
        