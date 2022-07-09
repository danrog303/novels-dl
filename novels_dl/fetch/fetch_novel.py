import json
from collections import deque
from typing import Optional, Collection
from bs4 import BeautifulSoup
from novels_dl.fetch import Fetch
from novels_dl.models import Novel, PrefetchedNovelChapter


class NovelFetch(Fetch):
    """Allows to fetch novel data by specifying novel's URL code."""

    def _prefetch_novel_chapters(self, novel_page: BeautifulSoup) -> Collection[PrefetchedNovelChapter]:
        result = deque()

        # Obtain chapter url code of some random novel chapter
        chapter_url = str(novel_page.select_one("a.card-body.card-link")["href"])
        chapter_url_code = chapter_url.split("/")[-1]

        # Url code of any chapter in the novel allows to use /api/reader/toc endpoint to fetch the table of contents
        toc_endpoint = f"https://novelki.pl/api/reader/toc/{chapter_url_code}"
        toc_result = self.ctx.requests.get(toc_endpoint)
        toc_data = json.loads(toc_result.content)["data"]

        # Append all fetched toc entries to the result
        for toc_entry in toc_data:
            prefetched_chapter_data = dict()
            prefetched_chapter_data["title"] = toc_entry["title"]
            prefetched_chapter_data["number"] = toc_entry["number"]
            prefetched_chapter_data["volume"] = toc_entry["volume"]
            prefetched_chapter_data["url_code"] = toc_entry["url_code"]

            result.appendleft(PrefetchedNovelChapter(**prefetched_chapter_data))

        return result

    def fetch_novel(self, novel_url_code: str) -> Optional[Novel]:
        novel_endpoint = f"https://novelki.pl/projekty/{novel_url_code}"
        novel_response = self.ctx.requests.get(novel_endpoint)
        novel_page = BeautifulSoup(novel_response.content, "html.parser")

        if novel_response.status_code == 404:
            return None

        novel_data = dict()
        novel_data["url_code"] = novel_url_code
        novel_data["name"] = novel_page.select_one("h3").text
        novel_data["author"] = novel_page.select("p.h5 span")[1].text
        novel_data["cover_url"] = "https://novelki.pl" + novel_page.select_one("main#app img")["src"]
        novel_data["prefetched_chapters"] = self._prefetch_novel_chapters(novel_page)

        return Novel(**novel_data)
