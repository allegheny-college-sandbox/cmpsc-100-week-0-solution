#!/usr/bin/env python3

# IGNORE THIS #
def open_box(combo):
    vals = [2, 6, 3]
    pts = [a * b for a, b in zip(vals, combo)]
    return sum(pts)
# IGNORE THIS #

# Set up message
message = "🎉🎉🎉You've opened the puzzle box!🎉🎉🎉"

# Initial state of buttons
buttons = [False, False, False]

buttons = [True, False, True]

# IGNORE THIS #
result = open_box(buttons)
# IGNORE THIS #

if result == 5:
    print(message)