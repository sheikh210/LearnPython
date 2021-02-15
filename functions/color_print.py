import colorama

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


# def color_print(text: str, effect: str) -> None:
#     """
#     Print `text` using ANSI sequences to change color/effects
#     :param text: Text to print
#     :param effect: Effect on text that is being printed.
#     """
#     print("{}{}{}".format(effect, text, RESET))
#
#
# colorama.init()
# color_print("This is in black (but it's really white due to dark theme)", BLACK)
# print("\n***TEST FOR RESET***\n")
# color_print("This is in red", RED)
# color_print("This is in green", GREEN)
# color_print("This is in yellow", YELLOW)
# color_print("This is in blue", BLUE)
# color_print("This is in magenta", MAGENTA)
# color_print("This is in cyan", CYAN)
# color_print("This is in white (but it's really grey due to dark theme)", WHITE)
# color_print("This is bold", BOLD)
# color_print("This is underlined", UNDERLINE)
# color_print("This is color-reversed", REVERSE)
# colorama.deinit()


# THIS SECTION ADDED AFTER star_examples.py
def color_print(text: str, *effects: str) -> None:
    """
    Print `text` using ANSI sequences to change color/effects
    :param text: Text to print
    :param effects: Effect(s) on text that is being printed.
    """

    effect_string = "".join(effects)
    print("{}{}{}".format(effect_string, text, RESET))


colorama.init()
color_print("This is in black, in bold & underlined (but it's really white due to dark theme)", BLACK, BOLD, UNDERLINE)
print("\n***TEST FOR RESET***\n")
color_print("This is in red, but highlighted", RED, REVERSE)
color_print("This is in green, underlined", GREEN, UNDERLINE)
color_print("This is in yellow, in bold", YELLOW, BOLD)
colorama.deinit()
