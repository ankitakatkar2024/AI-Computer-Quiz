# stage 1 Code 

# print("Welcome to my computer quiz!")
# playing = input("Do you want to play? ")
# print(playing)

# if playing.lower() != "yes":
#     quit()

# print("Okay! Let's play :)")

# score = 0

# answer = input("What does CPU stand for? ")

# if answer.strip().lower() == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer is Central Processing Unit")

# answer = input("What does GPU stand for? ")

# if answer.strip().lower() == "graphics processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer is Graphics Processing Unit")

# answer = input("What does RAM stand for? ")

# if answer.strip().lower() == "random access memory":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer is Random Access Memory")

# answer = input("What does PSU stand for? ")

# if answer.strip().lower() == "power supply unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect! The correct answer is Power Supply Unit")

# print("You got " + str(score) + " questions correct!")
# print("You got " + str((score / 4) * 100) + "%.")


# Stage 2 Code
# Question list/dictionary        ↓
# for loop         ↓
# 20+ questions         ↓
# Random questions

# import random 
# print("Welcome to my computer quiz! ")
# playing = input("Do you want to play? ")
# if playing.strip().lower() != "yes":
#     quit()
# print("Okay! Let's play :) ")

# # Question bank
# questions = [
#     {
#      "question": "What does CPU stand for?",
#      "answer": "central processing unit"
#     },
#     {
#      "question": "What does GPU stand for?",
#       "answer": "graphics processing unit"
#     },
#     {
#      "question": "What does RAM stand for?",
#      "answer": "random access memory"
#     },
#     {
#     "question": "What does PSU stand for?",
#     "answer": "power supply unit"
#     },
#     {
#      "question": "What does SSD stand for?",
#      "answer": "solid state drive"
#     },
#     {
#      "question": "What does HDD stand for?",
#      "answer": "hard disk drive"
#     },
#     {
#      "question": "What does HTML stand for?",
#      "answer": "hypertext markup language"
#     },
#     {
#      "question": "What does CSS stand for?",
#      "answer": "cascading style sheets"
#     },
#     {
#      "question": "what does URL stand for?",
#      "answer": "uniform resource locator"
#     },
#     {
#      "question": "What does API stand for?",
#      "answer": "application programming interface",
#     },
#     {
#      "question": "What does IDE stand for?",
#      "answer": "integrated development environment"
#     },
#     {
#     "question": "What does BIOS stand for?",
#     "answer": "basic input output system"
#     },
#     {
#      "question": "What does LAN stand for?",
#      "answer": "local area network"
#     },
#     {
#      "question": "What does WAN stand for?",
#      "answer": "wide area network"
#     },
#     {
#      "question": "What does AI stand for?",
#      "answer": "artificial intelligence"
#     },
#     {
#      "question": "What does GUI stand for?",
#      "answer": "graphical user interface"
#     },
#     {
#      "question": "What does OS stand for?",
#      "answer": "operating system"   
#     },
#     {
#      "question": "What does SQL stand for?",
#      "answer": "structured query language"
#     }
# ]

# # Shuffle questions
# random.shuffle(questions)

# # Score
# score = 0

# # Ask questions

# for question in questions:
    
#     print()
#     print(question["question"])
    
#     answer = input("Your answer: ")
    
#     if answer.strip().lower() == question["answer"]:
#       print("Correct! ")
#       score += 1
#     else:
#       print("Incorrect!")
#       print("The correct answer is:", question["answer"])

# # Final result
# print()
# print("========== RESULT ==========")
# print("You got " + str(score) + " out of " + str(len(questions)) + " questions correct! ")
# percentage = (score / len(questions)) * 100
# print("You got " + str(round(percentage, 2)) + "%.")


# stage 3
# Multiple Choice (A/B/C/D) ← first
# Categories ← Hardware / Software / Networking / Programming, etc.

import random
import time
import msvcrt
import os
import json
from matplotlib.pylab import test
import matplotlib.pyplot as plt
from google import genai

SCORE_FILE = "high_scores.txt"

# ================= GEMINI =================

client = genai.Client()


print("================= Welcome to my computer quiz! ===============")

playing = input("Do you want to play? ")

if playing.strip().lower() != "yes":
    quit()

print()
print("Okay! Let's play :) ")


# ================= QUESTIONS =================

