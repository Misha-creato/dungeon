import os


def is_file_available(file: str):
    if os.path.isfile(file) and os.path.getsize(file) > 0:
        return True
    return False
