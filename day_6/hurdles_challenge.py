# Hurdles Challenge.
# Write a script that uses the Reeborg's World environment to navigate through a maze of hurdles.
# The turn_right() function is defined to turn the robot right by calling the turn_left() function three times.
# The jump() function is defined to make the robot jump over the hurdle by moving forward, turning right, moving forward, turning right, moving forward, and turning left.
# The while loop is used to check if the robot has reached the goal. If the robot is not at the goal, the robot checks if the front is clear. If the front is clear, the robot moves forward. If the front is not clear, the robot jumps over the hurdle.

def turn_left():
    pass  # Define the function to turn the robot left

def move():
    pass  # Define the function to move the robot forward

def at_goal():
    pass  # Define the function to check if the robot has reached the goal

def front_is_clear():
    pass  # Define the function to check if the front is clear

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
