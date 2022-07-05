from getpass import getpass
from colorama import Fore, Style
from novels_dl.localization import get_localization
from novels_dl.auth import AuthenticationClient


def cli_authenticate(context):
    """Gets email + password from standard input and tries to authenticate."""

    print(Style.BRIGHT + get_localization("MAIN_AUTH") + Style.RESET_ALL + "\n")

    auth_email = input(Style.BRIGHT + get_localization("MAIN_AUTH_EMAIL") + Style.RESET_ALL)
    auth_password = getpass(Style.BRIGHT + get_localization("MAIN_AUTH_PASSWORD") + Style.RESET_ALL)
    auth_client = AuthenticationClient(context)
    auth_result = auth_client.authenticate(auth_email, auth_password)

    if auth_result:
        print("\n" + Fore.GREEN + Style.BRIGHT + get_localization("MAIN_AUTH_OK") + Style.RESET_ALL)
    else:
        print("\n" + Fore.RED + Style.BRIGHT + get_localization("MAIN_AUTH_ERR") + Style.RESET_ALL)
        exit(1)
