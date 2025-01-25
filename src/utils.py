import os

# ANSI color codes for terminal text
COLORS = {
    "green": "\033[92m",
    "red": "\033[91m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}


def clear_screen():
    """
    Clear the terminal screen.
    This works across platforms (Windows and Unix-based systems).
    """
    os.system("cls" if os.name == "nt" else "clear")


def color_text(text, color="reset"):
    """
    Apply ANSI color codes to text for terminal output.
    
    :param text: The text to colorize.
    :param color: The color name (e.g., 'green', 'red', 'yellow').
                  Defaults to 'reset' (no color).
    :return: Colorized text.
    """
    color_code = COLORS.get(color, COLORS["reset"])
    return f"{color_code}{text}{COLORS['reset']}"


def print_colored(text, color="reset"):
    """
    Print text in a specified color to the terminal.
    
    :param text: The text to print.
    :param color: The color name (e.g., 'green', 'red', 'yellow').
                  Defaults to 'reset' (no color).
    """
    print(color_text(text, color))


def load_payloads(file_path):
    """
    Load payloads from a file.
    
    :param file_path: Path to the file containing payloads.
    :return: A list of payloads as strings.
    """
    if not os.path.exists(file_path):
        print_colored(f"Error: File '{file_path}' not found.", "red")
        return []
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]
