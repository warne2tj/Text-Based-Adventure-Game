# Text-Based-Adventure-Game - A Python Experience
Hello! My name is Thaddeus, and I created this game to serve as a reference to help guide you along creating your own text based adventure game! I know that many of you have probably not used Python before, or perhaps any programming language, but Python is a great choice for your first language!

In this README, you will find some general tips on how to write python, and some tips to help you create your own text based adventure game.

First, I would recommend downloading this game, and playing it! It doesn't have a super in-depth story, but it does have some pretty advanced technical features to help portray what is possible in a text based adventure game. But there is more that you can do as well! If you can think it, you can probably do it. Google is a great resource for specific questions that Mr. Langely or this guide does not answer (especially StackOverflow posts!). 

In order to run a python file once it has been downloaded, you must type `python python_file.py` in the Command Prompt. So in our case, use the windows key and search for "Command Prompt", and then navigate to the directory that contains the Python file (probably using `cd Downloads`), and finally type `python TextBasedAdventure.py`.

After playing the game, come back here and we will learn some basic Python.

P.S. if you are playing the game and find a bug, show it to Mr. Langley and he *might* give you some extra credit... (if you ask nicely?)

# Comments
Comments are useful and important. If you want to remember what a section of code is doing or why, add a comment! Here are two examples of comments:
```
#This is a single line comment! Anything on a line after a "#" will be treated as a comment and not a code
"""
This is a multi-line comment (also called a doc-string). Anything between the triple quotes will be treated as a comment and not code
"""
```
Remember, **I highly recommend using comments to document your code, so you can easily remember what it is doing and what it means!**

# Variale Declaration
Variables are something that store values. So if you want to remember the value 5, you can type `my_number = 5`. Then, whenever you reference `my_number`, you are really referencing the value 5. So consider this section of code:
```
my_number = 5
your_number = 3
our_number = my_number - your_number
```
Now, what is the value stored in `our_number`? Well, `5 - 3 = 2`, so the value is 2.

There are different types of variables, but Python does not require type declaration. That sounds fancy, but what that means is if you have a variable that contains an integer, you can reassign that variable with any value you want, like a string or boolean. A string is basically just a sentence, and a boolean basically just means true or false. For example:

```
my_string = "Hello world!"
my_boolean = False
your_boolean = True
```

There are different variable types, such as arrays, lists, dictionaries, etc. But I will let you explore those on your own.

# If, else, elif statements
An if statement is a conditional. IF some condition is true, then we do what is contained in the if code block. If there is an elif statement, that means `else if`. So if the first condition wasn't true, check the second condition, and if it is true, do what it designates. Finally, if there is an else statement, if condition one and condition two aren't true, do whatever the else states. If A is true, then do B. Else if (elif) C is true, then do D. Else, do E.

What this means, is we check 
```
my_bo0lean = False:
if my_boolean is True:
  print("my_boolean is True!")
elif my_boolean is False:
  print("my_boolean is False!")
else:
  print("my_boolean is neither true nor false!")
```
In this example, `my_boolean is False!` will be printed to the console. This can also be done using the negation operator, `!`. But to keep things simple, I will let you look up the negation operator. 

You can also use inequalities as a conditional in an if statement. For example
```
my_num = 5
if my_num >= 10:
  print("That is a large number!")
else:
  print("That is a small number!")
```
This code block checks if `my_num` is less than or equal to 10. In this case, the conditional is false, and the else statement will fire, printing `That is a small number!`. There are other inequality symbols as well. They are: `<`, `>`, `<=`, `>=`, `==` (where `==` is equality, so `my_num == 5` would return `True`).

The last thing we will go over is the commands that allow for checking more than on condition in an if (or elif) statement. Example:
```
my_num = 5
my_boolean = True
if my_num == 5 and my_boolean is True:
  print("Hello world!")
```
This example will print `Hello World!` as both conditions evaluate as true. The other useful operator is `or`, which will allow the if statement to fire even if only one of the statements is true. That is, if `my_boolean = False` and you use an `or` operator, `Hello World!` will still be printed.

