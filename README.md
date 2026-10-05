# 🧠 AI Computer Quiz

An AI-powered Computer Science Quiz application built using **Python, Tkinter, Gemini AI, and Matplotlib**.

The application generates computer science multiple-choice questions using Google's Gemini AI and provides an interactive GUI-based quiz experience with a timer, 50/50 lifeline, scoring system, high scores, and progress graph.

---

## 🚀 Features

- 🤖 **AI-Generated Questions**
  - Uses Google Gemini AI to generate quiz questions dynamically.
  - Generates 10 multiple-choice questions for each quiz.

- 📚 **Multiple Categories**
  - Hardware
  - Software
  - Networking
  - Programming
  - Cyber Security
  - All Categories

- ⏱️ **15-Second Timer**
  - Each question has a 15-second time limit.
  - If the timer reaches zero, the question is automatically skipped.

- 🎯 **50/50 Lifeline**
  - Provides two 50/50 lifelines.
  - Removes two incorrect options from a question.

- 📊 **Score Calculation**
  - Displays the number of correct answers.
  - Calculates the final percentage score.

- 🏆 **High Score System**
  - Saves quiz scores locally.
  - Displays the top 3 scores.

- 📈 **Progress Graph**
  - Displays quiz performance using a graph.
  - Shows score percentage across quiz attempts.

- 🎨 **Modern GUI**
  - Built using Python Tkinter.
  - Dark-themed user interface.
  - Interactive buttons and visual feedback.

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter** – GUI development
- **Google Gemini API** – AI question generation
- **Matplotlib** – Score progress graph
- **JSON** – Processing AI-generated questions
- **OS** – File handling
- **Random** – Question and option randomization
- **Time** – Timer functionality

---

## 📂 Project Structure

```text
AI-Computer-Quiz/
│
├── quiz_gui.py
├── Quiz_game.py
├── gemini_test.py
├── check_models.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── high_scores.txt