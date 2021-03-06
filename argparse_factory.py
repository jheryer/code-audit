import argparse


def parse_vcaudit_args(args):
    parser = vcaudit_arg_parse()
    return parser.parse_args(args)


def vcaudit_arg_parse():
    parser = _get_parser("Identifies change frequency of files for a given git repository")
    parser.add_argument('--repo', required=True, help='Path to git repository')
    parser.add_argument('--limit', required=False, help='Limit the number of results')
    parser.add_argument('--audit', required=True, help='Specify which audit to perform [frequency]')
    return parser


def _get_parser(description):
    return argparse.ArgumentParser(description=description)
