from colorama import Style, Fore
from novels_dl.localization import get_localization


def cli_volume_split(context):
    """Asks user if they want to enable volume-split feature.
    Returns True, if user want to enable volume-split (otherwise False)."""

    print(Style.BRIGHT + get_localization("CLI_VOL_SPLIT_ASK"))
    print(Style.RESET_ALL + Fore.YELLOW + get_localization("CLI_VOL_SPLIT_WARN"))

    result = -1
    while result not in [1, 2]:
        result = input(Style.RESET_ALL + Style.BRIGHT + "Wybierz 1 lub 2: ")
        result = int(result) if result.isnumeric() else result

    print("\n" + Style.RESET_ALL)
    return result == 2
