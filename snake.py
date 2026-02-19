
import curses
import random

# Initialize curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
curses.noecho()

# Set up game window
height, width = stdscr.getmaxyx()
window = curses.newwin(height, width, 0, 0)
window.border(0)
window.nodelay(True)  # Non-blocking input
window.timeout(100)   # Refresh every 100ms

# Initialize snake and food
snake = [[4, 5], [4, 4], [4, 3]]  # Snake is a list of coordinates
food = [10, 10]
window.addch(food[0], food[1], curses.ACS_PI)  # ACS_PI is a character for food

# Initialize score
score = 0

# Initial direction
direction = curses.KEY_RIGHT

# Game loop
while True:
    # Get user input
    key = window.getch()
    if key != curses.ERR:
        if key in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, 27]:
            direction = key

    # Calculate next head position
    head = snake[0]
    if direction == curses.KEY_RIGHT:
        new_head = [head[0], head[1] + 1]
    elif direction == curses.KEY_LEFT:
        new_head = [head[0], head[1] - 1]
    elif direction == curses.KEY_UP:
        new_head = [head[0] - 1, head[1]]
    elif direction == curses.KEY_DOWN:
        new_head = [head[0] + 1, head[1]]
    else:
        new_head = head  # Keep moving in the same direction

    # Check game over conditions
    if (
        new_head[0] == 0
        or new_head[0] == height - 1
        or new_head[1] == 0
        or new_head[1] == width - 1
        or new_head in snake
    ):
        break  # Game over

    # Snake eating food
    if new_head == food:
        score += 1
        food = None
        while food is None:
            new_food = [random.randint(1, height - 2), random.randint(1, width - 2)]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)

    else:
        # Move snake by adding new head and removing tail
        last = snake.pop()
        window.addch(last[0], last[1], ' ')  # Clear the last segment

    snake.insert(0, new_head)
    window.addch(new_head[0], new_head[1], curses.ACS_CKBOARD)

    # Update score
    window.addstr(0, 2, f"Score: {score}")

# End screen
window.clear()
window.addstr(height // 2, width // 2 - 4, "Game Over")
window.refresh()
window.getch()

# Clean up curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

print(f"Final score: {score}")
