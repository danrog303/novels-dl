import os
from novels_dl.assets.get_asset import get_asset
from novels_dl.epub.writers import Writer
from novels_dl.fetch import ChapterFetch
from novels_dl.utils import file_rewrite
from novels_dl.localization import get_localization


class ChapterWriter(Writer):
    """Fetches and saves all novel chapters. Adds downloaded chapters to table of contents."""

    def write(self):
        self.ctx.logger(get_localization("CHAPTER_WRITER_BEGIN"))
        text_declarations = ""
        text_id_declarations = ""
        nav_point_declarations = ""

        template_dir = get_asset("epub_template")

        with open(os.path.join(template_dir, "page-template.html"), "r") as page_template:
            page_template = page_template.read()

        chapters_count = len(self.ctx.downloading_novel.prefetched_chapters)
        for chapter_index, prefetched_chapter_instance in enumerate(self.ctx.downloading_novel.prefetched_chapters):
            chapter = ChapterFetch(self.ctx).fetch_chapter(prefetched_chapter_instance.url_code)
            chapter_filename = os.path.join(self.ctx.working_tempdir, f"text/part-{chapter_index}.html")
            chapter_ebook_filename = f"text/part-{chapter_index}.html"
            self.ctx.logger(f"{get_localization('CHAPTER_WRITER_ANALYZING')}: {chapter.title} ({chapter_index + 1}/{chapters_count})")

            with open(chapter_filename, "w", encoding='utf-8') as chapter_file:
                chapter_display_title = f"{chapter.volume}.{chapter.number}. {chapter.title}"
                chapter_html = page_template
                chapter_html = chapter_html.replace("!CHAPTER_NAME!", chapter_display_title)
                chapter_html = chapter_html.replace("!CHAPTER_HTML!", chapter.content)
                chapter_file.write(chapter_html)

                text_declarations += f"<item href='{chapter_ebook_filename}' id='part-{chapter_index}' media-type='application/xhtml+xml'/>\n\t\t"
                text_id_declarations += f"<itemref idref='part-{chapter_index}'/>\n\t\t"

                nav_point_declarations += f"<navPoint playOrder='{chapter_index + 1}' id='part-{chapter_index}'><navLabel><text>{chapter_display_title}</text></navLabel><content src='{chapter_ebook_filename}'/></navPoint>\n\t\t"

        self.ctx.logger(get_localization("CHAPTER_WRITER_SAVING_METADATA"))
        with open(os.path.join(self.ctx.working_tempdir, "content.opf"), "r+", encoding="UTF-8") as content_opf, \
                open(os.path.join(self.ctx.working_tempdir, "toc.ncx"), "r+", encoding="UTF-8") as toc_ncx:
            opf_content = content_opf.read()
            opf_content = opf_content.replace("!TEXT_DECLARATIONS!", text_declarations)
            opf_content = opf_content.replace("!TEXT_IDS!", text_id_declarations)
            file_rewrite(content_opf, opf_content)

            ncx_content = toc_ncx.read()
            ncx_content = ncx_content.replace("!NAV_POINTS!", nav_point_declarations)
            file_rewrite(toc_ncx, ncx_content)
        self.ctx.logger(get_localization("CHAPTER_WRITER_END"))
