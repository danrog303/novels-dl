import os
import unittest
from typing import Optional
from novels_dl.context.context import Context
from novels_dl.context.context_manager import ContextManager
from novels_dl.auth.authentication_client import AuthenticationClient


class AuthenticationRequiringTestCase(unittest.TestCase):
    """Base class for test cases that require authentication on novelki.pl.
    All test cases extending this class require NOVELS_DL_EMAIL and NOVELS_DL_PASSWORD environment variable."""

    _ctx_manager: Optional[ContextManager] = None
    ctx: Optional[Context] = None

    @classmethod
    def setUpClass(cls):
        login = os.environ.get("NOVELS_DL_EMAIL", None)
        password = os.environ.get("NOVELS_DL_PASSWORD", None)

        if login is None:
            raise RuntimeError("This test case requires authentication. Please set NOVELS_DL_EMAIL env variable. ")
        if password is None:
            raise RuntimeError("This test case requires authentication. Please set NOVELS_DL_PASSWORD env variable. ")

        cls._ctx_manager = ContextManager()
        cls.ctx = cls._ctx_manager.open()
        auth_client = AuthenticationClient(cls.ctx)
        auth_result = auth_client.authenticate(login, password)

        if not auth_result:
            raise RuntimeError("Authentication unsuccessful. Please check your credentials.")

    @classmethod
    def tearDownClass(cls):
        cls._ctx_manager.close()
