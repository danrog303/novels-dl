from requests.sessions import Session
from typing import Optional, Callable
from novels_dl.models import EpubOptions
from novels_dl.models import Novel


class Context:
    """Application context. Instance of this class is passed between most novels_dl classes and functions."""

    # -------------------- AUTHENTICATION STUFF --------------------

    requests: Optional[Session] = None
    """Requests session object, which allows to keep authentication on https://novelki.pl/ persistent."""

    logged_in: bool = False
    """True if the user is authenticated on https://novelki.pl/."""

    csrf_token: Optional[str] = None
    """CSRF token, which is needed to send POST requests to https://novelki.pl/"""

    # -------------------- EPUB BUILDING STUFF --------------------

    working_tempdir: Optional[str] = None
    """Absolute path to temporary directory, where content of epub file will be stored."""

    epub_options: Optional[EpubOptions] = None
    """Instance of object that stores information about ebook formatting."""

    epub_output_path: Optional[str] = None
    """Path where novelki_dl should save generated epub file."""

    # -------------------- NOVEL DATA STUFF --------------------

    downloading_novel: Optional[Novel] = None
    """Novel that is currently downloaded."""

    # -------------------- LOGGING STUFF --------------------

    logger: Callable[[str], None] = lambda msg: None
    """Logger function, which will be used to log data."""
