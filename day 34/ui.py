from tkinter import *
from quiz_brain import QuizBrain 
THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", fg="white", font=("Arial", 10, "bold"))
        self.score.grid(row=0, column=1)
        self.score.config(padx=10, pady=10, bg=THEME_COLOR,)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0,)
        self.question = self.canvas.create_text(150, 125, width= 280, text="", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #self.canvas.itemconfig(self.canvas, padx=50, pady=50)
        
        true = PhotoImage(file="100-days-of-code/day 34/images/true.png")
        self.right = Button(image = true, command=self.true_button)
        self.right.config(padx=50, pady=100, highlightthickness=0,)
        self.right.grid(row=2, column=0)

        false = PhotoImage(file="100-days-of-code/day 34/images/false.png")
        self.wrong = Button(image=false, command=self.false_button)
        self.wrong.grid(row=2, column=1, )
        self.wrong.config(padx=50, pady=100, highlightthickness=0,)
        
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the test!")
            self.wrong.config(state="disable")
            self.right.config(state="disabled")

    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)