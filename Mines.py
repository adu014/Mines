import tkinter as tk
from tkinter import ttk
import random

payment_table = {
    1: [1.01, 1.08, 1.12, 1.18, 1.24, 1.3, 1.37, 1.46, 1.55, 1.65, 1.77, 1.99],
    2: [1.08, 1.17, 1.29, 1.41, 1.56, 1.74, 1.94, 2.18, 2.47, 2.83, 3.26, 3.81],
    3: [1.12, 1.29, 1.48, 1.71, 2.05, 2.43, 2.79, 3.4, 4.07, 5.26, 6.26, 7.96],
    4: [1.18, 1.41, 1.71, 2.09, 2.58, 3.09, 3.79, 4.94, 6.88, 9.17, 12.51, 17.52],
    5: [1.24, 1.56, 2.0, 2.58, 3.39, 4.52, 6.14, 8.5, 12.04, 17.52, 25.13, 40.87],
    6: [1.3, 1.74, 2.35, 3.23, 4.52, 6.46, 8.94, 14.17, 21.89, 35.03, 58.38, 102.17],
    7: [1.37, 1.94, 2.79, 4.09, 6.14, 9.14, 14.95, 24.47, 41.6, 73.95, 138.66, 277.33],
    8: [1.46, 2.18, 3.35, 5.03, 8.5, 14.17, 21.89, 35.03, 58.38, 102.17, 189.75, 379.5],
    9: [1.55, 2.47, 4.07, 6.88, 12.04, 21.89, 35.03, 58.38, 102.17, 189.75, 379.5, 831.98],
    10: [1.65, 2.83, 5.0, 9.17, 17.52, 35.03, 58.38, 102.17, 189.75, 356.56, 831.98, 2022.54],
    11: [1.77, 3.26, 6.26, 12.51, 25.13, 58.38, 102.17, 189.75, 356.56, 831.98, 2022.54, 5657.4],
    12: [1.99, 3.81, 7.96, 17.52, 40.87, 102.17, 189.75, 356.56, 831.98, 2022.54, 5657.4, 15471.86],
    13: [2.05, 4.56, 10.35, 25.13, 66.41, 189.75, 356.56, 831.98, 2022.54, 5657.4, 15471.86, 44128.26],
    14: [2.25, 5.46, 13.8, 37.95, 113.99, 356.56, 831.98, 2022.54, 5657.4, 15471.86, 44128.26, 107075.9],
    15: [2.47, 6.66, 18.97, 59.64, 208.74, 831.98, 2022.54, 5657.4, 15471.86, 44128.26, 118973.0, 237942.34],
    16: [2.75, 8.5, 27.11, 99.39, 417.45, 2022.54, 5657.4, 15471.86, 44128.26, 118973.0, 237942.34, 525983.62],
    17: [3.09, 11.04, 40.66, 178.91, 939.26, 5657.4, 15471.86, 44128.26, 118973.0, 237942.34, 525983.62, 1187973.0],
    18: [3.54, 14.14, 65.06, 357.81, 2022.54, 15471.86, 44128.26, 118973.0, 237942.34, 525983.62, 1187973.0, 2504756.54],
    19: [4.12, 19.8, 113.89, 834.9, 525983.62, 15471.86, 44128.26, 118973.0, 525983.62, 1187973.0, 2504756.54, 5259836.2],
    20: [4.95, 29.7, 227.7, 2504.0, 525983.62, 1187973.0, 44128.26, 118973.0, 525983.62, 2504756.54, 5259836.2, 11879730.0],
}

