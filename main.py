from question_model import Question 
from data import question_data 
from quiz_brain import Quiz
from logo import logo
print(logo)
question_bank=[]
for i in question_data:
    obj=Question(i["text"],i["answer"])
    question_bank.append(obj) 
obj1=Quiz(question_bank)
while obj1.still_has_questions():
    obj1.next_question()

print("You've completed the quiz")
print(f"Your final score was :{obj1.score}/{obj1.question_number}")