from dataclasses import dataclass
from typing import List


@dataclass
class Novel:
    url_code: str
    """Novel's URL slug. Typically consists of small latin letters separated with a hyphen,
    for example 'this-is-a-url-code-of-some-light-novel'."""

    name: str
    """Novel's name."""

    author: str
    """Novel's author."""

    cover_url: str
    """Cover image URL."""

    chapter_url_codes: List[str]
    """List of URL codes of all chapters in the novel. See NovelChapter class for URL code explanation."""

    def __str__(self):
        return f"{self.name} (by {self.author})"
