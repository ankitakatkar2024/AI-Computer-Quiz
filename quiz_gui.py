import random
import time
import os
import json
import tkinter as tk
from dotenv import load_dotenv
from tkinter import messagebox
import matplotlib.pyplot as plt
from google import genai

load_dotenv()
SCORE_FILE = "high_scores.txt"
client = genai.Client()

# Modern High-End Color Palette
BG_COLOR = "#090d16"         # Deep Obsidian Background
CARD_BG = "#131c2e"          # Elevated Surface Card
TEXT_COLOR = "#f8fafc"       # Crisp Bright White
TEXT_MUTED = "#94a3b8"       # Soft Gray for subtitles
ACCENT_COLOR = "#6366f1"     # Vibrant Indigo Accent
BTN_BG = "#1e293b"           # Button Default Background
BTN_HOVER = "#3b82f6"        # Button Hover Color (Bright Blue)
CORRECT_COLOR = "#10b981"    # Emerald Green
WRONG_COLOR = "#f43f5e"      # Rose Red
DISABLED_BG = "#0f172a"      # Disabled Item Background
DISABLED_FG = "#334155"      # Disabled Item Text

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced AI Python Quiz")
        self.root.geometry("820x680")
        self.root.config(bg=BG_COLOR)
        self.root.resizable(False, False)

        # Quiz State
        self.questions = []
        self.current_question_index = 0
        self.score = 0
        self.fifty_fifty_remaining = 2
        self.time_left = 15
        self.timer_id = None

        self.create_start_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ================= 1. START & CATEGORY SCREEN =================
    def create_start_screen(self):
        self.clear_window()

        title_label = tk.Label(
            self.root, text="⚡ AI Computer Science Quiz", 
            font=("Segoe UI", 24, "bold"), bg=BG_COLOR, fg=TEXT_COLOR
        )
        title_label.pack(pady=35)

        card = tk.Frame(self.root, bg=CARD_BG, padx=40, pady=30)
        card.pack(pady=10, padx=50, fill="x")

        tk.Label(
            card, text="Select Challenge Category:", 
            font=("Segoe UI", 14, "bold"), bg=CARD_BG, fg=TEXT_COLOR
        ).pack(anchor="w", pady=(0, 15))

        self.category_var = tk.StringVar(value="Hardware")
        categories = ["Hardware", "Software", "Networking", "Programming", "Cyber Security", "All Categories"]

        for cat in categories:
            rb = tk.Radiobutton(
                card, text=cat, variable=self.category_var, value=cat,
                font=("Segoe UI", 12), bg=CARD_BG, fg=TEXT_COLOR, selectcolor=BG_COLOR,
                activebackground=CARD_BG, activeforeground=TEXT_COLOR, cursor="hand2"
            )
            rb.pack(anchor="w", pady=6)

        start_btn = tk.Button(
            self.root, text="Start Quiz Experience", font=("Segoe UI", 13, "bold"),
            bg=ACCENT_COLOR, fg=TEXT_COLOR, padx=25, pady=12, relief="flat", cursor="hand2",
            command=self.load_ai_questions
        )
        start_btn.pack(pady=25)
        start_btn.bind("<Enter>", lambda e: start_btn.config(bg="#4f46e5"))
        start_btn.bind("<Leave>", lambda e: start_btn.config(bg=ACCENT_COLOR))

    def load_ai_questions(self):
        selected_cat = self.category_var.get()
        ai_category = "Hardware, Software, Networking, Programming, and Cyber Security" if selected_cat == "All Categories" else selected_cat

        self.clear_window()
        
        loading_card = tk.Frame(self.root, bg=CARD_BG, padx=40, pady=40)
        loading_card.pack(expand=True, padx=50, fill="both")

        tk.Label(
            loading_card, text=f"✨ Generating AI Questions for\n'{selected_cat}'...", 
            font=("Segoe UI", 16, "bold"), bg=CARD_BG, fg=ACCENT_COLOR, justify="center"
        ).pack(expand=True)
        
        self.root.update()

        prompt = f"""
        Generate 10 multiple-choice computer science quiz questions about {ai_category}.
        For every question, provide:
        1. A clear question
        2. Exactly 4 options (starting with A., B., C., D.)
        3. One correct answer (letter only: A, B, C, or D)
        4. The category
        Return ONLY valid JSON in this exact format:
        [
            {{
                "question": "Question here",
                "options": ["A. Option 1", "B. Option 2", "C. Option 3", "D. Option 4"],
                "answer": "A",
                "category": "{ai_category}"
            }}
        ]
        Do not add explanations or markdown.
        """
        try:
            response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            
            self.questions = json.loads(text.strip())
            random.shuffle(self.questions)
            self.current_question_index = 0
            self.score = 0
            self.fifty_fifty_remaining = 2
            self.start_quiz_loop()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate questions: {e}")
            self.create_start_screen()

    # ================= 2. QUIZ GAMEPLAY SCREEN =================
    def start_quiz_loop(self):
        if self.current_question_index >= len(self.questions):
            self.show_score_screen()
            return

        self.clear_window()
        q_data = self.questions[self.current_question_index]

        # Top Header Bar
        top_frame = tk.Frame(self.root, bg=BG_COLOR)
        top_frame.pack(fill="x", padx=40, pady=20)

        progress_text = f"Question {self.current_question_index + 1} of {len(self.questions)}"
        tk.Label(top_frame, text=progress_text, font=("Segoe UI", 11, "bold"), bg=BG_COLOR, fg=TEXT_MUTED).pack(side="left")

        self.lifeline_btn = tk.Button(
            top_frame, text=f"⚡ 50/50 Lifeline ({self.fifty_fifty_remaining})",
            font=("Segoe UI", 10, "bold"), bg=BTN_BG, fg=TEXT_COLOR,
            relief="flat", padx=12, pady=6, cursor="hand2", command=self.use_fifty_fifty
        )
        self.lifeline_btn.pack(side="right")
        if self.fifty_fifty_remaining <= 0:
            self.lifeline_btn.config(state="disabled", bg=DISABLED_BG, fg=DISABLED_FG, cursor="arrow")

        # Smooth Timer Bar Canvas
        self.timer_canvas = tk.Canvas(self.root, width=740, height=6, bg=CARD_BG, highlightthickness=0)
        self.timer_canvas.pack(padx=40)
        self.timer_rect = self.timer_canvas.create_rectangle(0, 0, 740, 6, fill=ACCENT_COLOR, outline="")

        # Main Question Card Container
        card = tk.Frame(self.root, bg=CARD_BG, padx=30, pady=25)
        card.pack(fill="both", expand=True, padx=40, pady=15)

        tk.Label(
            card, text=q_data["question"], font=("Segoe UI", 15, "bold"),
            bg=CARD_BG, fg=TEXT_COLOR, wraplength=680, justify="left"
        ).pack(anchor="w", pady=(0, 20))

        # Option Buttons
        self.option_buttons = []
        for option in q_data["options"]:
            btn = tk.Button(
                card, text=option, font=("Segoe UI", 12), bg=BTN_BG, fg=TEXT_COLOR,
                anchor="w", padx=15, pady=12, relief="flat", cursor="hand2",
                activebackground=ACCENT_COLOR, activeforeground=TEXT_COLOR,
                command=lambda o=option: self.check_answer(o[0])
            )
            btn.pack(fill="x", pady=6)
            
            # Modern Hover Animations for Options
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=BTN_HOVER) if b['state'] == 'normal' else None)
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=BTN_BG) if b['state'] == 'normal' else None)
            
            self.option_buttons.append(btn)

        # Start Timer Countdown
        self.time_left = 15
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            width = int((self.time_left / 15) * 740)
            self.timer_canvas.coords(self.timer_rect, 0, 0, width, 6)
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.check_answer(None)

    def use_fifty_fifty(self):
        if self.fifty_fifty_remaining > 0:
            self.fifty_fifty_remaining -= 1
            self.lifeline_btn.config(text=f"⚡ 50/50 Lifeline ({self.fifty_fifty_remaining})")
            if self.fifty_fifty_remaining == 0:
                self.lifeline_btn.config(state="disabled", bg=DISABLED_BG, fg=DISABLED_FG, cursor="arrow")

            q_data = self.questions[self.current_question_index]
            correct_ans = q_data["answer"]

            # Filter incorrect options and disable exactly 2 of them (leaving 2 options visible)
            incorrect_buttons = [btn for btn in self.option_buttons if btn.cget("text")[0] != correct_ans]
            to_disable = random.sample(incorrect_buttons, 2)
            
            for btn in to_disable:
                btn.config(state="disabled", bg=DISABLED_BG, fg=DISABLED_FG, cursor="arrow")

    def check_answer(self, selected_letter):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        q_data = self.questions[self.current_question_index]
        correct_letter = q_data["answer"]

        for btn in self.option_buttons:
            btn.config(state="disabled", cursor="arrow")
            btn_letter = btn.cget("text")[0]
            if btn_letter == correct_letter:
                btn.config(bg=CORRECT_COLOR, fg=TEXT_COLOR)
            elif btn_letter == selected_letter and selected_letter != correct_letter:
                btn.config(bg=WRONG_COLOR, fg=TEXT_COLOR)

        if selected_letter == correct_letter:
            self.score += 1

        self.root.after(1300, self.next_question)

    def next_question(self):
        self.current_question_index += 1
        self.start_quiz_loop()

    # ================= 3. SCORE & STATS SCREEN =================
    def show_score_screen(self):
        self.clear_window()

        total = len(self.questions)
        percentage = (self.score / total) * 100

        with open(SCORE_FILE, "a") as f:
            f.write(f"{percentage:.2f}\n")

        tk.Label(
            self.root, text="🏆 Quiz Completed Successfully!", 
            font=("Segoe UI", 22, "bold"), bg=BG_COLOR, fg=TEXT_COLOR
        ).pack(pady=25)

        card = tk.Frame(self.root, bg=CARD_BG, padx=40, pady=30)
        card.pack(pady=10, padx=50, fill="x")

        tk.Label(card, text=f"Correct Answers: {self.score} / {total}", font=("Segoe UI", 13), bg=CARD_BG, fg=TEXT_MUTED).pack(anchor="w", pady=4)
        tk.Label(card, text=f"Final Score: {percentage:.2f}%", font=("Segoe UI", 18, "bold"), bg=CARD_BG, fg=ACCENT_COLOR).pack(anchor="w", pady=4)

        tk.Label(card, text="\nTop High Scores:", font=("Segoe UI", 12, "bold"), bg=CARD_BG, fg=TEXT_COLOR).pack(anchor="w", pady=(10, 5))
        
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r") as f:
                scores = sorted([float(line.strip()) for line in f if line.strip()], reverse=True)
            for idx, sc in enumerate(scores[:3], 1):
                tk.Label(card, text=f"#{idx} — {sc:.2f}%", font=("Segoe UI", 11), bg=CARD_BG, fg=TEXT_MUTED).pack(anchor="w", pady=1)

        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(pady=25)

        graph_btn = tk.Button(
            btn_frame, text="📊 View Progress Graph", font=("Segoe UI", 11, "bold"),
            bg=BTN_BG, fg=TEXT_COLOR, padx=18, pady=10, relief="flat", cursor="hand2",
            command=self.show_graph
        )
        graph_btn.pack(side="left", padx=10)
        graph_btn.bind("<Enter>", lambda e: graph_btn.config(bg="#334155"))
        graph_btn.bind("<Leave>", lambda e: graph_btn.config(bg=BTN_BG))

        restart_btn = tk.Button(
            btn_frame, text="🔄 Play Again", font=("Segoe UI", 11, "bold"),
            bg=ACCENT_COLOR, fg=TEXT_COLOR, padx=18, pady=10, relief="flat", cursor="hand2",
            command=self.create_start_screen
        )
        restart_btn.pack(side="left", padx=10)
        restart_btn.bind("<Enter>", lambda e: restart_btn.config(bg="#4f46e5"))
        restart_btn.bind("<Leave>", lambda e: restart_btn.config(bg=ACCENT_COLOR))

    def show_graph(self):
        if not os.path.exists(SCORE_FILE):
            return
        with open(SCORE_FILE, "r") as f:
            scores = [float(line.strip()) for line in f if line.strip()]
        
        attempts = list(range(1, len(scores) + 1))
        plt.figure(figsize=(6, 4))
        plt.plot(attempts, scores, marker="o", color="#6366f1", linewidth=2.5, markersize=6)
        plt.title("Quiz Score Progress Over Time", fontsize=12, fontweight="bold")
        plt.xlabel("Attempt Number")
        plt.ylabel("Score (%)")
        plt.ylim(0, 100)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()