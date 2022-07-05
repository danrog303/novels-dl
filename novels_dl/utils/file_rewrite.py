from typing import IO


def file_rewrite(file_obj: IO, new_content: str):
    """Utility function, which completely rewrites specified file with new content."""
    file_obj.seek(0, 0)
    file_obj.truncate()
    file_obj.write(new_content)
