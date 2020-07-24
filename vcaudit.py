import sys
from argparse_factory import parse_vcaudit_args
import version_control
from process import run


def find_cf(repository_path, limit):
    change_frequency = version_control.change_frequency(repository_path, limit, run)
    return change_frequency


if __name__ == "__main__":
    args = parse_vcaudit_args(sys.argv[1:])
    print(find_cf(args.repo, args.limit).to_string(index=False))
