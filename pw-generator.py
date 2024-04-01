#!/bin/python3

#########################################
# Name:   password generator            #
# Author: https://github.com/w-manuel   #
#########################################

# import random and system module
import random, sys

# Create empty lists and set counter variable x to 0
full_list = []
random_pw = []
x = 0

# Predefine possible characters etc. in selection lists
symbol_list = ['@','!','§','$','%','&','/','(',')','?']
number_list = ['0','1','2','3','4','5','6','7','8','9']
lower_case_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Print Headline after program starts
print("### Simple password generator ###")

# Query the password length selected by the user
pw_length = int(input("Choose the length of the password [4-128]: "))
if pw_length > 3 and pw_length < 129:

    # Query the password composition selected by the user and add to the generation list
    # If "ENTER, Y or y" is selected, the list is used for random generation. All other characters are ignored
    pw_symbols = str(input("Symbols? [Y/n]: "))
    if pw_symbols == "y" or pw_symbols == "Y" or pw_symbols == "":
        full_list.append(''.join(symbol_list))

    pw_uppercase = str(input("Upper-case letters? [Y/n]: "))
    if pw_uppercase == "y" or pw_uppercase == "Y" or pw_uppercase == "":
        full_list.append(''.join(upper_case_list))

    pw_lowercase = str(input("Lower-case letters? [Y/n]: "))
    if pw_lowercase == "y" or pw_lowercase == "Y" or pw_lowercase == "":
        full_list.append(''.join(lower_case_list))

    pw_numbers = str(input("Numbers? [Y/n]: "))
    if pw_numbers == "y" or pw_numbers == "Y" or pw_numbers == "":
        full_list.append(''.join(number_list))
    
    # password is generated randomly from the selected lists. the loop runs through x cycles depending on the selected password length
    while x < pw_length:
        random_pw.append(random.choice(random.choice(full_list)))
        x+=1

    # Remove unnecessary characters from the completed list and display the password to the user in the terminal
    print("\nPassword:")
    print(''.join(random_pw))

# If invalid characters are typed by the user during the query, the program terminates with the error return value 1
else:
    print("Input is out of range... exit")
    sys.exit(1)