questions = [
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Processing Unit",
            "C. Central Peripheral Unit",
            "D. Computer Program Utility"
        ],
        "answer": "A",
        "category": "Hardware"
    },

    {
        "question": "What does GPU stand for?",
        "options": [
            "A. Graphics Processing Unit",
            "B. Graphical Processing Unit",
            "C. Graphics Peripheral Unit",
            "D. Graphical Peripheral Unit"
        ],
        "answer": "A",
        "category": "Hardware"
    },

    {
        "question": "What does USB stand for?",
        "options": [
            "A. Universal System Bus",
            "B. United Serial Bus",
            "C. Universal Serial Bus",
            "D. Universal Software Bus"
        ],
        "answer": "C",
        "category": "Hardware"
    },

    {
        "question": "What does HTML stand for?",
        "options": [
            "A. Hypertext Markup Language",
            "B. Hyperlink Markup Language",
            "C. Hypertext Machine Language",
            "D. Hyper Transfer Markup Language"
        ],
        "answer": "A",
        "category": "Programming"
    },

    {
        "question": "What does RAM stand for?",
        "options": [
            "A. Random Access Memory",
            "B. Read Access Memory",
            "C. Run Access Memory",
            "D. Random Application Memory"
        ],
        "answer": "A",
        "category": "Hardware"
    },

    {
        "question": "What does PSU stand for?",
        "options": [
            "A. Power System Unit",
            "B. Power Supply Unit",
            "C. Power Source Unit",
            "D. Power Storage Unit"
        ],
        "answer": "B",
        "category": "Hardware"
    },

    {
        "question": "What does OS stand for?",
        "options": [
            "A. Operator Source",
            "B. Operation System",
            "C. Operating System",
            "D. Operating Software"
        ],
        "answer": "C",
        "category": "Software"
    },

    {
        "question": "What does CSS stand for?",
        "options": [
            "A. Computer Style Sheets",
            "B. Cascading Style Sheets",
            "C. Creative Style System",
            "D. Computer Styling System"
        ],
        "answer": "B",
        "category": "Programming"
    },

    {
        "question": "What does SQL stand for?",
        "options": [
            "A. Structured Query Language",
            "B. Simple Query Language",
            "C. System Query Language",
            "D. Structured Question Language"
        ],
        "answer": "A",
        "category": "Programming"
    },

    {
        "question": "What does LAN stand for?",
        "options": [
            "A. Large Area Network",
            "B. Local Area Network",
            "C. Long Area Network",
            "D. Local Access Network"
        ],
        "answer": "B",
        "category": "Networking"
    },

    {
        "question": "What does URL stand for?",
        "options": [
            "A. Universal Resource Link",
            "B. Uniform Resource Locator",
            "C. Universal Reference Locator",
            "D. Uniform Reference Link"
        ],
        "answer": "B",
        "category": "Networking"
    },

    {
        "question": "What does AI stand for?",
        "options": [
            "A. Automated Information",
            "B. Artificial Intelligence",
            "C. Advanced Internet",
            "D. Automatic Intelligence"
        ],
        "answer": "B",
        "category": "Programming"
    },

    {
        "question": "Which of the following is a strong password?",
        "options": [
            "A. 123456",
            "B. password",
            "C. Ankita123",
            "D. T9#kL2@pQ7!"
        ],
        "answer": "D",
        "category": "Cyber Security"
    },

    {
        "question": "What does HTTPS provide?",
        "options": [
            "A. A faster internet connection",
            "B. Encrypted communication",
            "C. More computer storage",
            "D. A larger screen"
        ],
        "answer": "B",
        "category": "Cyber Security"
    }
]

# ================= AI QUESTION GENERATOR =================

