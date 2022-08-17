import cv2
from keras.models import load_model
import numpy as np
import random
import time

class camera_rps:

    def __init__(self):
        self.options = ["rock", "scissors", "paper", "nothing"]
        self.model = load_model('keras_model.h5')
        self.user_wins = 0
        self.computer_wins = 0

    def get_prediction(self):
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        print("\npress s to start the timer")
        while True: 
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        countdown = 4
        predict_once = 0
        start = time.time()
        while True: 
            ret, frame = cap.read()
            if countdown > 1:
                cv2.putText(frame, str(countdown - 1), (236, 316), cv2.FONT_HERSHEY_SIMPLEX, 8, (255, 255, 255), 20)
            cv2.imshow('frame', frame)  
            if time.time() > start - countdown + 5 and countdown > 0:
                if countdown > 1:
                    print(countdown - 1)
                countdown -= 1
            elif countdown == 0 and predict_once == 0:
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = self.model.predict(data)
                predict_once = 1
                print("\nPress r to see results for this round")
            if cv2.waitKey(1) & 0xFF == ord('r') and countdown == 0:
                break
        return prediction

    def get_computer_choice(self):
        return random.choice(self.options[:-1])

    def get_user_choice(self, prediction):
        choice = np.argmax(prediction)
        print("You chose " + self.options[choice])
        return self.options[choice]

    def get_winner(self, computer_choice,user_choice):
        if (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
            return 1
        elif (computer_choice == "rock" and user_choice == "scissors") or (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors" and user_choice == "paper"):
            return -1
        else: 
            computer_choice == user_choice
            return 0

    def play(self):
        print("\nWelcome to a game of Computer Vision Rock Paper Scissors\nFirst to win 3 rounds, takes the trophy\nGood Luck")
        while self.user_wins < 3 and self.computer_wins < 3:
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice(self.get_prediction())
            winner = self.get_winner(computer_choice, user_choice)
            print(user_choice.lower() + " : " + computer_choice.lower() +"\nComputer chose" + " " + computer_choice.lower())
            if winner == 1:
                self.user_wins += 1
                print("You won!\n")
            elif winner == -1:
                print("You lost!\n")
                self.computer_wins += 1
            elif winner == 0: 
                print("It is a tie!\n")
            else:
                print("No choice was detected.")
            print("The score is " + str(self.user_wins) + " : " + str(self.computer_wins))
        if self.user_wins == 3:
            print("You won the match!")
        else:
            print("You lost the match!")
        cv2.destroyAllWindows()
if __name__ == "__main__":
    rps = camera_rps()
    rps.play()