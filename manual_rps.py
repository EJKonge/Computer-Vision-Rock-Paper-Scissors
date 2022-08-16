import random

class Rock_Paper_Scissors:

    def __init__(self):
        pass


    def get_computer_choice(self):
        choice_list = ['Rock','Paper','Scissors']
        computer_choice = random.choice(choice_list).lower()
        return computer_choice


    def get_user_choice(self):
        while True:

            user_choice = input('Please choose Rock, Paper or Scissors:').lower()
            if user_choice == 'rock' or user_choice == 'scissors' or user_choice == 'paper':
                return user_choice
            else:
                    print('Please choose one of the options selected')

    def get_winner(self, computer_choice,user_choice):
        if computer_choice == "rock" and user_choice == "paper":
            print("You won")
        elif computer_choice == "rock" and user_choice == "scissors":
            print("You lost")
        elif computer_choice == "paper" and user_choice == "rock": 
            print("You lost")
        elif computer_choice == "paper" and user_choice == "scissors":
            print("You won")
        elif computer_choice == "scissors" and user_choice == "rock": 
            print("You won")   
        elif computer_choice == "scissors" and user_choice == "paper": 
            print("You lost")
        else: 
            computer_choice == user_choice
            print("It's a tie")

def play():
        game = Rock_Paper_Scissors()
        computer_choice = game.get_computer_choice()
        user_choice = game.get_user_choice()
        game.get_winner(computer_choice,user_choice)

if __name__ ==  '__main__':
    choice_list = ['Rock','Paper','Scissors','Nothing']

    play()


