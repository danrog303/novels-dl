from dataclasses import dataclass
from typing import List, Optional
from novels_dl.models import PrefetchedNovelChapter


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

    prefetched_chapters: List[PrefetchedNovelChapter]
    """List of prefetched chapters (basic information about chapters)."""

    volume: Optional[int]
    """Volume number. If null, it means that ebook is not split into multiple volumes."""

    def __str__(self):
        return f"{self.name} (by {self.author})"

    def __init__(self, url_code: str, name: str, author: str, cover_url: str,
                 prefetched_chapters: List[PrefetchedNovelChapter], volume: Optional[int] = None):
        self.url_code = url_code
        self.name = name
        self.author = author
        self.cover_url = cover_url
        self.prefetched_chapters = prefetched_chapters
        self.volume = volume
