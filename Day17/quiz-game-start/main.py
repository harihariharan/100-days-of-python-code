from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_bank.append(Question(questions["text"],questions["answer"]))
quiz = QuizBrain(question_bank)
while quiz.still_had_questions():
    quiz.next_question()   
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}.")    