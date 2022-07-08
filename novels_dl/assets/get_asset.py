import os
from typing import Collection


def get_asset(*args: str):
    """
    Returns absolute path to specified asset.
    For example, on Linux get_asset('epub_template', 'META-INF', 'container.xml') can return
    '/home/myuser/novels-dl/novels_dl/assets/epub_template/META-INF/container.xml'.
    """

    assets_dir = os.path.dirname(os.path.realpath(__file__))
    requested_path = os.path.join(assets_dir, *args)
    return requested_path
