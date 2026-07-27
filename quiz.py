#imports 
import json
import random
import os

score = 0

# open the file and decode the JSON data
with open('questions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

#shuffle data so the questions are in a random order
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
        print()
        user_answer = input("Your answer (A/B/C/D): ")
        if user_answer in valid_answers:
            break
        else:
            print("Invalid answer. Please enter A, B, C, or D.")

    # check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['answer']}")

#print final score
print()
print(f"Your final score is: {score}/{len(data)}")

#ask the user for their name to save their score
print()
name = input("Enter your name to save your score: ")

# load existing scores or start fresh if file doesnt exist or is empty
if os.path.exists('scores.json') and os.path.getsize('scores.json') > 0:
    with open('scores.json', 'r', encoding='utf-8') as file:
        scores = json.load(file)
else:
    scores = []

#check if the user already has a score saved
name_found = False

for entry in scores:
    if entry["name"] == name:
        name_found = True
        #update the score if the new score is higher
        if score > entry["score"]:
            entry["score"] = score


#add new score if the user doesn't have a score saved yet
if not name_found:
    scores.append({"name": name, "score": score})

#save it back into the file
with open('scores.json', 'w', encoding='utf-8') as file:
    json.dump(scores, file, indent=4)

#tell the user the score was saved
print(f"Score saved for {name}.")
print()

#sort the scores in descending order
scores.sort(key=lambda x: x["score"], reverse=True)

#print score board
print("Score Board:")
print()
for entry in scores:
    print(f"{entry['name']}: {entry['score']}")
print()