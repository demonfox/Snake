# Snake Game

A classic Snake game implemented in Python using the `curses` library.

## Features

- Playable snake controlled with arrow keys
- Random food generation
- Score tracking
- Game over on wall collision or self-collision
- Clean terminal-based UI

## Requirements

- Python 3.x
- Unix-like terminal (macOS/Linux)

## How to Play

1. Run the game:
   ```bash
   python3 snake.py
   ```

2. Controls:
   - **Arrow Keys**: Move the snake
   - **ESC**: Quit the game

3. Eat food (π symbol) to grow and increase your score.
4. Avoid hitting the walls or yourself!

## Game Mechanics

- The snake moves continuously in the current direction
- Each food item eaten increases score by 1
- The game ends when the snake collides with walls or itself

## License

MIT
