import Data
from Question_Model import Question
from Quiz_Brain import QuizBrain
question_bank = []
for q in Data.data1:
    new_q = Question(q["text"], q["answer"])
    question_bank.append(new_q)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
