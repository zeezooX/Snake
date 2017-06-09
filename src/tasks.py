import src.game_utils.function_proxy as check
from src.basic_functions import *
from src.game_utils.game_setup import *
import tkinter.messagebox as msgBox
import time


snake = get_snake()
speed = 60

"""
    This file is the one you'll be working on 
    read the documentation of the functions to know 
    what it must be able to do.
"""


# TODO:: implement this
def move_snake():
    """
    This function controls how the snake moves
    """
    global snake
    snake.body.append(get_next_point(snake.body[len(snake.body) - 1], snake.move_direction))
    snake.body.pop(0)


# TODO:: implement this
def grow_snake():
    """
    This function is responsible for growing the snake when it eats food
    """
    global snake
    snake.body.append(get_next_point(snake.body[len(snake.body) - 1], snake.move_direction))


def end_game():
    set_color_string("red")
    print_text_to_screen(0,0,"Game Over")
    time.sleep(2)
    game_over()
    # score = game_world.score
    # target = open("leaderboard.bin", "w+")
    # target.write(target.read() + "Hi")
    # target.write("\n")
    # msgBox.showinfo(title="Leaderboard", message=target.read())
    # target.close()



# TODO:: implement this
def frame_logic():  # Don't change the name of this function
    """
        This function now only changes the food location each frame into a random location which is obviously wrong :D, 
        add your own code that defines what happens when each frame is drawn, it should basically move the snake and 
        update the score and the food. 
        a simple code example: 
            move_snake()
            if (get_food_position() == calculate_snake_next_position()):
                change_food_location(random_point())
                grow_snake()
    """
    global snake
    for index, point in enumerate(snake.body):
        if (is_out_of_screen(snake.body[len(snake.body) - 1])):
            end_game()
            break
        elif(point == snake.body[len(snake.body) - 1]):
            if(index != len(snake.body) - 1):
                end_game()
                break
    else:
        if (get_food_position() == snake.body[len(snake.body) - 1]):
            while True:
                rand = random_point()
                if(rand not in snake.body):
                    break
            change_food_location(rand)
            grow_snake()
            increase_score()
        else:
            move_snake()


# TODO:: (optional) add to this function if needed
def setup():  # Don't change the name of this function
    """
    This function contains the game setup logic, add any code here that you want to 
    execute before the game is loaded  
    """
    # change speed
    global speed
    set_game_speed(speed)
    # change color
    set_color_string("blue")
    # listen to key presses
    screen.onkeypress(point_snake_up, "w")
    screen.onkeypress(point_snake_down, "s")
    screen.onkeypress(point_snake_left, "a")
    screen.onkeypress(point_snake_right, "d")
    screen.listen()


# DO NOT CHANGE THIS FUNCTION
def submit_your_functions():
    check.proton_frame_logic = frame_logic