def generate_questions(category, number_of_questions=10):

    prompt = f"""
Generate {number_of_questions} multiple-choice computer science quiz questions
about {category}.

For every question, provide:

1. A clear question
2. Exactly 4 options
3. One correct answer
4. The category

Return ONLY valid JSON in this exact format:

[
    {{
        "question": "Question here",
        "options": [
            "A. Option 1",
            "B. Option 2",
            "C. Option 3",
            "D. Option 4"
        ],
        "answer": "A",
        "category": "{category}"
    }}
]

Do not add explanations or markdown.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()
        
        if text.startswith("```json"):
            text =text[7:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip() 

        questions = json.loads(text)

        return questions

    except Exception as e:

        print()
        print("AI question generation failed.")
        print("Please try again later.")
        print("Error:", e)

        return []

# ================= CATEGORY MENU =================

categories = {
    "1": "Hardware",
    "2": "Software",
    "3": "Networking",
    "4": "Programming",
    "5": "Cyber Security",
    "6": "All Categories"
}


print()
print("================== Choose Category ==================")
print("1. Hardware")
print("2. Software")
print("3. Networking")
print("4. Programming")
print("5. Cyber Security")
print("6. All Categories")

category_choice = input("Enter the number of your choice: ").strip()


# Check category choice

if category_choice not in categories:
    print("Invalid choice!")
    quit()


selected_category = categories[category_choice]


# ================= SELECT QUESTIONS =================

# ================= SELECT QUESTIONS =================

# ================= GENERATE AI QUESTIONS =================

print()
print("Generating AI questions...")
print()

if selected_category == "All Categories":

    ai_category = "Hardware, Software, Networking, Programming, and Cyber Security"

else:

    ai_category = selected_category


selected_questions = generate_questions(
    ai_category,
    10
)


# Check if AI questions were generated

if not selected_questions:

    print()
    print("No AI questions were generated.")
    print("Please try again later.")
    quit()


random.shuffle(selected_questions)


score = 0


# ================= 50/50 LIFELINE =================

# Number of 50/50 lifelines available
fifty_fifty_remaining = 2

def use_fifty_fifty(question):

    correct_answer = question["answer"]

    incorrect_options = []

    for option in question["options"]:

        option_letter = option[0]

        if option_letter != correct_answer:

            incorrect_options.append(option)

    random_incorrect_option = random.choice(incorrect_options)

    remaining_options = []

    for option in question["options"]:

        option_letter = option[0]

        if option_letter == correct_answer:

            remaining_options.append(option)

        elif option == random_incorrect_option:

            remaining_options.append(option)

    return remaining_options


# ================= TIMER FUNCTION =================

def get_answer_with_timer(time_limit=10):

    answer = ""

    start_time = time.time()

    last_second = time_limit

    # Initial display
    print(f"Time remaining: {time_limit} seconds")
    print("Your answer: ", end="", flush=True)

    while True:

        elapsed_time = time.time() - start_time

        remaining_time = time_limit - int(elapsed_time)


        # ================= TIME UP =================

        if remaining_time <= 0:

            print()

            print("Time's up!")

            return None


        # ================= UPDATE TIMER =================

        if remaining_time != last_second:

            # Save current cursor position
            print("\033[s", end="")

            # Move cursor up to timer line
            print("\033[1A", end="")

            # Clear timer line
            print("\033[2K", end="")

            # Print updated timer
            print(
                f"Time remaining: {remaining_time} seconds",
                end=""
            )

            # Restore cursor to answer line
            print("\033[u", end="", flush=True)

            last_second = remaining_time


        # ================= CHECK KEYBOARD =================

        if msvcrt.kbhit():

            key = msvcrt.getch()


            # Enter key
            if key == b"\r":

                print()

                return answer


            # Backspace
            elif key == b"\x08":

                if answer:

                    answer = answer[:-1]

                    print("\b \b", end="", flush=True)


            # A, B, C or D
            else:

                try:

                    character = key.decode("utf-8").upper()

                    if character in ["A", "B", "C", "D"]:

                        answer += character

                        print(
                            character,
                            end="",
                            flush=True
                        )

                except UnicodeDecodeError:

                    pass


        time.sleep(0.05)
# ================= SAVE HIGH SCORE =================

def save_score(percentage):

    with open(SCORE_FILE, "a") as file:

        file.write(f"{percentage:.2f}\n")
        
# ================= DISPLAY HIGH SCORES =================

def show_high_scores():

    if not os.path.exists(SCORE_FILE):

        print("No high scores available yet.")

        return

    with open(SCORE_FILE, "r") as file:

        scores = []

        for line in file:

            scores.append(float(line.strip()))

    scores.sort(reverse=True)

    print()
    print("========== 🏆 HIGH SCORES ==========")

    for position, score in enumerate(scores[:5], start=1):

        print(f"{position}. {score:.2f}%")

    print()
    
    # ================= SCORE GRAPH =================

def show_score_graph():

    if not os.path.exists(SCORE_FILE):

        print("No scores available for graph.")

        return

    with open(SCORE_FILE, "r") as file:

        scores = []

        for line in file:

            scores.append(float(line.strip()))

    if not scores:

        print("No scores available for graph.")

        return

    attempts = list(range(1, len(scores) + 1))

    plt.figure(figsize=(8, 5))

    plt.plot(
        attempts,
        scores,
        marker="o"
    )

    plt.title("Quiz Score Progress")

    plt.xlabel("Quiz Attempt")

    plt.ylabel("Score (%)")

    plt.ylim(0, 100)

    plt.xticks(attempts)

    plt.grid(True)

    plt.show()


# ================= QUIZ LOOP =================

for question in selected_questions:

    print()
    print("--------------------------------")
    print(question["question"])
    print("--------------------------------")

    # Show all options first
    options = question["options"]

    for option in options:

        print(option)

    print()

    # ================= 50/50 LIFELINE =================

    if fifty_fifty_remaining > 0:

        print(
            f"50/50 Lifeline available "
            f"({fifty_fifty_remaining} remaining)"
        )

        lifeline_choice = input(
            "Do you want to use 50/50? (yes/no): "
        ).strip().lower()

        if lifeline_choice == "yes":

            options = use_fifty_fifty(question)

            fifty_fifty_remaining -= 1

            print()
            print("50/50 Lifeline used!")
            print(
                f"Lifelines remaining: "
                f"{fifty_fifty_remaining}"
            )

            print()
            print("Remaining options:")

            for option in options:

                print(option)

            print()

    else:

        print("50/50 Lifeline: Not available")

        print()


    # ================= TIMER =================

    answer = get_answer_with_timer(10)


    # ================= CHECK ANSWER =================

    if answer is None:

        print(
            "The correct answer is:",
            question["answer"]
        )


    elif answer.strip().upper() == question["answer"]:

        print("Correct!")

        score += 1


    else:

        print("Incorrect!")

        print(
            "The correct answer is:",
            question["answer"]
        )
# ================= FINAL SCORE =================

total_questions = len(selected_questions)

percentage = (score / total_questions) * 100

print()
print("========================================")
print("             QUIZ COMPLETED")
print("========================================")

print(f"Correct Answers: {score}")
print(f"Total Questions: {total_questions}")
print(f"Percentage: {percentage:.2f}%")

# Save score
save_score(percentage)

print()
print("Score saved!")

# Show high scores
show_high_scores()

# Show score graph
show_score_graph()