
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