import frequency
import sys
from argparse_factory import parse_vcaudit_args
from complexity import get_complexity_by_file_list
from process import run
from pathlib import Path


def _merge_frequency_and_complexity(frequency_frame, repository_path):
    file_list = frequency_frame['file'].to_list()
    file_list = ['{0}/{1}'.format(repository_path, file) for file in file_list]
    complexity_frame = get_complexity_by_file_list(file_list, repository_path)
    merged_frame = frequency_frame.merge(complexity_frame, left_on='file', right_on='file_name')
    merged_frame.drop(columns='file', inplace=True)
    return merged_frame


def find_cf(repository_path, limit):
    change_frequency = frequency.change_frequency(repository_path, limit, run)
    merged_frame = _merge_frequency_and_complexity(change_frequency, repository_path)
    return merged_frame


audit_dispatcher = {"frequency": find_cf}

if __name__ == "__main__":
    args = parse_vcaudit_args(sys.argv[1:])
    repo_path = Path(args.repo)
    print(repo_path)
    if args.audit in audit_dispatcher:
        print(audit_dispatcher[args.audit](args.repo, args.limit).to_string(index=False))
    else:
        print("Error: {} is not a valid audit".format(args.audit))
