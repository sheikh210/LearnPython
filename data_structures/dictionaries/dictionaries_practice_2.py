computer_parts = {"1": "computer",
                  "2": "monitor",
                  "3": "keyboard",
                  "4": "mouse",
                  "5": "hdmi cable",
                  "6": "dvd drive",
                  }

current_choice = None
computer_parts_dict = {}

while current_choice != "0":
    if current_choice in computer_parts:
        chosen_part = computer_parts[current_choice]

        if current_choice in computer_parts_dict:
            computer_parts_dict.pop(current_choice)
            print(f"Removing {chosen_part}")
        else:
            computer_parts_dict[current_choice] = chosen_part
            print(f"Adding {chosen_part}")
    else:
        print("PLEASE ADD FROM AVAILABLE PARTS:\n")
        for key, value in computer_parts.items():
            print(key, value, sep=": ")

    current_choice = input("> ")

print(f"Your shopping cart: \n\t{computer_parts_dict.items()}")
