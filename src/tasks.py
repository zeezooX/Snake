import src.game_utils.function_proxy as check
from src.basic_functions import *
from src.game_utils.game_setup import *
import tkinter.messagebox as msgBox
import tkinter
import time
import os
import sys
import pickle

"""
    This file is the one you'll be working on 
    read the documentation of the functions to know 
    what it must be able to do.
"""

snake = get_snake()  # Gets snake object


# Declaring GUI elements
easy = tkinter.Button(text="Easy")
normal = tkinter.Button(text="Normal")
hard = tkinter.Button(text="Hard")
label = tkinter.Label(text="Enter your name:")
text = tkinter.Entry()
button = tkinter.Button(text="Enter")


def activate(e):
    """
    Event handler for difficulty buttons
    """
    global easy
    global normal
    global hard
    # Setting an appropriate speed for the selected difficulty
    if(e.widget == easy):
        set_game_speed(180)
    elif(e.widget == normal):
        set_game_speed(120)
    elif(e.widget == hard):
        set_game_speed(60)
    check.proton_frame_logic = frame_logic
    # Removing unnecessary GUI elements
    easy.pack_forget()
    normal.pack_forget()
    hard.pack_forget()


def score(e):
    """
    This function manages the leaderboard
    """
    global text
    try:
        with open("leaderboard.pickle", "rb") as f:
            leaderboard = pickle.load(f)
    except:
        leaderboard = []
    leaderboard.append((game_world.score, text.get()))
    leaderboard.sort(reverse=True)
    if(len(leaderboard) > 10):
        leaderboard = leaderboard[:10]
    temp = ["{0}. {1}: {2}".format(str(index + 1), element[1], str(element[0]))
            for index, element in enumerate(leaderboard)]
    msgBox.showinfo("Leaderboard", "\n".join(str(e) for e in temp))
    with open("leaderboard.pickle", "wb") as f:
        f.truncate()
        pickle.dump(leaderboard, f)
    os.execl(sys.executable, sys.executable, *sys.argv)


# Binding the difficulty buttons to their event handler
easy.bind('<Button-1>', activate)
normal.bind('<Button-1>', activate)
hard.bind('<Button-1>', activate)
button.bind('<Button-1>', score)


# TODO:: implement this
def move_snake():
    """
    This function controls how the snake moves
    """
    global snake
    snake.body.append(get_next_point(
        snake.body[len(snake.body) - 1], snake.move_direction))
    snake.body.pop(0)


# TODO:: implement this
def grow_snake():
    """
    This function is responsible for growing the snake when it eats food
    """
    global snake
    snake.body.append(get_next_point(
        snake.body[len(snake.body) - 1], snake.move_direction))


def end_game():
    """
    This function is called when the player loses
    """
    check.proton_frame_logic = None
    set_color_string("red")
    print_text_to_screen(0, 0, "Game Over")
    try:
        import winsound
        winsound.Beep(100, 1000)
    except:
        time.sleep(1)
    time.sleep(1)
    global label
    global text
    global button
    # Displays name registering GUI elements
    label.pack()
    text.pack()
    button.pack()


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
        # Checking if the snake's head is out of the grid
        if (is_out_of_screen(snake.body[len(snake.body) - 1])):
            end_game()
            break
        # Checking if the snake had eaten itself
        elif(point == snake.body[len(snake.body) - 1]):
            if(index != len(snake.body) - 1):
                end_game()
                break
    else:
        # Checking if the snake has eaten the food
        if (get_food_position() == snake.body[len(snake.body) - 1]):
            try:
                import winsound
                winsound.Beep(1000, 250)
            except:
                pass
            # Respawns food in an empty position
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
    # change color
    set_color_string("blue")
    # Play background music
    try:
        import winsound
        soundfile = "background.wav"
        winsound.PlaySound(
            soundfile, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except:
        print("Your operating system doesn't support sound playback")


# DO NOT CHANGE THIS FUNCTION
def submit_your_functions():
    # Displaying difficulty buttons
    global easy
    easy.pack()
    global normal
    normal.pack()
    global hard
    hard.pack()
