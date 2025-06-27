# 🎮 Python Tic-Tac-Toe Game

A fully functional desktop Tic-Tac-Toe game built with Python tkinter featuring modern UI design, score tracking, sound effects, and visual feedback. Demonstrates object-oriented programming principles and GUI development skills transitioning from Java to Python.

## 🎯 What I Built

**Complete Game Implementation**: Full two-player Tic-Tac-Toe with automatic turn switching and win detection  
**Modern Visual Design**: Blue and dark gray color scheme with dynamic button highlighting  
**Score Tracking System**: Persistent score display tracking X wins, O wins, and ties  
**Audio Feedback**: Sound effects for moves and wins using Windows system sounds  
**Professional UI**: Clean layout with proper spacing and responsive design  
**Visual Win Indication**: Winning combinations highlighted in red with white text  

## ✨ Key Features

🎲 **Two-Player Gameplay**: Alternating X and O turns with automatic switching  
🎨 **Modern Color Scheme**: Blue (#3498db) and dark gray (#2c3e50) alternating pattern  
🔤 **Clean Typography**: 30pt Arial font with orange text for clear visibility  
📊 **Live Score Tracking**: Real-time display of wins and ties  
🔊 **Sound Effects**: Beep sounds for moves (800Hz) and wins (1000Hz)  
⚡ **Instant Visual Feedback**: Button colors change immediately on player moves  
🏆 **Win Highlighting**: Winning combinations highlighted in red background  
🖱️ **One-Click Moves**: Simple click interface for placing X's and O's  
🎯 **Move Validation**: Prevents overwriting existing moves  
🔄 **Auto-Reset**: Automatic game reset after win or tie  

## 🏗️ Technical Architecture

```
TicTacToe Game
├── Game Logic
│   ├── Turn management (X/O alternation)
│   ├── Win detection algorithm (8 combinations)
│   ├── Score tracking and persistence
│   └── Move validation system
├── User Interface
│   ├── tkinter Frame-based layout
│   ├── 3x3 Button grid with custom styling
│   ├── Score display label
│   └── Modern color scheme implementation
├── Audio System
│   ├── winsound integration for move feedback
│   ├── Different tones for moves vs wins
│   └── Cross-platform Windows sound support
└── Event System
    ├── Lambda-based button click handling
    ├── Real-time game state updates
    └── Automatic turn switching logic
```

## 🔧 Implementation Details

**Game Board**: 9-button grid using tkinter Button widgets with grid layout management  
**Turn Logic**: String-based turn switching between 'X' and 'O' players  
**Win Detection**: Algorithm checking 8 possible winning combinations (rows, columns, diagonals)  
**Score Persistence**: In-memory score tracking with live UI updates  
**Visual Feedback**: Dynamic button background colors indicating player moves  
**Sound Integration**: Windows winsound module for audio feedback  
**Layout Management**: Frame-based organization separating score display from game grid  

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/python-tic-tac-toe.git

# Navigate to project directory
cd python-tic-tac-toe

# Run the game (Python 3.6+ required)
python tictactoe.py
```

### IDE Setup:
- Import the project into your Python IDE (PyCharm, VS Code, IDLE)
- Ensure Python 3.6+ is installed with tkinter support
- Run `tictactoe.py` as the main module
- **Note**: Disable virtual environment if encountering tkinter issues

### Requirements:
- Python 3.6+
- tkinter (included with most Python installations)
- winsound (Windows only - for sound effects)

## 🔧 Technologies & Concepts

**Python 3** - Core programming language  
**tkinter** - Built-in GUI framework for desktop applications  
**Object-Oriented Programming** - Single-class architecture with method separation  
**Event-Driven Programming** - Lambda functions and callback-based user interactions  
**Game Development** - Turn-based logic and state management  
**Audio Programming** - System sound integration for user feedback  
**Grid Layout Management** - Mathematical positioning using modulo arithmetic  

## 💡 Technical Highlights

**Efficient Grid Mapping**: Uses `i // 3` and `i % 3` for converting linear index to 2D coordinates  
**Dynamic Color Management**: Button colors change based on player moves and game state  
**Lambda Event Handling**: Closure-based button click handlers preserving button index  
**Win Detection Algorithm**: Optimized checking of all 8 possible winning combinations  
**Sound Feedback System**: Different frequencies for different game events  
**Memory-Efficient Design**: Single list storing button references for easy manipulation  
**Professional UI Standards**: Consistent spacing, colors, and typography  

## 📖 Learning Outcomes

This project demonstrates proficiency in:

**Python GUI Development**: Professional desktop application using tkinter framework  
**Game Development Fundamentals**: Turn-based logic, win conditions, and state management  
**Object-Oriented Design**: Clean class structure with logical method separation  
**Event-Driven Programming**: Responsive user interface with immediate feedback  
**Audio Integration**: System sound programming for enhanced user experience  
**Algorithm Implementation**: Efficient win detection and grid management algorithms  

## 🎮 How to Play

1. **Start Game**: Launch the application to display the 3x3 game board
2. **Player X Goes First**: Click any empty cell to place an X (button turns red)
3. **Alternating Turns**: Game automatically switches to Player O (button turns green)
4. **Make Your Move**: Continue clicking empty cells to place X's and O's
5. **Visual Feedback**: Hear beep sounds and see immediate color changes
6. **Win Detection**: Winning combinations highlight in red automatically
7. **Score Tracking**: Wins and ties are tracked in the header display
8. **Auto-Reset**: Game resets automatically after each round

## 🎨 Design Features

**Color Palette**: Modern blue (#3498db) and dark gray (#2c3e50) base with dynamic highlights  
**Player Colors**: Red background for X moves, green background for O moves  
**Typography**: 30pt Arial font for optimal readability on all screen sizes  
**Spacing**: 5px padding between cells for clean visual separation  
**Window Size**: 500x500 pixels optimized for desktop gameplay  
**Audio Design**: Distinct frequencies (800Hz/1000Hz) for different game events  

*Part of my programming portfolio* [Github](https://github.com/AGButt04) | [LinkedIn](https://www.linkedin.com/in/abdul-ghani-butt-290056338/)