# Loops: for and while
This is the last and more technical thing we will talk about. After this, you should be able to create a basic Python text based adventure game.

A loop is exaclty as it sounds, something that keeps happening for a specified amount of time. The for loop run ~for~ a specific amount of times, and a while loop wil run while a specific condition is true. Examples
```
#For loop
for number in range(5):
  print("This repeats 5 times!")

#While loop
my_num = 0
while my_num < 5:
  prunt("This repeates 5 times!")
  my_num = my_num + 1
```
There are a few notable things in this example. The for loop runs for each number in the range of 5. `range(5)` is actually a function call, and it returns the number 0, 1, 2, 3, and 4. Notice that it returns 5 numbers, and the loop runs 5 times. This isn't a coincidence. Also notice, the first number is 0, and not 1. This is just an annoying thing that the inventors of programming decided to do!. The important thing is that this for loop runs 5 times, and if you wanted a for loop to run 8 times, you type `for number in range(8)`.
Now, the while loops is the more useful loop for a text based adventure game. I don't think I use a single for loop. And that is because I want to continue doing a sequence of actions given that a condition isn't met. For example, in the game when you fight the guard, you continue fighting the guard `while` you and the guard still have health remaining. Or, and of the choices you made, like which weapon you wanted, you were stuck chosing a weapon `while` you had not input a valid value. I recommend you take a look at the code for this game, and get a good understanding of this concept. Not allowing a user to pick an invalid input is usually pretty important, because otherwise your game might crash!
Just to run you through how I handled these scenarios, I used the `clean_input()` function I created to check if the user entered a number or if they entered a string (text). If they entered text, it would return -1, and their choice would be set to -1 (which is a designator value that the use picked invalid choice). Then, the while loop would check if the choice was invalid, and if it was, it would tell the user to pick a proper value. I recommend using this technique for your choices as well. However, you can have the user input text and then use that as well. Say, for creating a character name, or chosing yes or no vs using 1 or 2. But again, I will let you figure out how to do this as a challenge!

