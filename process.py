import subprocess
from typing import List


def run(args: List) -> List:
    if not args:
        raise Exception("Arguments must be provided")
    return subprocess.check_output(args, universal_newlines=True).splitlines()
