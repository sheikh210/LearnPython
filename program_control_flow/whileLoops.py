exits = ['north', 'south', 'east', 'west']
exit_choice = None

while exit_choice not in exits:
    exit_choice = input("Which exit will you choose?: ").lower()
    if exit_choice.casefold() == "quit":
        print("GAME OVER")
        break

else:
    print("Exited using the {} door".format(exit_choice))



