from typing import List


def change_frequency_command(path) -> List:
    if not path or path == "./":
        return ["git", "log", "--format=format:", "--name-only"]
    else:
        return ["git", "-C", path, "log", "--format=format:", "--name-only"]
