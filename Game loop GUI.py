import tkinter as tk
import random

class NumberGuessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("300x200")

        ## Generate a random number
        self.target_number = random.randint(1, 100)

        ## Game instructions
        self.instructions_label = tk.Label(self, text="Guess a number between 1 and 100:")
        self.instructions_label.pack(pady=10)

        ## Entry field for user input
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack(pady=10)

        ## Submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        ## Result label
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess == self.target_number:
                self.result_label.config(text="Congratulations! You guessed the number correctly.")
            elif guess < self.target_number:
                self.result_label.config(text="Your guess is too low. Try again.")
            else:
                self.result_label.config(text="Your guess is too high. Try again.")
            self.guess_entry.delete(0, tk.END)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    game = NumberGuessGame()
    game.mainloop()