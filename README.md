# Mines Game GUI

This repository contains a Python-based graphical user interface (GUI) for a Minesweeper-inspired betting game. Players can place bets, uncover safe spots, and cash out their profits before hitting a mine.

---

## Features

### 🎮 Gameplay
- **Minesweeper-style game mechanics:** Uncover safe spots on a grid to increase your multiplier while avoiding mines.
- **Dynamic multipliers:** Safe clicks increase your multiplier based on the number of mines and the payment table.
- **Cash out early:** Exit the game at any time to secure your profits.

### 💰 Betting System
- **Bet options:** Bet all or half of your current balance before each round.
- **Profit calculation:** Earn profits based on your bet and the current multiplier.
- **Balance management:** Game automatically resets when balance reaches zero.

### 🖥️ GUI
- **Customizable grid size:** Default 5x5 grid, scalable to different dimensions.
- **Dynamic UI updates:** Display balance, bet amount, multiplier, and profit in real time.
- **Interactive controls:** Intuitive buttons and dropdown menus for gameplay settings.

---

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/username/mines-game-gui.git
cd mines-game-gui
```

### 2️⃣ Install Dependencies
This project requires Python 3.x and the `tkinter` library (bundled with Python).

### 3️⃣ Run the Game
Run the game directly using:
```bash
python mines_game_gui.py
```

---

## How to Play

1. **Select Number of Mines:** Use the dropdown menu to choose the number of mines on the grid.
2. **Place Your Bet:** Enter your bet amount using the dropdown menu (`Bet All` or `Bet Half`).
3. **Click Grid Cells:** Uncover safe spots to increase your multiplier.
4. **Cash Out:** Click the "Cash Out" button to secure your profit before hitting a mine.

---

## Payment Table

The game uses a predefined payment table for calculating multipliers based on the number of mines and safe clicks. The table dynamically adjusts your multiplier as you uncover safe spots.

---

## Future Enhancements
- **Persistent data:** Save and load game states for continuous play.
- **Leaderboard:** Track high scores and player stats.
- **Custom difficulty:** Allow users to set grid size and mines count.

---
