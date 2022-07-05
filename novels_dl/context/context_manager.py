import requests
import tempfile
from typing import Optional
from novels_dl.context.context import Context
from novels_dl.logging import ConsoleLogger
from novels_dl.models import EpubOptions


class ContextManager:
    """
    Creates new novels_dl Context object with some initial data:
      - creates and initializes requests.Session
      - creates empty temporary directory
      - creates EpubOptions object
      - sets logging function
      - on exit, closes requests.Session and deletes temporary directory
    """

    _ctx: Optional[Context] = None
    _temporary_directory: Optional[tempfile.TemporaryDirectory] = None

    def open(self):
        self._ctx = Context()
        self.temporary_directory: Optional[tempfile.TemporaryDirectory]
        self._temporary_directory = tempfile.TemporaryDirectory()
        self._ctx.requests = requests.Session()
        self._ctx.requests.headers.update({'User-Agent': 'Mozilla/5.0'})
        self._ctx.epub_options = EpubOptions()
        self._ctx.working_tempdir = self._temporary_directory.name
        self._ctx.logger = ConsoleLogger.log
        return self._ctx

    def close(self):
        self._ctx.requests.close()
        self._temporary_directory.cleanup()
        self._ctx = None
        self._temporary_directory = None

    def __enter__(self):
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
