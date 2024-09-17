#====================================================
# Filename: Prob1.py
# 
# Your name: Baily LIvengood
# Who did you work with (if anyone)?: Nobody
# Estimate for time spent (in hrs)?: 5
#====================================================

import karel

# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a function below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.



def main():
    put_beeper()
    Check_right()
    

def Check_right(): #Complete a row going right
    Checker()
    turn_left()
    if front_is_clear():
        start_line()
        turn_left()
        Check_left()

def Check_left(): #Complete a row going left
    Checker()
    turn_right()
    if front_is_clear():
        start_line()
        turn_right()
        Check_right()

def start_line(): 
    if beepers_present():
        move()
    else:
        move()
        put_beeper()


def Checker(): #Alternate beeper placement
    while front_is_clear():
        if beepers_present():
            move()
        else:
            move()
            put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Remember to define any more helper functions you want down here


