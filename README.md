# CS Quiz App

A Python terminal quiz app that tests your computer science knowledge. Questions are randomized every run, with instant feedback and a final score at the end.

## Features
- Multiple choice questions covering core CS concepts
- Randomized question order every run
- Input validation — only accepts A, B, C, or D
- Instant right/wrong feedback after each question
- Final score summary at the end

## Technologies
- Python
- JSON for data storage
- `json` and `random` standard library modules

## Project Structure
```
quiz-app/
├── quiz.py           # Main program logic
└── questions.json    # Question bank
```

## How to Run

### Prerequisites
- Python 3 installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/hellypatelcu/quiz-app.git
   cd quiz-app
   ```

2. Run the program:
   ```bash
   python quiz.py
   ```

## How to Play
- A question will appear with 4 choices labeled A, B, C, and D
- Type your answer and press enter
- You'll be told immediately if you were right or wrong
- At the end you'll see your final score out of the total number of questions

## Topics Covered
- Data structures (stacks, queues)
- Time complexity and algorithms
- Python syntax
- Computer hardware
- Git and version control
- General programming concepts

## Adding Your Own Questions
Questions are stored in `questions.json`. To add your own, follow this format:
```json
{
    "question": "Your question here?",
    "choices": ["A. Option 1", "B. Option 2", "C. Option 3", "D. Option 4"],
    "answer": "A"
}
```
Add as many as you want; they'll be shuffled automatically every run.
