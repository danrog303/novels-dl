import os

from novels_dl.localization.get_localization import get_localization
from novels_dl.utils import file_rewrite
from novels_dl.epub.writers import Writer


class MetadataWriter(Writer):
    """Writes some basic epub metadata (like author and e-book title)."""

    def write(self):
        self.ctx.logger(get_localization("METADATA_WRITER_BEGIN"))
        with open(os.path.join(self.ctx.working_tempdir, "content.opf"), "r+", encoding="utf-8") as content_opf, \
                open(os.path.join(self.ctx.working_tempdir, "toc.ncx"), "r+", encoding="utf-8") as toc_ncx:
            ncx_content = toc_ncx.read()
            opf_content = content_opf.read()

            ncx_content = ncx_content.replace("!BOOK_TITLE!", self.ctx.downloading_novel.name)
            opf_content = opf_content.replace("!BOOK_TITLE!", self.ctx.downloading_novel.name)
            opf_content = opf_content.replace("!BOOK_AUTHOR!", self.ctx.downloading_novel.author)

            file_rewrite(toc_ncx, ncx_content)
            file_rewrite(content_opf, opf_content)
        self.ctx.logger(get_localization("METADATA_WRITER_END"))
