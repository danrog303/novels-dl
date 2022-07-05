from novels_dl.fetch import ChapterFetch
from novels_dl_tests import AuthenticationRequiringTestCase


class TestChapterFetch(AuthenticationRequiringTestCase):

    def setUp(self):
        self.fetch_client = ChapterFetch(self.ctx)

    def test_fetch_nonexistent_chapter(self):
        chapter_instance = self.fetch_client.fetch_chapter("abcde")
        self.assertIsNone(chapter_instance)

    def test_fetch_existing_chapter(self):
        chapter_instance = self.fetch_client.fetch_chapter("ff2e34b46728f988e8f38cdd9ddc7d36")
        self.assertEqual(chapter_instance.title, "Magiczny Las")
        self.assertEqual(chapter_instance.number, 277.5)
        self.assertEqual(chapter_instance.volume, 12)
        self.assertTrue(len(chapter_instance.content) > 100)
