#QUIZ_GENERATED_BY_PYTHON
#Task 5

import random
questions = {
    "What is the capital of France?": "Paris",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the capital of Japan?": "Tokyo",
    "What is the chemical symbol for gold?": "Au",
    "Who is known as the father of modern physics?": "Albert Einstein",
}

def load_quiz_questions():
    return questions

def present_quiz_questions(quiz_questions):
    score = 0
    total_questions = len(quiz_questions)
    
    print("\nWelcome to the Quiz Game!")
    print("You will be asked multiple-choice or fill-in-the-blank questions on a specific topic.")
    print("Let's get started!\n")

    for question, answer in quiz_questions.items():
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")

        print()

    return score, total_questions

def display_final_results(score, total_questions):
    percentage = (score / total_questions) * 100

    print("\nQuiz Complete!")
    print(f"Your final score is: {score}/{total_questions}")
    print(f"Your performance: {percentage:.2f}%")

def play_quiz_game():
    play_again = 'yes'

    while play_again.lower() == 'yes':
        quiz_questions = load_quiz_questions()
        score, total_questions = present_quiz_questions(quiz_questions)
        display_final_results(score, total_questions)

        play_again = input("Do you want to play again? (yes/no): ")

    print("Thank you for playing the Quiz Game!")

if __name__ == "__main__":
    play_quiz_game()
