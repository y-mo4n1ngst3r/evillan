import os
import time

COLORS = {"green": "\033[92m", "red": "\033[91m", "yellow": "\033[93m", "reset": "\033[0m"}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_blinking_ascii():
    """Display blinking ASCII art."""
    art = r"""
                            ___    ___
                        __ /\_ \  /\_ \
           __   __  __ /\_\\//\ \ \//\ \      __      ___
         /'__`\/\ \/\ \\/\ \ \ \ \  \ \ \   /'__`\  /' _ `\
        /\  __/\ \ \_/ |\ \ \ \_\ \_ \_\ \_/\ \L\.\_/\ \/\ \
        \ \____\\ \___/  \ \_\/\____\/\____\ \__/.\_\ \_\ \_\
         \/____/ \/__/    \/_/\/____/\/____/\/__/\/_/\/_/\/_/
    """
    for color in ["green", "red", "yellow"]:
        clear_screen()
        print(f"{COLORS[color]}{art}{COLORS['reset']}")
        time.sleep(0.5)
