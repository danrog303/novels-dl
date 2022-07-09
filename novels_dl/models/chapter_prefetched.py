from dataclasses import dataclass


@dataclass
class PrefetchedNovelChapter:
    """Stores basic information about single light novel chapter.
    PrefetchedNovelChapter does not store chapter's content, only some basic metadata."""

    url_code: str
    """URL code, which can be seen in browser's URL bar while reading the chapter. URL codes are 
    32 character long and consists of small latin letters and digits."""

    title: str
    """Title of this chapter."""

    volume: int
    """Light novel volume."""

    number: float
    """Chapter number."""

    def __str__(self):
        return f"{self.volume}.{self.number} ({self.title})"
