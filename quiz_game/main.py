import data
import question_model
import quiz_brain

q_bank = []
for question in data.question_data:
    q = question_model.Question(question["text"], question["answer"] )
    q_bank.append(q)
        

qb = quiz_brain.QuizBrain(q_bank) 
while qb.still_has_question():
    qb.next_question()
    