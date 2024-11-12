# Color Fill Puzzle Game 🎨

A Python-based puzzle game where players fill a 5x5 grid with colors while ensuring no adjacent squares share the same color. Built with Pygame.

Created by Kujtim Saliu

## 📖 Game Overview

Color Fill Puzzle is an engaging puzzle game that challenges players to fill a grid with four different colors (Red, Green, Blue, and Yellow) following a simple rule: no adjacent squares can share the same color. The game features a hint system, move tracking, and score calculation to help players improve their strategies.

## 🎮 Gameplay Screenshots

### Initial Game State
![Empty Grid](screenshot1.png)
*Starting state with empty grid and color palette*

### Game in Progress with Hints
![Hints Active](screenshot3.png)
*Hint mode showing number of valid colors for each empty square*

### Completed Puzzle
![Completed Puzzle](screenshot2.png)
*Successfully completed puzzle with score display*

## ✨ Features

- 5x5 grid puzzle board
- Four distinct colors
- Hint system showing possible valid moves
- Move counter and timer
- Score tracking system
- Undo functionality
- Simple and intuitive interface

## 🎯 How to Play

1. **Objective**: Fill the entire 5x5 grid with colors while ensuring no adjacent squares (up, down, left, right) share the same color

2. **Controls**:
   - Click a color in the palette to select it
   - Click any grid square to fill it with the selected color
   - Press `H` to toggle hints
   - Press `U` to undo your last move
   - Press `R` to reset the game

3. **Scoring**:
   - Score is calculated based on moves taken and time elapsed
   - Lower scores are better
   - Try to complete the puzzle efficiently!

## 🛠️ Installation

1. Ensure you have Python 3.x installed
2. Install Pygame:
```bash
pip install pygame
```

3. Clone the repository:
```bash
git clone https://github.com/kujtimsaliu/color-fill-puzzle.git
cd color-fill-puzzle
```

4. Run the game:
```bash
python color_fill_game.py
```

## 🔍 Game Tips

- Use the hint system (H key) to see how many valid colors are available for each empty square
- Plan ahead! Sometimes you need to fill squares in a specific order
- If you make a mistake, use the undo feature (U key) instead of starting over
- Try to minimize both moves and time for the best score

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Author

Created by Kujtim Saliu

## 🌟 Acknowledgments

- Built with Pygame
- Inspired by classic color puzzle games
- Thanks to all testers and contributors