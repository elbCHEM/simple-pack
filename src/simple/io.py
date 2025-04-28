"""
Very simple io.
"""
import os
from typing import LiteralString


def append_a_little_message_to_a_file(message: LiteralString, file: os.PathLike) -> None:
    """Print a little message to a file in append mode"""
    if not os.path.isfile(file):
        raise FileNotFoundError(f"File {file} does not exists")
    with open(file, mode="a") as filewrapper:
        filewrapper.writelines([message, ])
