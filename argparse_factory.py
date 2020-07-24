import argparse


def parse_cf_args(args):
    parser = cf_arg_parse()
    return parser.parse_args(args)


def cf_arg_parse():
    parser = _get_parser("Identifies change frequency of files for a given git repository")
    parser.add_argument('--repo', required=True, help='Path to git repository')
    parser.add_argument('--limit', required=False, help='Limit the number of results')
    return parser


def _get_parser(description):
    return argparse.ArgumentParser(description=description)
