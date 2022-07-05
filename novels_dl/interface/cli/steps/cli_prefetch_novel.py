from colorama import Style, Fore
from novels_dl.localization import get_localization
from novels_dl.fetch import NovelFetch


def cli_prefetch_novel(context):
    """Asks user which novel they want to download and fetches its metadata."""

    print(Style.BRIGHT + "\n" + get_localization("MAIN_NOVEL_KEY"))
    novel_url_key = input("\n" + get_localization("MAIN_NOVEL_KEY_INPUT") + Style.RESET_ALL)
    novel_fetch_client = NovelFetch(context)
    novel_instance = novel_fetch_client.fetch_novel(novel_url_key)

    if novel_instance:
        context.downloading_novel = novel_instance
        print(Style.BRIGHT + Fore.GREEN + "\n" + get_localization("MAIN_NOVEL_KEY_OK"))
        print(Style.RESET_ALL + Fore.GREEN + get_localization("MAIN_NOVEL_KEY_DETECTED") + str(novel_instance))
    else:
        print(Style.BRIGHT + Fore.RED + "\n" + get_localization("MAIN_NOVEL_KEY_INVALID"))
        exit(2)
