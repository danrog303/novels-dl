from novels_dl_tests import AuthenticationRequiringTestCase


class TestAuthenticationClient(AuthenticationRequiringTestCase):
    def test_authentication_performed_correctly(self):
        self.assertTrue(self.ctx.logged_in)
        self.assertIsNotNone(self.ctx.csrf_token)
