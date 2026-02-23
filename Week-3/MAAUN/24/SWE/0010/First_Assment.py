# Abdallah Ali Muhammad Thani
# maaun/24/SWE/0010
# the list od dectionary that contains the questions, options and answers for the quiz
test =[{
    "quitstions": "what is the capital of Nigeria?",
    "options": ["A) Lagos", "B) Abuja", "C) Kano"],
    "answer": "B"
},
       {
    "quitstions": "what is the fullmeaning of HTML?",
    "options": ["A) Hyper Text Markup Language", "B) High Tech Modern Language", "C) Home Tool Markup Language"],
    "answer": "A"
       },

       {"quitstions": "what is the fullmeaning of CSS?",
        "options": ["A) Cascading Style Sheets", "B) Computer Style Sheets", "C) Creative Style Sheets"],
        "answer": "A"},

        {"quitstions": "what is the fullmeaning of JS?",
         "options": ["A) JavaScript", "B) JavaSource", "C) JustScript"],
         "answer": "A"}]
# function to get the user input and convert it to uppercase for comparison with the correct answer
def user_input():
    user_answer = input("Enter your answer (A, B, or C): ").upper()
    return user_answer
# function to calculate the percentage score and determine if the user passed or failed based on a passing threshold of 50%
def calculate_percentage(score, max_score):
    
    percentage = (score / max_score) * 100
    if percentage >= 50:
        print(f"Congratulations, you passed with {percentage}%!")
    else:
        print(f"Sorry, you failed with {percentage}%.")
    return percentage
score = 0
max_score = len(test) * 25
# loop through the questions, display them to the user, get their answers, and calculate the score based on correct answers

for q in test:
    print("\n" + q["quitstions"])
    for option in q["options"]:
        print(option)
        
    user_answer = user_input()
    
    if user_answer == q["answer"]:
        print("Correct!")
        score += 25
    else:
        print("Incorrect.")

calculate_percentage(score, max_score)