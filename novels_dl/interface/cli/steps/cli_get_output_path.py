from colorama import Style
from novels_dl.localization import get_localization


def cli_get_output_path(context):
    """Asks user where to save generated EPUB file."""
    print("\n" + Style.RESET_ALL + Style.BRIGHT + get_localization("MAIN_EPUB_OUTPUT"))
    context.epub_output_path = input("\n" + Style.RESET_ALL + get_localization("MAIN_EPUB_OUTPUT_PROMPT"))
