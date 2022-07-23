from colorama import Fore, Style
from novels_dl.context import Context
from novels_dl.localization import get_localization


def cli_rotate_long_images(context: Context):
    """Gets email + password from standard input and tries to authenticate."""

    print(Style.BRIGHT + get_localization("CLI_ROTATE_LONG_ASK") + Style.RESET_ALL)
    print(get_localization("CLI_ROTATE_LONG_EXPLANATION") + "\n")

    choice = -1
    while choice not in [1, 2]:
        choice = input(Style.RESET_ALL + Style.BRIGHT + get_localization("UTIL_CHOOSE_1_2"))
        choice = int(choice) if choice.isnumeric() else choice

    print(Style.RESET_ALL)

    if choice == 1:
        context.epub_options.rotate_long_images = False
    elif choice == 2:
        context.epub_options.rotate_long_images = True


