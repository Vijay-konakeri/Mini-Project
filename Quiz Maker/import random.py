import json
import random

with open("questions.json", "r") as f:
    data = json.load(f)
    questions = data["questions"]

quiz_questions = random.sample(questions, 10)

user_answers = []
for i, question in enumerate(quiz_questions):
    print(f"\nQuestion {i+1}: {question['question']}")
    for j, option in enumerate(question['options']):
        print(f"{j+1}. {option}")
    answer_index = int(input("Enter the number of your answer: ")) - 1
    if question['options'][answer_index] == question['answer']:
        print("Correct!")
        user_answers.append({'question': question['question'], 'answer': question['options'][answer_index], 'correct': True})
    else:
        print(f"Wrong! The correct answer is {question['answer']}")
        user_answers.append({'question': question['question'], 'answer': question['options'][answer_index], 'correct': False})

print("\nQuiz Result:")
num_correct = sum(answer['correct'] for answer in user_answers)
print(f"You answered {num_correct} out of {len(quiz_questions)} questions correctly.\n")

print("Questions Summary:")
for i, answer in enumerate(user_answers):
    print(f"{i+1}. {answer['question']}")
    print(f"Your answer: {answer['answer']}")
    if answer['correct']:
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is: {answer['correct']}")
    print()
    
score = (num_correct / len(quiz_questions)) * 100
print(f"You scored {score:.2f}%") 
