from colorama import Style
from novels_dl.localization import get_localization
from novels_dl.utils import css_unit_format


def cli_initialize_epub_options(context):
    print(Style.RESET_ALL + Style.BRIGHT + "\n" + get_localization("MAIN_CONVERT_HYPHENS"))
    print(get_localization("MAIN_CONVERT_HYPHENS_OPTION_1"))  # do not change dialogue introduction method
    print(get_localization("MAIN_CONVERT_HYPHENS_OPTION_2") + "\n")  # convert quotes to hyphens
    convert_hyphens = -1
    while not str(convert_hyphens).isnumeric() or int(convert_hyphens) not in [1, 2]:
        convert_hyphens = input(Style.BRIGHT + get_localization("MAIN_CONVERT_HYPHENS_PROMPT") + Style.RESET_ALL)
    if int(convert_hyphens) == 2:
        context.epub_options.convert_quotes_to_hyphens = True

    print(Style.BRIGHT + "\n" + get_localization("MAIN_PARAGRAPH_SEPARATION"))
    print(get_localization("MAIN_PARAGRAPH_SEPARATION_OPTION_1"))  # English style
    print(get_localization("MAIN_PARAGRAPH_SEPARATION_OPTION_2"))  # Polish style
    print(get_localization("MAIN_PARAGRAPH_SEPARATION_OPTION_3") + "\n")  # Combined style
    context.epub_options.paragraph_separation_indent = context.epub_options.paragraph_separation_block_margin = False
    paragraph_separation = -1
    while not str(paragraph_separation).isnumeric() or int(paragraph_separation) not in [1, 2, 3]:
        paragraph_separation = input(Style.BRIGHT + get_localization("MAIN_PARAGRAPH_SEPARATION_PROMPT") + Style.RESET_ALL)
    if int(paragraph_separation) in [1, 3]:
        context.epub_options.paragraph_separation_block_margin = True
    if int(paragraph_separation) in [2, 3]:
        context.epub_options.paragraph_separation_indent = True

    if context.epub_options.paragraph_separation_indent:
        print("\n" + Style.BRIGHT + get_localization("MAIN_INDENTS_SIZE") + "\n")
        print(Style.RESET_ALL + get_localization("MAIN_INDENTS_SIZE_SUGGESTION") + "\n")
        indent_size = None
        while indent_size is None:
            indent_size = input(Style.BRIGHT + get_localization("MAIN_INDENTS_SIZE_PROMPT") + Style.RESET_ALL)
            indent_size = css_unit_format(indent_size)
        context.epub_options.indent_size = indent_size

    if context.epub_options.paragraph_separation_block_margin:
        print("\n" + Style.BRIGHT + get_localization("MAIN_MARGIN_SIZE"))
        print(Style.RESET_ALL + get_localization("MAIN_MARGIN_SIZE_SUGGESTION") + "\n")
        margin_size = None
        while margin_size is None:
            margin_size = input(Style.BRIGHT + get_localization("MAIN_MARGIN_SIZE_PROMPT") + Style.RESET_ALL)
            margin_size = css_unit_format(margin_size)
        context.epub_options.margin_size = margin_size

    print()
