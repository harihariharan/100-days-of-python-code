class QuizBrain():

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self,actual_answer,user_answer):
        if actual_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")   
        print(f"The correct answer was: {actual_answer}")    
        print(f"Your current score is: {self.score}/{self.question_number}.") 
        print("\n")

    def still_had_questions(self):
        return len(self.question_list) > self.question_number 

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(current_question.answer,answer)
        
