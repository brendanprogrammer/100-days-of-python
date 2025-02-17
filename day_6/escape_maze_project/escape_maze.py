# Create a maze-solving algorithm for navigating an environment where the 
# agent must reach a goal. It follows the right-hand rule, 
# always preferring to turn right when possible.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Move forward until an obstacle is hit
while front_is_clear():
    move()
turn_left()

# Main loop to navigate the maze
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()