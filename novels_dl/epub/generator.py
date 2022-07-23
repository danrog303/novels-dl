from distutils.dir_util import copy_tree
from typing import List, Dict
from novels_dl.assets import get_asset
from novels_dl.context import Context
from novels_dl.epub.compiler import EpubCompiler
from novels_dl.epub.writers import ChapterWriter, CleanupWriter, CoverWriter, \
    FixWriter, ImageWriter, MetadataWriter, StyleWriter
from novels_dl.localization import get_localization
from novels_dl.models import Novel
from novels_dl.utils import remove_dir_content


class EpubGenerator:
    """Generates EPUB file based on values from context object."""

    def __init__(self, ctx: Context):
        self.ctx = ctx

    def _run_all_writers(self):
        writers_order = [
            ChapterWriter,
            CoverWriter,
            FixWriter,
            MetadataWriter,
            StyleWriter,
            ImageWriter,
            CleanupWriter
        ]
        for writer in writers_order:
            writer(self.ctx).write()

    def perform_epub_generation(self):
        """Creates one epub file containing all light novel volumes."""

        self.ctx.logger(get_localization("GENERATOR_BEGIN_GENERATION") + str(self.ctx.downloading_novel))
        template_dir = get_asset("epub_template")

        # Make working tempdir empty (if volume split has been requested, directory can already contain something)
        remove_dir_content(self.ctx.working_tempdir)

        copy_tree(template_dir, self.ctx.working_tempdir)
        self._run_all_writers()
        EpubCompiler(self.ctx).compile()
        self.ctx.logger(get_localization("GENERATOR_END_GENERATION") + str(self.ctx.downloading_novel))

    def perform_multiple_volume_epub_generation(self):
        """Creates multiple epub files (one for every light novel chapter)."""
        self.ctx.logger(get_localization("GENERATION_BEGIN_MULTIPLE_GENERATIONS"))

        # Maps volume number to Novel instance
        novels: Dict[int, Novel] = dict()

        # Fill novels dict with (volume number => instance) pairs
        for chapter in self.ctx.downloading_novel.prefetched_chapters:
            existing_novel_instance = novels.get(chapter.volume, None)

            if existing_novel_instance is None:
                existing_novel_instance = novels[chapter.volume] = Novel(
                    url_code=self.ctx.downloading_novel.url_code,
                    name=f"{self.ctx.downloading_novel.name} #{chapter.volume}",
                    author=self.ctx.downloading_novel.author,
                    cover_url=self.ctx.downloading_novel.cover_url,
                    prefetched_chapters=list(),
                    volume=chapter.volume
                )

            existing_novel_instance.prefetched_chapters.append(chapter)

        # Run epub generation on every novel instance
        downloading_novel_copy = self.ctx.downloading_novel
        for novel in novels.values():
            self.ctx.downloading_novel = novel
            self.perform_epub_generation()
        self.ctx.downloading_novel = downloading_novel_copy

        self.ctx.logger(get_localization("GENERATION_END_MULTIPLE_GENERATIONS"))