class MinesGameGUI:
    def __init__(self, master, grid_size=5, starting_balance=100):
        self.master = master
        self.grid_size = grid_size
        self.balance = starting_balance
        self.bet = 0
        self.current_multiplier = 1.0
        self.safe_clicks = 0
        self.mines_count = 1
        self.buttons = {}
        self.mines = set()
        self.game_over = False

        self.master.title("Mines")
        self.master.configure(bg="#1c1f25")
        self.frame = tk.Frame(self.master, bg="#1c1f25")
        self.frame.pack(padx=20, pady=20)

        self.init_mine_selection()
        self.create_grid()
        self.init_controls()
        self.place_mines()

    def init_mine_selection(self):
        self.select_mine_text = tk.Label(self.frame, text="Select Mines:", fg="white", bg="#1c1f25", font=("Times New Roman", 16))
        self.select_mine_text.grid(row=0, column=0, columnspan=3, padx=(5, 5), pady=(5, 5), sticky="w")
        self.mine_options = list(range(1, 21))
        self.selected_mine_count = tk.IntVar(self.frame)
        self.selected_mine_count.set(self.mine_options[0])
        self.mine_dropdown = tk.OptionMenu(self.frame, self.selected_mine_count, *self.mine_options, command=self.update_mine_count)
        self.mine_dropdown.config(width=5, relief=tk.FLAT, highlightthickness=1, bd=0)
        self.mine_dropdown.nametowidget(self.mine_dropdown.menuname).config(bg="#2c2f36", fg="white")
        self.mine_dropdown.grid(row=0, column=2, columnspan=10, padx=(5, 5), pady=(5, 5), sticky="e")

    def init_controls(self):
        self.balance_label = tk.Label(self.frame, text=f"Balance: ${self.balance:.2f}", fg="white", bg="#1c1f25", font=("Times New Roman", 16))
        self.balance_label.grid(row=self.grid_size + 4, columnspan=self.grid_size, pady=(5, 5), sticky = "w")

        self.multiplier_label = tk.Label(self.frame, text=f"Multiplier: x{self.current_multiplier}", fg="white", bg="#1c1f25", font=("Times New Roman", 16))
        self.multiplier_label.grid(row=self.grid_size + 5, columnspan=self.grid_size, pady=(5, 5), sticky = "e")

        self.bet_label = tk.Label(self.frame, text=f"Bet Amount: $0.00", fg="white", bg="#1c1f25", font=("Times New Roman", 16))
        self.bet_label.grid(row=self.grid_size + 5, columnspan=self.grid_size, pady=(5, 5), sticky = "w")

        self.profit_label = tk.Label(self.frame, text="Profit: $0.00", fg="white", bg="#1c1f25", font=("Times New Roman", 16))
        self.profit_label.grid(row=self.grid_size + 4, columnspan=self.grid_size, pady=(5, 5), sticky = "e")

        tk.Label(self.frame, text="Enter Bet:", fg="white", bg="#1c1f25", font=("Times New Roman", 16)).grid(row=self.grid_size + 6, column=0, columnspan=2, sticky="w")
        self.bet_entry = ttk.Combobox(self.frame, font=("Times New Roman", 16), values=["Bet Half", "Bet All"], width=10)
        self.bet_entry.set("")
        self.bet_entry.grid(row=self.grid_size + 6, column=2, columnspan=3, pady=(5, 5), sticky="e")
        self.bet_entry.bind("<<ComboboxSelected>>", self.on_bet_selected)

        self.submit_bet_button = tk.Button(self.frame, text="Submit Bet", command=self.submit_bet, bg="#3c9149", fg="white")
        self.submit_bet_button.grid(row=self.grid_size + 8, columnspan=self.grid_size, pady=5, sticky="e")

        self.exit_button = tk.Button(self.frame, text="Cash Out", command=self.exit_early, state=tk.DISABLED, bg="#2c2f36", fg="white")
        self.exit_button.grid(row=self.grid_size + 8, columnspan=self.grid_size, pady=5, sticky="w")

    def on_bet_selected(self, event):
        selected = self.bet_entry.get()
        if selected == "Bet All":
            self.bet_all()
        elif selected == "Bet Half":
            self.bet_half()

    def bet_half(self):
        self.bet_entry.delete(0, tk.END)
        self.bet_entry.insert(0, str(int(self.balance / 2)))

    def bet_all(self):
        self.bet_entry.delete(0, tk.END)
        self.bet_entry.insert(0, str(int(self.balance)))

    def submit_bet(self):
        try:
            bet_value = int(self.bet_entry.get())
            if bet_value <= 0 or bet_value > self.balance:  
                self.update_balance_label(f"Invalid bet!")
            else:
                self.bet = bet_value
                self.balance = self.balance - self.bet
                self.update_balance_label()
                self.update_profit()
                self.update_bet()

                self.submit_bet_button.config(state=tk.DISABLED, bg="#2c2f36", fg="white")
                self.exit_button.config(state=tk.DISABLED, bg="#2c2f36", fg="white")

                self.bet_entry.config(state=tk.DISABLED)
                self.mine_dropdown.config(state=tk.DISABLED)
                self.profit_label.grid(row=self.grid_size + 4, columnspan=self.grid_size, pady=(5, 5), sticky = "e")
        except ValueError:
            self.update_balance_label("Invalid input!")

    def create_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                button = tk.Button(self.frame, text="", width=5, height=2, font=("Times New Roman", 14),
                                   bg="#2c2f36", fg="white", activebackground="#3a3d46",
                                   relief=tk.FLAT, 
                                   command=lambda r=row, c=col: self.click(r, c))
                button.grid(row=row+1, column=col, padx=5, pady=5)
                self.buttons[(row, col)] = button

    def place_mines(self):
        self.mines.clear()
        while len(self.mines) < self.mines_count:
            mine_position = (x := random.randint(0, self.grid_size - 1),  y := random.randint(0, self.grid_size - 1))
            self.mines.add(mine_position)

    def click(self, row, col):
        if self.game_over or self.bet == 0:
            return

        if (row, col) in self.mines:
            self.buttons[(row, col)].config(text="💣", bg="red", fg="white")
            self.exit_button.config(bg="#2c2f36", state=tk.DISABLED)
            self.end_game(False)
        else:
            self.safe_clicks += 1
            self.exit_button.config(state=tk.NORMAL)
            self.update_multiplier()
            self.update_profit()
            self.buttons[(row, col)].config(text="✅", bg="#3c9149", fg="white")
            self.check_win()

    def update_bet(self):
        bet_amount = self.bet
        self.profit_label.config(text=f"Bet amount: ${bet_amount:.2f}")
        self.profit_label.grid(row=self.grid_size + 4, columnspan=self.grid_size, pady=(5, 5), sticky = "e")

    def update_multiplier(self):
        if self.safe_clicks <= 12:
            try:
                self.current_multiplier = payment_table[self.mines_count][self.safe_clicks - 1]
            except IndexError:
                self.current_multiplier = 1.0
            self.multiplier_label.config(text=f"Multiplier: x{self.current_multiplier}")

    def update_profit(self):
        profit = (self.bet * self.current_multiplier)
        self.profit_label.config(text=f"Profit: ${profit:.2f}")
        self.profit_label.grid(row=self.grid_size + 4, columnspan=self.grid_size, pady=(5, 5), sticky = "e")

    def exit_early(self):
        profit = (self.bet * self.current_multiplier)
        print(self.balance)
        print(profit)
        print(self.bet)
        self.balance = profit + self.balance
        self.update_balance_label(f"Exited early with ${profit:.2f} profit!")
        self.exit_button.config(state=tk.DISABLED, bg="#2c2f36", fg="white")
        self.reset_game()

    def end_game(self, won):
        self.game_over = True
        if not won:
            message = "Game Over!"
            self.current_multiplier = 1.0  # Reset multiplier on loss
            self.multiplier_label.config(text=f"Multiplier: x{self.current_multiplier}")
        else:
            message = f"You Win! Final balance: ${self.balance:.2f}"

        self.update_balance_label(message)
        self.restart_game()

    def restart_game(self):
        tk.Button(self.frame, text="Play Again", command=self.reset_game, bg="#3c9149", fg="white").grid(row=self.grid_size + 10, columnspan=self.grid_size, pady=10, stick="we")

    def reset_game(self):
        if self.balance == 0:

            self.balance = 100
        self.game_over = False
        self.bet = 0
        self.safe_clicks = 0
        self.current_multiplier = 1.0
        self.submit_bet_button.config(state=tk.NORMAL, bg="#3c9149", fg="white")
        self.exit_button.config(state=tk.DISABLED, bg="#2c2f36", fg="white")  # Reset Cash Out button

        self.bet_entry.config(state=tk.NORMAL)
        self.mine_dropdown.config(state=tk.NORMAL)
        self.exit_button.config(state=tk.DISABLED)
        self.bet_entry.delete(0, tk.END)
        self.profit_label.config(text="Profit: $0.00")
        self.update_balance_label()
        self.create_grid()
        self.place_mines()

    def update_balance_label(self, message=None):
        if message:
            self.balance_label.config(text=f"{message}")
        else:
            self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

    def check_win(self):
        safe_buttons = [(r, c) for r in range(self.grid_size) for c in range(self.grid_size) if (r, c) not in self.mines]
        all_revealed = all(self.buttons[pos]["text"] == "✅" for pos in safe_buttons)

        if all_revealed:
            self.end_game(True)

    def update_mine_count(self, value):
        self.mines_count = int(value)
        self.reset_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = MinesGameGUI(root, grid_size=5, starting_balance=100)
    root.resizable(False, False)
    root.mainloop()