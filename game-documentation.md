# Color Fill Puzzle Game Documentation

## Overview
Color Fill Puzzle is a grid-based puzzle game where players must fill a 5x5 grid with colors while ensuring no adjacent squares share the same color. This document explains the game's features, implementation, and how to play.

## How to Play

### Basic Rules
1. The game presents a 5x5 grid of empty squares
2. Players must fill each square with one of four colors: Red, Green, Blue, or Yellow
3. Adjacent squares (up, down, left, right) cannot share the same color
4. The goal is to complete the entire grid while following these rules

### Controls
- **Mouse Click**: Select colors and fill grid squares
- **H key**: Toggle hint mode
- **U key**: Undo last move
- **R key**: Reset the game

### Game Features

#### Color Selection
- Four distinct colors available: Red, Green, Blue, Yellow
- Colors are displayed in a palette below the grid
- Selected color is highlighted with a larger circle
- Color names are displayed for clarity

#### Hint System
- Toggle hints with the H key
- Shows the number of valid color options for empty squares
- Helps players make strategic decisions

#### Progress Tracking
- Move counter shows total moves made
- Timer tracks elapsed time
- Score combines moves and time
- Best score is saved and displayed upon completion

#### Quality of Life Features
- Undo system for correcting mistakes
- Game prevents invalid moves automatically
- Reset option to start fresh
- Clear visual feedback for selected colors and valid moves

## Technical Implementation

### Core Components

1. **Grid System**
```python
self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
```
- 5x5 grid implemented as 2D array
- None values represent empty squares
- Colors stored as RGB tuples

2. **Move Validation**
```python
def is_valid_move(self, row, col, color):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
            if self.grid[new_row][new_col] == color:
                return False
    return True
```
- Checks adjacent squares in all four directions
- Prevents placement of same color in adjacent squares
- Ensures moves follow game rules

3. **User Interface**
- Centered grid with proper spacing
- Clear color palette with visual feedback
- Game statistics display
- Hint system overlay
- Victory message

### Key Features Implementation

1. **Undo System**
- Maintains stack of previous moves
- Each entry contains position and previous color
- Allows step-by-step move reversal

2. **Hint System**
- Calculates valid colors for each empty square
- Displays count of available options
- Updates dynamically with each move

3. **Score System**
- Combines move count and elapsed time
- Tracks best score across games
- Provides feedback on completion

## Installation & Requirements

1. Requirements:
   - Python 3.x
   - Pygame library

2. Installation:
```bash
pip install pygame
```

3. Running the game:
```bash
python color_fill_game.py
```

## Future Improvements
1. Save/load game state
2. Multiple difficulty levels
3. Custom grid sizes
4. Additional color schemes
5. Achievement system
6. Tutorial mode
