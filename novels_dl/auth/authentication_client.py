from bs4 import BeautifulSoup
from novels_dl.context import Context


class AuthenticationClient:
    """Performs authentication on https://novelki.pl/ website. Authentication will be persistent
    because of usage of requests.Session in context variable."""

    def __init__(self, ctx: Context):
        self.ctx = ctx

    def authenticate(self, email: str, password: str) -> bool:
        """Tries to authenticate with specified email and password.
        Function returns true if authentication is successful."""

        # Obtains a valid CSRF token from the main page
        main_page = BeautifulSoup(self.ctx.requests.get("https://novelki.pl/").content, "html.parser")
        csrf_token = main_page.select_one("[name='csrf-token']")["content"]

        # Sends a login request to the authentication endpoint
        login_data = {"email": email, "password": password, "_token": csrf_token}
        login_response = self.ctx.requests.post("https://novelki.pl/auth/login", data=login_data)
        login_response_page = BeautifulSoup(login_response.content, "html.parser")

        # Checks whether the user has been authenticated correctly
        # (Correct authentication redirects user to Homepage, which has "Home" in the <title> tag)
        has_authenticated = "Home" in login_response_page.select_one("title").text

        # If user has been authenticated, sets some values in the context object
        if has_authenticated:
            self.ctx.csrf_token = csrf_token
            self.ctx.logged_in = True

        return has_authenticated
