import os
from glob import iglob
from novels_dl.epub.writers import Writer
from novels_dl.localization import get_localization
from novels_dl.utils import file_rewrite
from io import StringIO


class StyleWriter(Writer):
    """Changes CSS styling of an e-book. Generated styling is based on context's EpubOptions instance."""

    def write(self):
        self.ctx.logger(get_localization("STYLE_WRITER_BEGIN"))
        with open(os.path.join(self.ctx.working_tempdir, "main.css"), "r+") as main_css:
            css_content = main_css.read()
            paragraph_separation_css = ""
            if self.ctx.epub_options.paragraph_separation_indent:
                self.ctx.logger(get_localization("STYLE_WRITER_INDENTS"))
                indent_size = self.ctx.epub_options.indent_size
                paragraph_separation_css += f"text-indent: {indent_size}; margin: 0;"
            if self.ctx.epub_options.paragraph_separation_block_margin:
                self.ctx.logger(get_localization("STYLE_WRITER_MARGINS"))
                margin_size = self.ctx.epub_options.margin_size
                paragraph_separation_css += f"margin-top: {margin_size}; margin-bottom: {margin_size};"
            css_content = css_content.replace("!INDENT_METHOD!", paragraph_separation_css)
            file_rewrite(main_css, css_content)

        if self.ctx.epub_options.convert_quotes_to_hyphens:
            for chapter_path in iglob(os.path.join("tmp", "text", "*.html")):
                print(get_localization("STYLE_WRITER_REPLACING_QUOTES") + chapter_path)
                with open(chapter_path, "r+", encoding="UTF-8") as chapter_file:
                    chapter_builder = StringIO()
                    for line in chapter_file.readlines():
                        chapter_line = line
                        if chapter_line.startswith("<p>\""):
                            chapter_line = chapter_line.replace("<p>\"", "<p>– ", 1)
                            chapter_line = chapter_line[::-1].replace("\"", "", 1)[::-1]
                        if chapter_line.startswith("<p>„"):
                            chapter_line = chapter_line.replace("<p>„", "<p>- ", 1)
                            chapter_line = chapter_line[::-1].replace("”", "", 1)[::-1]

                        chapter_builder.write(chapter_line)
                    file_rewrite(chapter_file, chapter_builder.getvalue())

        self.ctx.logger(get_localization("STYLE_WRITER_END"))
