from typing import Optional


class EpubOptions:
    """Stores data about ebook formatting."""

    cover_aspect_ratio: Optional[float] = None
    """If set, this option will resize cover image to match the specified aspect ratio.
    (NOT IMPLEMENTED YET)"""

    rotate_long_images: bool = False
    """If set to True, long images will be rotated 90deg to be displayed vertically.
    (NOT IMPLEMENTED YET)"""

    convert_quotes_to_hyphens: bool = False
    """If set to True, all English-styled novels will be converted to Polish style
    (see https://culture.pl/en/article/pen-to-paper-mastering-the-quirks-of-polish-writing for more information)"""

    paragraph_separation_indent = True
    """If set to True, every paragraph will start with the indent. You can specify the indent size
    by setting EpubOptions.indent_size option."""

    paragraph_separation_block_margin = False
    """If set to True, every paragraph will have margin. You can specify the margin size
    by setting EpubOption.margin_size option."""

    indent_size: Optional[str] = "1 cm"
    """Allows to specify paragraph indentation size in CSS units. If paragraph_separation_indent has 
    not been set to True, this option will be ignored."""

    margin_size: Optional[str] = "1 em"
    """Allows to specify paragraph margin size in CSS units. If paragraph_separation_block_margin has
    not been set to True, this option will be ignored."""

