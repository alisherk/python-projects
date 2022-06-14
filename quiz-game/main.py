from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
   
    text = question['text'] 

    answer = question['answer']  

    new_question = Question(text, answer)

    question_bank.append(new_question)
   

quiz = QuizBrain(question_bank)

while(quiz.still_has_questions()): 
    quiz.next()


print("You have completed the quize")
print(f"Your final score was: {quiz.score}/{quiz.question_number} ")