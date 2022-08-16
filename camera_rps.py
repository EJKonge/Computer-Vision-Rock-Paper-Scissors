import cv2
from keras.models import load_model
import numpy as np
import random
import time

class RPS:

    def __init__(self):
        self.computer_choice = random.choice(self.choice_list)
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.user_score = 0
        self.computer_score = 0
        pass

    def get_computer_choice(self):
        choice_list = ['Rock','Paper','Scissors']
        computer_choice = random.choice(choice_list).lower()
        return computer_choice

    def get_prediction(self):
        
        if self.prediction[0][0] > 0.8:
            user_choice = 'rock'
        elif self.prediction[0][1] > 0.8:
            user_choice = 'paper'
        elif self.prediction[0][2] > 0.8:
            user_choice = 'scissors'
        elif self.prediction[0][3] > 0.8:
            user_choice = 'nothing'
        else:
            user_choice = 'No user choice detected'
        return user_choice
    
    def timer(self):

        start_time = time.time()
        print("You have 5 seconds to choose.")

        while True:

            elapsed_time = time.time() - start_time
            remaining_time = 5 - elapsed_time
            #print("You have {:.0f} seconds left".format(remaining_time))
            
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window

            if (remaining_time < 0):
                user_choice = self.get_prediction(prediction)
                computer_choice = self.get_computer_choice()
                print("You chose: {}".format(user_choice))
                print("Computer choice was: {}".format(computer_choice))
                self.get_winner(computer_choice, user_choice)

                print("You have 5 seconds to choose.")
                start_time = time.time()
                remaining_time = 5
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                    
        # After the loop release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

    