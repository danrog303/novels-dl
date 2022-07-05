import json
import time
from typing import Optional
from novels_dl.localization import get_localization
from novels_dl.fetch import Fetch
from novels_dl.models import NovelChapter


class ChapterFetch(Fetch):
    """Allows to fetch chapter data by specifying chapter's URL code."""

    def fetch_chapter(self, chapter_url_code: str) -> Optional[NovelChapter]:
        chapter_endpoint = f"https://novelki.pl/api/reader/chapters/{chapter_url_code}"
        chapter_result = self.ctx.requests.get(chapter_endpoint)

        if chapter_result.status_code == 404:
            return None

        # Handle 429 status code (Too Many Requests)
        if chapter_result.status_code == 429:
            retry_after = chapter_result.headers.get("retry-after") or 40
            self.ctx.logger(get_localization("FETCH_CHAPTER_HTTP429").replace("{1}", retry_after))
            time.sleep(int(retry_after) + 1)
            chapter_result = self.ctx.requests.get(chapter_endpoint)

        # Parse JSON and return NovelChapter instance
        chapter_data = json.loads(chapter_result.content)["data"]
        return NovelChapter(chapter_data["url_code"], chapter_data["title"], chapter_data["volume"],
                            chapter_data["number"], chapter_data["content"])
