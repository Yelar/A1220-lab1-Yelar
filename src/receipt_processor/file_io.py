"""File I/O utilities for reading and encoding receipt images."""

import os
import base64


def encode_file(path):
    """Encode a file as a base64 string.

    Args:
        path (str): The file path to encode.

    Returns:
        str: The base64-encoded contents of the file.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def list_files(dirpath):
    """List all files in a directory.

    Args:
        dirpath (str): The directory path to list files from.

    Yields:
        tuple: A tuple containing (filename, full_path) for each file
            in the directory. Subdirectories are excluded.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path
