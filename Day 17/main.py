from data import question_data
from typing import List
from question_model import Question
import random
from quiz_brain import QuizBrain

question_bank: List[Question] = []  # Explicit type hint

for question in question_data:
    new_text = question["text"]
    new_answer = question["answer"]
    new_q = Question(new_text, new_answer)
    question_bank.append(new_q)

game_questions = QuizBrain(question_bank)
game_on = True

while game_on:
    new_question = game_questions.next_question(game_questions.question_number)

    # print(question_bank[0].text)
    # print(new_question.text)
    print(game_questions.question_number)
    print(new_question.answer)
    # print(new_q.text)
    game_answer= input(f"Q.{game_questions.question_number+1}: {new_question.text} (True/False)?").title()
    if not game_questions.check_answer(game_answer) or not game_questions.is_end():
        game_on = False

if not game_questions.is_end():
   print(f"Completed! Final Score: {game_questions.question_number+1}")
else:
    print(f"Wrong! Final Score: {game_questions.question_number}")
