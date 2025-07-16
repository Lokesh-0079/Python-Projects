# OBJECTIVES
"""
1 Make questions
2 Create a function to check for the answers from user
3 if correct increment the score, else correct the user
4 if player quits say thanks for playing and display the score

"""
import random

questions={
    " What is the keyword to define a function in python ? " : "def",
    " What does len() function returns ? " : "length",
    " What is the keyword to use a module in python ? " : "import",
    " What is the extension store Python files ? " : ".py",
    " What is the symbol used for comments in python ? " : "#",
    " Who invented python ? " : "Guido Van Rossum",
    " What does OOP stand for ? " : "Object Oriented Programming",
    " When was python published ? " : "1991",
    " Which data type is used to store a sequence of characters in python ? " : "str"
}

def game():
    que_list=list(questions.keys())
    total_que=5
    score=0

    selected_que=random.sample(que_list,total_que)
    for idx, question in enumerate(selected_que, start=1):
        print(f"{idx}. {question}")

        user_answer = input("Enter your answer (q to quit) : ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct Answer!\n")
            score += 1
        elif user_answer == "q":
            print(f"You exited the game with {score}/{total_que} points")
            break
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.\n")


    print("\nThank you for playing!")
    print(f"Your total score is: {score}/{total_que}")


game()
