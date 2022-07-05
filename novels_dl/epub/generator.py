import os
from distutils.dir_util import copy_tree
from novels_dl.context import Context
from novels_dl.epub.compiler import EpubCompiler
from novels_dl.epub.writers import ChapterWriter, CleanupWriter, CoverWriter, \
    FixWriter, ImageWriter, MetadataWriter, StyleWriter


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
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(cur_dir, "template")
        copy_tree(template_dir, self.ctx.working_tempdir)
        self._run_all_writers()
        EpubCompiler(self.ctx).compile()
