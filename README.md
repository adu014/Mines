Mines Game GUI
This repository contains a Python-based Minesweeper-style game built with Tkinter. Players wager virtual currency and uncover tiles to increase their winnings, avoiding hidden mines. The game offers dynamic risk-reward mechanics, adjustable settings, and a user-friendly interface.

Features
Interactive Gameplay: Players click tiles to reveal safe spots, aiming to avoid mines while increasing profits through a multiplier system.
Betting System: Place wagers using the "Bet Half" or "Bet All" options, with real-time updates to balance, profits, and multipliers.
Customizable Settings: Adjust the number of hidden mines (1–20) via a dropdown menu, allowing for scalable difficulty.
Dynamic Multipliers: Winnings are determined by a progressive multiplier table based on safe clicks and mine count.
Cash-Out Option: Players can exit early to secure profits or risk continued play for higher rewards.
Game State Management: Handles wins, losses, and restarts seamlessly, resetting the game board and balance for new rounds.
How It Works
Initialize the Game:

A 5x5 grid is displayed, with hidden mines randomly placed based on the selected difficulty.
Bet Placement:

Players enter their bet amount or use the "Bet Half" or "Bet All" options.
Gameplay:

Click tiles to reveal safe spots. Safe clicks increase the multiplier, while clicking a mine ends the game.
Cash Out:

Players can exit early, securing their profits based on the current multiplier.
Win/Loss Conditions:

Reveal all safe tiles to win or click a mine to lose.
Usage Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/username/mines-game-gui.git
cd mines-game-gui
Install Python 3.x and ensure Tkinter is available.

Run the script:

bash
Copy code
python mines_game_gui.py
Controls:

Adjust mine count using the dropdown menu.
Enter your bet and click Submit Bet.
Reveal tiles by clicking on them.
Cash out using the Cash Out button to secure your profits.
Dependencies
Python 3.x
Tkinter (Standard Library)
Future Enhancements
Add leaderboards to track high scores across sessions.
Implement varying grid sizes for scalable gameplay.
Add sound effects and animations for improved user engagement.
This project demonstrates an engaging application of GUI programming in Python, combining elements of logic, strategy, and risk management for an interactive gaming experience.






