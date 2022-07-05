from dataclasses import dataclass


@dataclass
class NovelChapter:
    """Stores information about single light novel chapter."""

    url_code: str
    """URL code, which can be seen in browser's URL bar while reading the chapter. URL codes are 
    32 character long and consists of small latin letters and digits."""

    title: str
    """Title of this chapter."""

    volume: int
    """Light novel volume."""

    number: float
    """Chapter number."""

    content: str
    """HTML code with content of this chapter."""

    def __str__(self):
        return f"{self.volume}.{self.number} ({self.content})"