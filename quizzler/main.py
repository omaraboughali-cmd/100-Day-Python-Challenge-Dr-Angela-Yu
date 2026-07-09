from question_model import Question
from quiz_brain import QuizBrain
from ui import UI
import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()['results']

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

brain = QuizBrain(question_bank)

quiz_ui = UI(brain)