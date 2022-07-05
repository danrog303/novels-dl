import re
from typing import Optional


def css_unit_exists(css_unit) -> bool:
    return css_unit in \
        ["cm", "mm", "in", "px", "pt", "pc", "em", "ex", "ch", "rem", "vw", "vh", "vmin", "vmax", "%"]


def css_unit_format(css_unit_str: str) -> Optional[str]:
    """
    Tries to format string to a valid CSS unit.
    For example, css_unit_format('1 PX') will return '1px' (whitespace will be stripped + unit will be lowercase).
    If specified value cannot be formatted to a valid CSS unit, None will be returned instead.
    """

    # Remove all whitespace (taking advantage of str.split's behavior with no sep parameter)
    css_unit_str = "".join(css_unit_str.split())

    # Replace commas with points
    css_unit_str = css_unit_str.replace(",", ".")

    # Make css_unit lowercase
    css_unit_str = css_unit_str.lower()

    # Get unit (i.e. "px" by using regular expression)
    regex_matches = re.search(r"^(\d+\.?\d*)([a-z]+)$", css_unit_str)

    if regex_matches is not None and len(regex_matches.groups()) == 2:
        css_unit = regex_matches.group(2)
        if css_unit_exists(css_unit):
            return css_unit_str
        else:
            return None
    else:
        return None
