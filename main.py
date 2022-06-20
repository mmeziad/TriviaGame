from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # print(question["text"])
    # print(question["answer"])
    question_bank.append(Question(question["text"], question["answer"]))

# for i in question_bank:
#     print(i.text)

quiz = QuizBrain(question_bank)

while quiz.still_has_q() is True:
    quiz.next_question()

print(f"\nYou have completed the quiz, your final score is {quiz.score}/{len(question_bank)}.")
