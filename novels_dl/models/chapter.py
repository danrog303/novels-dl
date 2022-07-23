from dataclasses import dataclass
from novels_dl.models import PrefetchedNovelChapter


@dataclass
class NovelChapter(PrefetchedNovelChapter):
    """Stores fully-fetched information about single light novel chapter.
    Contains some basic metadata of chapter + HTML content of the chapter."""

    content: str
    """HTML code with content of this chapter."""
