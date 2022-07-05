from novels_dl.context import Context


class Writer:
    """Base class for a writer. Writer is basically a class, which takes epub directory
    and performs some modification on it (for example changing metadata, cover, downloading images etc)."""

    def __init__(self, ctx: Context):
        self.ctx = ctx

    def write(self):
        pass
