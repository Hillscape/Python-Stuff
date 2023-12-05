import random
import time
class Rock_Paper_Scissors():
    def Start():
        while True:
            print("Hello welcome to the RPS Game ")
            time.sleep(1)
            print("""Press enter one of these options to continue
                1.Rock
                2.Paper
                3.Scissors""")
            choices = ["Rock", "Paper", "Scissors"]
            user_choice = int(input("Enter from 1-3 : "))
            computer_choice = random.randint(1,3)
            time.sleep(0.5)
            print("you chose", choices[user_choice-1])
            time.sleep(0.5)
            print("computer chose",choices[computer_choice-1])
            if user_choice == computer_choice:
                print("Draw")
            elif (user_choice == 1 and computer_choice == 3) or \
                (user_choice == 2 and computer_choice == 1) or \
                (user_choice == 3 and computer_choice == 2):
                print("You win!")
            else:
                print("computer wins!")
        # ------------------------------------------------------------------------------
            play_again = input("Do you want to play again? yes/no: ")
            if play_again.lower() == "yes":
                time.sleep(0.5)
                continue
            else:
                print("Thank you for playing ")
    Start()