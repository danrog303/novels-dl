from novels_dl.context import Context


class Fetch:
    """A fetching client base class.
    Currently, it only provides Context consumer constructor, but it may be expanded in the future. """

    def __init__(self, ctx: Context):
        self.ctx = ctx
