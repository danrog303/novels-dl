import os
import re
import shutil
from PIL import Image
from io import StringIO
from glob import iglob
from novels_dl.epub.writers import Writer
from novels_dl.assets import get_asset
from novels_dl.localization import get_localization
from novels_dl.utils import file_rewrite


class ImageWriter(Writer):
    """Downloads images that are present in some novels and registers them in the epub metadata."""

    def write(self):
        self.ctx.logger(get_localization("IMAGE_WRITER_BEGIN"))
        image_counter = 0

        for chapter_path in iglob(os.path.join(self.ctx.working_tempdir, "text", "*.html")):
            self.ctx.logger(get_localization("IMAGE_WRITER_CHECKING") + chapter_path)
            with open(chapter_path, "r+", encoding="UTF-8") as chapter_file:
                chapter_html = chapter_file.read()
                image_srcs = re.findall("<img src=[\"']([^\"']*)[\"']", chapter_html)

                for image_src in image_srcs:
                    try:
                        image_src = image_src.replace("&amp;", "&")
                        self.ctx.logger(get_localization("IMAGE_WRITER_DOWNLOADING") + image_src)
                        response = self.ctx.requests.get(image_src, stream=True)
                        image = Image.open(response.raw)
                        image = image.convert('RGB')  # prevents exception when image has transparency

                        if self.ctx.epub_options.rotate_long_images and image.width > image.height:
                            image = image.rotate(270, expand=True)

                        image.save(os.path.join(self.ctx.working_tempdir, "images", f"image-{image_counter}.jpeg"))
                        del response
                        del image
                    except Exception as exc:
                        template_path = get_asset("epub_template", "image-error.jpeg")
                        target_path = os.path.join(self.ctx.working_tempdir, "images", f"image-{image_counter}.jpeg")
                        shutil.copy(template_path, target_path)
                        self.ctx.logger(get_localization("IMAGE_WRITER_ERR"))
                    finally:
                        chapter_html = chapter_html.replace(image_src, f"../images/image-{image_counter}.jpeg")
                        image_counter += 1

                file_rewrite(chapter_file, chapter_html)

        self.ctx.logger(get_localization("IMAGE_WRITER_METADATA"))
        with open(os.path.join(self.ctx.working_tempdir, "content.opf"), "r+", encoding='utf-8') as content_opf:
            opf_content = content_opf.read()
            image_declarations = StringIO()
            for image_index in range(0, image_counter):
                image_declarations.write(f'<item href="images/image-{image_index}.jpeg" id="image-{image_index}" media-type="image/jpeg"/>\n\t\t')
            opf_content = opf_content.replace("!IMAGE_DECLARATIONS!", image_declarations.getvalue())
            file_rewrite(content_opf, opf_content)

        self.ctx.logger(get_localization("IMAGE_WRITER_END"))
