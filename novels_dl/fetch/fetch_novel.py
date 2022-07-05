import json
from collections import deque
from typing import Optional
from bs4 import BeautifulSoup
from novels_dl.fetch import Fetch
from novels_dl.models import Novel


class NovelFetch(Fetch):
    """Allows to fetch novel data by specifying novel's URL code."""

    def _fetch_novel_chapter_url_codes(self, novel_page: BeautifulSoup):
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
            result.appendleft(toc_entry["url_code"])

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
        novel_data["chapter_url_codes"] = self._fetch_novel_chapter_url_codes(novel_page)

        return Novel(**novel_data)
