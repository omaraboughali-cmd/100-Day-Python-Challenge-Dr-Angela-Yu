class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer_q = input(f"Q{self.question_number+1} is {current_question.question} ? ") 
        if answer_q.lower() == current_question.answer.lower():
            print("correct")
            self.score += 1
        else:
            print("wrong")
            print(f"the correct ans is {current_question.answer}")
        print(f"score is {self.score}/{self.question_number+1}")        
        self.question_number += 1 
    def still_has_question(self):               
        if self.question_number < len(self.question_list):
            return True
        else:
            return False