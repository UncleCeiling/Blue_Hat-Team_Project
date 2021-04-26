# pylint: disable=unused-variable
# Initialisation

    # Declare Variables

difficulty = 1                                          # Current difficulty setting - indexes via: difficulty_options[difficulty]
difficulty_options = ["Easy","Normal","Hard"]           # Possible difficulty options
colour = "d"                                            # Current colour setting - indexes via: colour_options[0][colour_options.index(colour)]
colour_options = [["d","r","y","g","c","b","m","i"],["Default","Red","Yellow","Green","Cyan","Blue","Magenta","Default Inverted"],["\u001b[0m","\u001b[0m\u001b[31m","\u001b[0m\u001b[33m","\u001b[0m\u001b[32m","\u001b[0m\u001b[36m","\u001b[0m\u001b[34m","\u001b[0m\u001b[35m","\u001b[0m\u001b[30;47m"]] # Possible colour options, names and codes

    # Import functions from libraries

from os import chdir, path                              # To set Working Directory
from random import sample                               # For sampling lists

    # Set Working directory to file directory

chdir(path.dirname(__file__))

    # Import data from .txt into arrays - example layout:
    # var_name = (open("txt_file_name.txt","r").readlines())[0].split(",")

highscore = (open("highscore.txt","r").readlines())[0].split(",")
adjective = (open("weapon_adjectives.txt", "r").readlines())[0].split(",")
noun1 = (open("weapon_nouns1.txt", "r").readlines())[0].split(",")
noun2 = (open("weapon_nouns2.txt", "r").readlines())[0].split(",")

# Functions

def sar_start_function(): # Syed's start function (HAS PLACEHOLDER - line 31)
    print("start screen")
    var = input("Please enter something to continue : ")
    if var == (""):
        sar_start_function()
    else:
        return

def print_credits():
    print("""
========Codenation Blue-hats========\n\n        Crara Loft made by:\n\nPesh B\n\nSyed R\n\nAmir H\n\nMike D\n\nChris F\n\n""")

def highscore():
    hs1 = [highscore[0]]
    hs2 = [highscore[1]]
    hs3 = [highscore[2]]
    def print_hs():
        print(f"=============HIGH SCORES============\n\n{hs1[0]}:{hs1[1]}\n\n{hs2[0]}:{hs2[1]}\n\n{hs3[0]}:{hs3[1]}")
    
def gen_weapon(): # Weapon Generator - call to generate a weapon - returns a string
    sample_adjective = sample(adjective,1)[0]
    sample_noun1 = sample(noun1,1)[0]
    sample_noun2 = sample(noun2,1)[0]
    return (f"{sample_adjective} {sample_noun1} of {sample_noun2}")

def options_menu(): # Options Menu - call to run options - does not return anything
    def print_options_main():                                               # Prints the options menu
        print(f"\n============OPTIONS MENU============\n\n       Difficulty||{difficulty_options[difficulty]}\n\n      Text Colour||{colour_options[1][colour_options[0].index(colour)]}\n\n================Exit================") #36 characters wide - print menu
    def difficulty_menu():                                                  # Difficulty Menu - call to run diff options - does not return anything
        def print_diff_menu(): # Prints the diff menu
            print(f"\n==========DIFFICULTY MENU===========\n\n  Difficulty is currently: {difficulty_options[difficulty]}\n\n    Easy       Normal       Hard\n\n================Exit================")
        global difficulty
        print_diff_menu() #print difficulty menu
        option_choice = (input("\nPlease select a difficulty : "))[0].lower() #take diff input
        while option_choice not in ["e","n","h"]: #if invalid input, ask again, but sassy
            print_diff_menu
            option_choice = (input("Hmmm, not sure that's an option...\nWhy don't you try something else?\n\nPlease select an option : "))[0].lower()
        if option_choice == "e": #easy
            print("\nSetting difficulty to Easy")
            difficulty = 0
        elif option_choice == "n": #normal
            print("\nSetting difficulty to Normal")
            difficulty = 1
        elif option_choice == "h": #hard
            print("\nSetting difficulty to Hard")
            difficulty = 2
        else: #shouldn't happen, but here just in case
            print("\nThat didn't work, sorry!\n\nReturning you to the options menu...\n")
        return
    def colour_menu():                                                      # Colour Menu - call to run colour options - does not return anything
        def print_colour_menu(): # Prints the colour menu
            print(f"{colour_options[2][colour_options[0].index(colour)]}============COLOUR MENU=============\n\n    Colour is currently: {colour_options[1][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m|Default |  \u001b[31mRed\u001b[0m   | \u001b[33mYellow\u001b[0m |{colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m| \u001b[32mGreen\u001b[0m  |  \u001b[36mCyan\u001b[0m  |  \u001b[34mBlue\u001b[0m  |{colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m|   \u001b[35mMagenta\u001b[0m  |\u001b[30;47m  Inverted   \u001b[0m|{colour_options[2][colour_options[0].index(colour)]}\n    \u001b[0m                            {colour_options[2][colour_options[0].index(colour)]}\n================Exit================")
        global colour # To change back to current colour, use f"{colour_options[2][colour_options[0].index(colour)]}TEXT HERE"
        print_colour_menu() # Print colour menu
        colour_choice = (input("\nPlease select a colour : "))[0].lower()   # Take colour input
        while colour_choice not in (colour_options[0]+["e"]):               # If invalid input, ask again, but sassy
            print_colour_menu
            colour_choice = (input("\nHmmm, not sure that's an option...\nWhy don't you try something else?\n\nPlease select an colour : "))[0].lower()
        if colour_choice in colour_options[0]:                              # If colour selected, change colour
            colour = colour_choice                                          # Make change in variables
            print(f"\nSwitching colour to {colour_options[2][colour_options[0].index(colour)]}{colour_options[1][colour_options[0].index(colour)]}") # Print Message
        elif colour_choice == "e":                                          # If exit selected, exit to the options menu
            print("\nExiting to Options Menu...")                           # Print Message
        else:                                                               # Shouldn't happen, but here just in case
            print("\nThat didn't work, sorry!\n\nReturning you to the options menu...\n") # Print Message
        return                                                              # Go back - I WANT TO BE MONKE
    print_options_main()                                                    # Print menu
    option_choice = (input("\nPlease select an option : "))[0].lower()      # Ask for Input
    while option_choice not in ["d","c","t","e"]:                           # Check if input is valid
        print_options_main()                                                # Print menu when not valid
        option_choice = (input("Hmmm, not sure that's an option...\nWhy don't you try something else?\n\nPlease select an option : "))[0].lower() # Chastise and take new input
    if option_choice == "d":                                                # Check if input was difficulty
        difficulty_menu()                                                   # Run diff menu
        options_menu()                                                      # After diff menu is finished, open up the options menu again
    elif option_choice in ["c","t"]:                                        # Check if input was colour or text
        colour_menu()                                                       # Run colour menu
        options_menu()                                                      # After colour menu is finished, open up the options menu again
    print("\nReturning to Main Menu...")                                    # Exit must have been selected so print a message and exit
    return

# Main block
