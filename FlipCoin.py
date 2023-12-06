import random
import time
def flip_coin():
    print("Hello the game has started GoodLuck")
    time.sleep(0.5)
    computer = random.choice(["heads","tails"]).lower()
    print("The coin has been flipped")
    time.sleep(1)
    user = str(input("""Enter your guess
            Heads or Tails ==>  """)).lower()
    if user == computer:
        print("Good choice it was",user.upper())
    else:
        print("You lost but it's ok it was",computer.upper())
#----------------------------------------------------------------
    again = str(input("Do you want to play again?"))
    if again.lower() == "yes":
        flip_coin()
    else:
        print("see you later👋")

flip_coin()