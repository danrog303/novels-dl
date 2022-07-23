import os.path
import shutil
from PIL import Image
from novels_dl.epub.writers import Writer
from novels_dl.localization import get_localization
from novels_dl.utils import file_rewrite, draw_tag_on_image


class CoverWriter(Writer):
    """Downloads cover image and registers it in the epub metadata."""

    def write(self):
        self.ctx.logger(get_localization("COVER_WRITER_BEGIN"))
        if len(str(self.ctx.downloading_novel.cover_url)) > 3:
            response = self.ctx.requests.get(self.ctx.downloading_novel.cover_url, stream=True)
            with open(os.path.join(self.ctx.working_tempdir, "cover.jpeg"), 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            cover_img_path = os.path.join(self.ctx.working_tempdir, "cover.jpeg")
            title_page_xml_path = os.path.join(self.ctx.working_tempdir, "titlepage.xhtml")

            with Image.open(cover_img_path).convert("RGB") as cover, open(title_page_xml_path, "r+") as title_page:
                width, height = cover.size
                file_content = title_page.read()
                file_content = file_content.replace("!COVER_WIDTH!", str(width))
                file_content = file_content.replace("!COVER_HEIGHT!", str(height))
                file_rewrite(title_page, file_content)

                # Prints volume tag on the cover image (if volume split is on)
                if self.ctx.downloading_novel.volume is not None:
                    # "Tom" means "Volume" in Polish
                    # (Hard-coding polish string, because light novels are in Polish anyway)
                    draw_tag_on_image(cover, f"Tom {self.ctx.downloading_novel.volume}")
                    self.ctx.logger(get_localization("IMAGE_WRITER_VOLUME_TAG"))
                    cover.save(cover_img_path)

            self.ctx.logger(get_localization("COVER_WRITER_END"))
        else:
            self.ctx.logger(get_localization("COVER_WRITER_ERR"))
