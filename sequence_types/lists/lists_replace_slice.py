computer_parts = ["pc",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse pad"
                  ]

print(computer_parts)

print(computer_parts[3])
print(computer_parts[3:])

# # When replacing a slice, Python will replace with the contents of the iterable on the right side of expression
# # This will input each individual character of "trackpad" into the list "computer_parts"
# computer_parts[3:] = "trackpad"

# To add "trackpad" to the list "computer_parts", we must make "trackpad" an iterable (in this case, a list)
computer_parts[3:] = ["trackpad"]

print(computer_parts)