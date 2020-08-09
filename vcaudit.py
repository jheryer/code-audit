import frequency
import sys
from argparse_factory import parse_vcaudit_args
from complexity import get_complexity_by_file
from process import run


def find_cf(repository_path, limit):
    change_frequency = frequency.change_frequency(repository_path, limit, run)
    complexity = get_complexity_by_file("/home/jheryer/Projects/python/maat-scripts/miner/complexity_calculations.py", repository_path)
    print(complexity)
    return change_frequency


audit_dispatcher = {"frequency": find_cf}

if __name__ == "__main__":
    args = parse_vcaudit_args(sys.argv[1:])

    if args.audit in audit_dispatcher:
        print(audit_dispatcher[args.audit](args.repo, args.limit).to_string(index=False))
    else:
        print("Error: {} is not a valid audit".format(args.audit))
