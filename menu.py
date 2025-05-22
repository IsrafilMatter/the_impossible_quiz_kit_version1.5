import tkinter as tk
import webbrowser
from quiz import ImpossibleQuiz
from creator import QuizCreator

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("The Impossible Quiz")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        # ... (colors, fonts, and UI setup as before)
        # ... (button setup as before)
        # ... (hover effects as before)

    def start_quiz(self):
        self.root.withdraw()
        quiz = ImpossibleQuiz(self.root)
        quiz.run()
        self.root.deiconify()

    def start_creator(self):
        self.root.withdraw()
        creator = QuizCreator(self.root)
        creator.run()
        self.root.deiconify()

    def open_github(self):
        webbrowser.open("https://github.com/IsrafilMatter")

    def run(self):
        self.root.mainloop()
