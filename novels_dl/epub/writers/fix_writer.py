import os
from glob import iglob
from novels_dl.epub.writers import Writer
from novels_dl.localization import get_localization
from novels_dl.utils import file_rewrite


class FixWriter(Writer):
    """Slightly improves formatting of some e-books."""

    def write(self):
        self.ctx.logger(get_localization("FIX_WRITER_BEGIN"))

        for chapter_path in iglob(os.path.join(self.ctx.working_tempdir, "text", "*.html")):
            with open(chapter_path, "r+", encoding="UTF-8") as chapter_file:
                chapter_html = chapter_file.read()
                self.ctx.logger(get_localization("FIX_WRITER_REDUNDANT_BRS") + chapter_path)
                chapter_html = chapter_html.replace("<p><br>", "<p>").replace("<p><br/>", "<p>").replace("<p><br />", "<p>")

                self.ctx.logger(get_localization("FIX_WRITER_HYPHENS") + chapter_path)
                chapter_html = chapter_html.replace("<p>- ", "<p>– ")
                file_rewrite(chapter_file, chapter_html)

        self.ctx.logger(get_localization("FIX_WRITER_END"))
