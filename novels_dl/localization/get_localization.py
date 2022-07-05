import locale
from functools import cache
from novels_dl.localization.localization_entries import localization_entries


@cache
def get_current_language():
    current_language = locale.getlocale()[0].lower()
    return current_language


def get_localization(key: str) -> str:
    if get_current_language() in ["pl_pl", "pl", "polish_poland"]:
        bank_key = "pl"
    else:
        bank_key = "en"

    return localization_entries[bank_key].get(key, key)