# Functions/Methods
Functions and methods are both essentially the same thing (they are semantically different, but you'll learn that if you go into the programming field!). Functions will be how you go to different areas or different sequences in your story. If you look at my code, you'll see `visit_cave()`, `visit_beach()`, and `visit_marrow()`. These functions are called (by typing `visit_cave()`, for example) to do exactly what they say! You can declare a function as follows:
```
def my_function():
  print("This is my function!")
```
So, when you type `my_function()`, `This is my function!` will be printed to the console. This is how I visited other locations during the game. There is, however, an important concept to remember. In the code, after a function is called and is finished, it will return to that spot in the caller function. That sounds complex, but lets look at an example.
```
def my_function():
  print("This prints second!")
  
print("This prints first!")
my_function()
print("This prints third!")
```
In this example, these statements will print in logical order. The first will print first, the second will print second, and then the called function will finish and return to where it was called, and then the third statement is printed. The reason this is important is because say you take a player to a new location, they explore that location, and the function finishes. Then they will be brought back to the spot in the code that took them to the location in the first place! The main way that I avoided this was by only sending a player to a new area when the finished with the area they were currently in. But remember, maybe this isn't a bad thing! Say your game has the player walking down a dirt path, and they come across a house. They can enter the house, explore the location, and then continue on the path! So this feature has uses, but it can also cause some unexpected results as well. So, if while you are testing your game and you finish an area, if it brings you back to a different location unexpectedly, this could be the reason why!

# Other Advanced (But useful!) Concepts
### Variable Scope
Variable scope is kind of like sitting in a house. If I am cooking dinner in my house, people outside my house have no idea that I'm cooking dinner. This parallels varaible scope. For example:
```
def my_function:
  my_num = 5

print(my_num)
```
This code will throw an error, because the variable `my_num` is locally scoped to `my_function`. That means only `my_function` knows what `my_num` is. So any code outside that function doesn't know what `my_num` is. This also goes the other way, and is what we would call global variables.
```
def my_function
  global my_num
  my_num = 10
  
my_num = 5
print(my_num)
my_function()
print(my_num)
```
In this example, `my_num` is a global varialbe declared outside of any function. That means that any function can access it using the keyword `global`. We use this to change the value of `my_num` to 10. So this code will print 5, and then will call the function, changing the value of `my_num`, and then will print 10. This is incredibly useful for character statistics or items. In my code, I use this to check if the user has a health potion or if they have a shield. If you look at my combat encounter with the guard, I use it a lot in order to to control the flow of the fight, as well as to calculate the damage that the player deals to the guard.

### Function Parameters
Function parameters are variables that are passed into a function. This allows that variable to be used in that function. This is useful if you don't want a varaible to have a global scope. But if you want, **you don't need to use this! You can use global variables instead!** For example:
```
def my_function(my_variable):
  print(my_variable)

your_variable = 5
my_function(your_variable)
```
This example might be a little confusing. This code only prints the number 5, but it does it in an interesting way. Outside of the function we declare `your_variable` and give it the value of 5. Then we pass `your_variable` into `my_function`. Inside this function, the passed in variable has the name `my_variable`. We didn't rename any variables, we just created a new one for the function to use. `my_variable` means nothing outside of `my_function` (because of variable scope). I use this when calculating the damage that the guard does to the player. Feel free to check that code out for a functional and more complex example. The guard deals damage based on if he is going to use a special attack and if the player is defending. Both of these conditions are passed into the `calculate_guard_damage()` function.

### Display "Graphics"
There is a way to display some form of "graphics" for your program. You can do this in two ways: using `print()` statements to display a series of characters onto the screen, thus creating text based graphics. Since this is a text based adventure game, this is probably the closest to graphics you can get. Another way would be to print the contents of a text file. While I don't do this in my program, you can [use this StackOverflow post](https://stackoverflow.com/questions/18256363/how-do-i-print-the-content-of-a-txt-file-in-python) to do it in your program!

# What I Recommend Copying From My Program
There are three functions from this that I recommend copying, `clear()`, `clean_input()` and `format_console()`. These are useful functions that I call quite regularly, and I imagine you will as well. The `clear()` function does exactly what is sounds, it clears the terminal from all text content. The `format_console()` function contains a way to resize the console and add background and foreground colors. You can play with the numbers in this command, `os.system('color 20')`, in order to change the color of the background and foreground (text) colors. Play with it in your own program and it will become more clear. Finally, `clean_input()` is how I check to see if a player's input is a number. If it's not a number, it returns the value -1, and then I check for that value to see if the user input a number or not. If they entered a number, it will return the number they entered. Just copy and paste these three functions into your code, and you can use them how you see fit. But remember, **there are different ways to validate or check user input.** You don't have to use the method that I used.

# How To Set Up Your Program
I recommend a few things that will make creating your program easier. These things will keep you from running into many errors.
1. The first, is to decalare all player stats or booleans at the beginning of your program. This helps to standardize the location of these variables and make them easier to define.
2. Next, decalare all functions that you are going to use. This is because Python is *dynamically compiled*. The code reads like a book. While the program is running, **it doesn't know about any code that is has not read yet**. So, if you have a function declared at the end of the file, you can't call it at the beginning of the file. To avoid these areas, have all your functions (different locations, damage calculators, etc.) after your global character statistics variables.
3. Finally, write the code that starts the adventure at the end of the file. This is just an extension of point two. If you start your adventure at the end, all character statistics and functions will be defined, and you shouldn't run into any `reference before assignment` errors. These errors occur when no variable or function exists at the scope that you called it.
4. IF you run into an error, Google it! There is nothing wrong with Googling a problem. Google is an excellent resource, especially if the error you are running into is a common error. You will likely find a StackOverflow post that contains your error, an explanation of why it occured, and how to fix it.

I have included a starter file that designates and follows the tips that are outlined above. Feel free (and I recommend!) downloading this file to use as a base for creating your own adventure game! With all this being said, goodluck!
