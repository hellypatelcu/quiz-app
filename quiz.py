#imports 
import json
import random

score = 0

# open the file and decode the JSON data
with open('questions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

#shuffle the questions so they appear in a random order each time the quiz is run
with open('questions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

random.shuffle(data)

# print the questions
for question in data:
    print()
    print(question["question"])

    #print the question
    for choice in question["choices"]:
        print(choice)

    #print the choices
    valid_answers = "A B C D".split()

    #error handling for invalid answers
    while True:
        user_answer = input("Your answer (A/B/C/D): ")
        if user_answer in valid_answers:
            break
        else:
            print("Invalid answer. Please enter A, B, C, or D.")

            print(f"Valid answers are: {valid_answers}")
            print(f"You typed: {user_answer}")

    # check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['answer']}")

#print final score
print(f"Your final score is: {score}/{len(data)}")