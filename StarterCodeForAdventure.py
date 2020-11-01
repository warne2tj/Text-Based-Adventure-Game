""" IMPORT STATEMENTS """
#These are import statements. They are used to include extra functions used for the program.
#Declare them at the top, and you'll always know where to find them.
import time #This is used for time.sleep() statements. Time.sleep(2) will cause the program to wait for 2 seconds.
import os #This is used for formatting and clearing your console
import random #This is used for random number generators (useful for combat)
import sys #This is used for terminating the program using sys.exit(), useful for if the player dies!



""" GLOBAL VARAIBLES """
#Include Character Stats and Booleans here (prevents many variable scope errors)
heath = 100
strength = 10
has_weapon = True
is_awesome = True



""" FUNCTION DECLARATIONS """
#Declare all your functinos here BEFORE you start your adventure (prevents many variable scope errors)
def my_function():
  print("This text based adventure game is going to be awesome!!!")
def use_global_variables():
    global health
    health = health + 10
    print("This function used a global variable and gave the player 10 health!")
def use_parameters(passed_in_value):
    #An example call to this function is use_parameters(has_weapon)
    if passed_in_value is True:
        print("This function checks if the variable passed in is true!")

        
#Below are the functions that I recommended keeping from my program
"""
format_console method - This command is going to format the console to the dimensions
that we want, as well as the background and text color. You can use this to change the
color of the text and/or background midgame. But I'll let you figure that out.
"""
def format_console():
    os.system('mode con: cols=175 lines=50')
    os.system('color 20')

"""
Clear method - This is how you can clear the text from the screen. Just type clear().
"""
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

"""
clean_input method - This is how we are going to make sure that responses are numbers
and not text. Feel free to allow text based responses (yes/no) in your game. But you'll
have to figure it out.

If the text entered what a number, it will return that number in
integer form (because the user inputs text (a string), not an integer). If it the text
entered was a actual text (a string), return -1.
"""
def clean_input(response):
    try:
        response = int(response)
        return response
    except ValueError:
        return -1




""" START YOUR ADVENTURE """
#Here is where you will start your adventure! Ask for names, choose a class, pick a location to travel to, etc!
print("Hello player! What name would you like to go y?")
player_name = input("Enter your name: ")
print("Hello " + player_name + "!")
