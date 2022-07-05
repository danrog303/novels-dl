import os
import shutil
from pathlib import Path
from novels_dl.context import Context


class EpubCompiler:
    """Allows to compile epub directory to epub file. It's pretty simple, because
    epub file is basically zip file with changed extension."""

    def __init__(self, ctx: Context):
        self.ctx = ctx

        # Remove trailing slash if exists
        if self.ctx.epub_output_path.endswith('/') or self.ctx.epub_output_path.endswith('\\'):
            self.ctx.epub_output_path = self.ctx.epub_output_path[:-1]

        # If path is like "/home/my_user/Documents/file.epub"
        # Convert it to "/home/my_user/Documents/file" (compile() method adds the extension by itself)
        if Path(self.ctx.epub_output_path).suffix == '.epub':
            stem = Path(self.ctx.epub_output_path).stem
            directory = os.path.dirname(self.ctx.epub_output_path)
            self.ctx.epub_output_path = os.path.join(directory, stem)

    def compile(self):
        shutil.make_archive(self.ctx.epub_output_path, 'zip', self.ctx.working_tempdir)
        shutil.move(f"{self.ctx.epub_output_path}.zip", f"{self.ctx.epub_output_path}.epub")
