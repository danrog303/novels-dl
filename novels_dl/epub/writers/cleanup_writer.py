import os
from pathlib import Path
from novels_dl.epub.writers import Writer
from novels_dl.localization import get_localization


class CleanupWriter(Writer):
    """Performs cleanup and removes all unnecessary data from the epub directory."""

    def write(self):
        self.ctx.logger(get_localization("CLEANUP_WRITER_BEGIN"))

        # Remove all gitkeep files
        for gitkeep_file_path in Path(self.ctx.working_tempdir).rglob(".gitkeep"):
            os.remove(gitkeep_file_path)

        # Remove chapter template file
        os.remove(os.path.join(self.ctx.working_tempdir, "page-template.html"))

        # Remove corrupted image template file
        os.remove(os.path.join(self.ctx.working_tempdir, "image-error.jpeg"))

        self.ctx.logger(get_localization("CLEANUP_WRITER_END"))

