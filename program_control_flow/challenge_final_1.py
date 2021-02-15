# Write a program to print a number of options, and allow the user to select an option from the list
# The options should be numbered 1-9 (if less than 9 options, ensure there are at least 4 options)
# Make sure there is one option dedicated to quitting the program
# The program should continue looping allowing the user to choose one of the options each time around
# The loop should ONLY terminate if the user selects the option to quit the program
# If the user makes a valid choice, the program should print a short message
# The message should include the value that they typed
# Don't print a different message for each choice - only thing that should change is the value they entered
# If users choice isn't listed in the menu, nothing should be printed
# As an optional extra, modify the program so that the menu is printed again if an invalid option is chosen

division_1 = 'AFC North'
division_2 = 'AFC East'
division_3 = 'AFC West'
division_4 = 'AFC South'
division_5 = 'NFC North'
division_6 = 'NFC East'
division_7 = 'NFC West'
division_8 = 'NFC South'
quit = 'Exit'
choice = None

while choice != 0:
    choice = int(input(
        "What is your favorite NFL division?\n1\t{0}\n2\t{1}\n3\t{2}\n4\t{3}\n5\t{4}\n6\t{5}\n7\t{6}\n8\t{7}\n0\t{8}"
        "\nENTER HERE: ".format(division_1, division_2, division_3, division_4, division_5, division_6, division_7,
                                division_8, quit)))

    if choice in range(1, 9):
        print("\n***YOU SELECTED: {}***".format(choice) + "\n")
    elif choice < 0 or choice >= 9:
        print("-" * 25)
        continue


