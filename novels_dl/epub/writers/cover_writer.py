import os.path
import shutil
from PIL import Image
from novels_dl.epub.writers import Writer
from novels_dl.localization import get_localization
from novels_dl.utils import file_rewrite


class CoverWriter(Writer):
    """Downloads cover image and registers it in the epub metadata."""

    def write(self):
        self.ctx.logger(get_localization("COVER_WRITER_BEGIN"))
        if len(str(self.ctx.downloading_novel.cover_url)) > 3:
            response = self.ctx.requests.get(self.ctx.downloading_novel.cover_url, stream=True)
            with open(os.path.join(self.ctx.working_tempdir, "cover.jpeg"), 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response

            with Image.open(os.path.join(self.ctx.working_tempdir, "cover.jpeg")) as cover, \
                 open(os.path.join(self.ctx.working_tempdir, "titlepage.xhtml"), "r+") as titlepage:
                width, height = cover.size
                file_content = titlepage.read()
                file_content = file_content.replace("!COVER_WIDTH!", str(width))
                file_content = file_content.replace("!COVER_HEIGHT!", str(height))
                file_rewrite(titlepage, file_content)

            self.ctx.logger(get_localization("COVER_WRITER_END"))
        else:
            self.ctx.logger(get_localization("COVER_WRITER_ERR"))
