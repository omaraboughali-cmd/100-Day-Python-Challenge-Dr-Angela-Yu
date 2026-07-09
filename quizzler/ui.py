import tkinter as tk
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        
        # Original Score Label formatting
        self.label_score = ttk.Label(self.window, text=f"SCORE: {self.quiz.score}", 
                                     font=('arial', 40, "bold"), 
                                     foreground='white', background=THEME_COLOR)
        self.label_score.grid(column=0, row=0, pady=10, columnspan=2)
        
        # Original Canvas
        self.canvas = tk.Canvas(width=800, height=526, bg='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        
        # Original Question Label formatting (with wrap fix)
        self.label_q = ttk.Label(self.window, text="Question text here", 
                                 font=('arial', 40, "bold"), 
                                 foreground=THEME_COLOR, background='white',
                                 wraplength=750, justify="center") # wraplength added to prevent spill
        self.label_q.grid(column=0, row=1, pady=10, columnspan=2)   
        
        # Original Buttons
        self.false_img = tk.PhotoImage(file="images/false.png")
        self.button_wrong = tk.Button(image=self.false_img, highlightthickness=0, bg='white', borderwidth=0, command=lambda: self.button_clicked('False'))
        self.button_wrong.grid(row=2, column=0, pady=20, padx=200, sticky="e")
        # Add this after your button grid code
        self.label_feedback = ttk.Label(self.window, text="", font=('arial', 40, "bold"), foreground='white', background=THEME_COLOR)
        self.label_feedback.grid(column=0, row=2, columnspan=2, pady=10)
        self.true_img = tk.PhotoImage(file="images/true.png")
        self.button_right = tk.Button(image=self.true_img, highlightthickness=0, bg='white', borderwidth=0, command=lambda: self.button_clicked('True'))
        self.button_right.grid(row=2, column=1, pady=20, padx=200, sticky="w")
        
        self.get_next_question()
        self.window.mainloop()
        
    def button_clicked(self, user_answer):
        # Check answer returns True/False
        is_right = self.quiz.check_answer(user_answer)
        
        # Update the feedback label
        if is_right:
            self.label_feedback.config(text="Correct!")
        else:
            self.label_feedback.config(text="Oops!")
            
        # Optional: You can add a short delay before clearing the feedback
        self.window.after(1000, self.clear_feedback)
        
        self.get_next_question()

    def clear_feedback(self):
        self.label_feedback.config(text="")

    # def get_next_question(self):
        
    #     q = self.quiz.next_question()
    #     # Restored original font and score update
    #     self.label_score.config(text=f"SCORE: {self.quiz.score}")
    #     self.label_q.config(text=q, font=('arial', 40, "bold"))
    def get_next_question(self):
        # Reset the canvas/label background to white for the new question
        self.canvas.config(background="white")
        self.label_q.config(background="white")
        
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"SCORE: {self.quiz.score}")
            q_text = self.quiz.next_question()
            # Updating the text in the Label instead of a Canvas item
            self.label_q.config(text=q_text)
        else:
            self.label_q.config(text="You've reached the end of the quiz!")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def give_feedback(self, is_right):
        # Change both the canvas AND the label background so it looks seamless
        if is_right:
            self.canvas.config(bg="green")
            self.label_q.config(bg="green")
        else:
            self.canvas.config(bg="red")
            self.label_q.config(bg="red")
        
        # Move to next question after 1 second
        self.window.after(1000, self.get_next_question)