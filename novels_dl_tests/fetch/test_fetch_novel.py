from novels_dl.fetch import NovelFetch
from novels_dl_tests import AuthenticationRequiringTestCase


class TestNovelFetch(AuthenticationRequiringTestCase):

    def setUp(self):
        self.fetch_client = NovelFetch(self.ctx)

    def test_fetch_nonexistent_novel(self):
        novel_instance = self.fetch_client.fetch_novel("xyz")
        self.assertIsNone(novel_instance)

    def test_fetch_existing_chapter(self):
        novel_instance = self.fetch_client.fetch_novel("isekai-wa-smartphone-to-tomo-ni")
        self.assertEqual(novel_instance.name, "Isekai wa Smartphone to Tomo ni")
        self.assertEqual(novel_instance.author, "Fuyuhara Patora")
