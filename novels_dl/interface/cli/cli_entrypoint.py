import sys
from colorama import init as colorama_init
from colorama import Fore, Style
from novels_dl.localization import get_localization
from novels_dl.context import ContextManager
from novels_dl.epub import EpubGenerator
from novels_dl.interface.cli.steps import cli_authenticate, cli_get_output_path,\
    cli_initialize_epub_options, cli_prefetch_novel


def cli_entrypoint():
    try:
        colorama_init()
        if sys.version_info.major < 3 or sys.version_info.minor < 9:
            print(Fore.RED + Style.BRIGHT + get_localization("MAIN_WRONG_PYVERSION").replace("{1}", "3.9") + Style.RESET_ALL)
            exit(3)

        with ContextManager() as context:
            cli_authenticate(context)
            cli_prefetch_novel(context)
            cli_get_output_path(context)
            cli_initialize_epub_options(context)

            generator = EpubGenerator(context)
            generator.perform_epub_generation()
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + Style.BRIGHT + get_localization("MAIN_INTERRUPT_SIGNAL") + Style.RESET_ALL)
