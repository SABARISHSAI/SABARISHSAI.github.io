from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    new_q = Question(text,answer)
    question_bank.append(new_q)

q = QuizBrain(question_bank)
while q.still_has_question():
    q.next_question()
q.display_mark()
